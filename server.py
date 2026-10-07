import json
import os
from datetime import date, timedelta
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(title="InvoicePilot Alexa+ MCP")

INVOICES: dict[str, dict[str, Any]] = {
    "INV-1001": {"id": "INV-1001", "customer": "Acme Studio", "amount": 1200.0, "currency": "EUR", "status": "sent", "due": "2026-10-15"},
    "INV-1002": {"id": "INV-1002", "customer": "Northstar Labs", "amount": 850.0, "currency": "EUR", "status": "paid", "due": "2026-10-02"},
    "INV-1003": {"id": "INV-1003", "customer": "Blue Harbor", "amount": 640.0, "currency": "EUR", "status": "overdue", "due": "2026-09-28"},
}

TOOLS = [
    {
        "name": "list_invoices",
        "description": "List invoices, optionally filtered by status.",
        "inputSchema": {"type": "object", "properties": {"status": {"type": "string"}}, "additionalProperties": False},
    },
    {
        "name": "get_invoice",
        "description": "Get one invoice by ID.",
        "inputSchema": {"type": "object", "properties": {"invoice_id": {"type": "string"}}, "required": ["invoice_id"], "additionalProperties": False},
    },
    {
        "name": "create_invoice",
        "description": "Create a draft invoice for a customer.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "customer": {"type": "string"},
                "amount": {"type": "number"},
                "currency": {"type": "string", "default": "EUR"},
                "due_days": {"type": "integer", "default": 14},
            },
            "required": ["customer", "amount"],
            "additionalProperties": False,
        },
    },
    {
        "name": "invoice_summary",
        "description": "Summarize outstanding, paid, and overdue invoice totals.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
    {
        "name": "ai_business_summary",
        "description": "Use Amazon Bedrock to turn invoice metrics into a concise business summary.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
]

def result_text(value: Any):
    return {"content": [{"type": "text", "text": json.dumps(value, ensure_ascii=False)}]}

def tool_call(name: str, args: dict[str, Any]):
    if name == "list_invoices":
        status = args.get("status")
        values = list(INVOICES.values())
        if status:
            values = [x for x in values if x["status"] == status]
        return result_text(values)

    if name == "get_invoice":
        invoice = INVOICES.get(args["invoice_id"])
        if not invoice:
            return {"isError": True, "content": [{"type": "text", "text": "Invoice not found"}]}
        return result_text(invoice)

    if name == "create_invoice":
        invoice_id = f"INV-{1000 + len(INVOICES) + 1}"
        invoice = {
            "id": invoice_id,
            "customer": args["customer"],
            "amount": float(args["amount"]),
            "currency": args.get("currency", "EUR"),
            "status": "draft",
            "due": str(date.today() + timedelta(days=int(args.get("due_days", 14)))),
        }
        INVOICES[invoice_id] = invoice
        return result_text(invoice)

    if name == "invoice_summary":
        outstanding = sum(x["amount"] for x in INVOICES.values() if x["status"] in {"sent", "overdue", "draft"})
        paid = sum(x["amount"] for x in INVOICES.values() if x["status"] == "paid")
        overdue = sum(x["amount"] for x in INVOICES.values() if x["status"] == "overdue")
        return result_text({"invoice_count": len(INVOICES), "outstanding_eur": outstanding, "paid_eur": paid, "overdue_eur": overdue})

    if name == "ai_business_summary":
        summary = json.loads(tool_call("invoice_summary", {})["content"][0]["text"])
        region = os.getenv("AWS_REGION")
        model_id = os.getenv("BEDROCK_MODEL_ID")
        if not region or not model_id:
            return result_text({"mode": "local", "summary": f"You have €{summary['outstanding_eur']:.2f} outstanding, including €{summary['overdue_eur']:.2f} overdue. Paid invoices total €{summary['paid_eur']:.2f}."})
        try:
            import boto3
            client = boto3.client("bedrock-runtime", region_name=region)
            prompt = f"Summarize these invoice metrics for a freelancer in two concise sentences: {summary}"
            body = {"messages": [{"role": "user", "content": [{"text": prompt}]}], "inferenceConfig": {"maxTokens": 180, "temperature": 0.2}}
            response = client.invoke_model(modelId=model_id, body=json.dumps(body), contentType="application/json", accept="application/json")
            payload = json.loads(response["body"].read())
            text = payload.get("output", {}).get("message", {}).get("content", [{}])[0].get("text", "")
            return result_text({"mode": "bedrock", "summary": text})
        except Exception as exc:
            return result_text({"mode": "fallback", "summary": f"Bedrock was unavailable, so InvoicePilot used a deterministic summary. Outstanding €{summary['outstanding_eur']:.2f}; overdue €{summary['overdue_eur']:.2f}.", "error": str(exc)})

    return {"isError": True, "content": [{"type": "text", "text": f"Unknown tool: {name}"}]}

@app.post("/mcp")
async def mcp(request: Request):
    body = await request.json()
    method = body.get("method")
    request_id = body.get("id")
    if method == "initialize":
        return JSONResponse({"jsonrpc": "2.0", "id": request_id, "result": {
            "protocolVersion": "2025-11-25",
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "invoicepilot-alexa", "version": "1.0.0"},
        }})
    if method == "tools/list":
        return JSONResponse({"jsonrpc": "2.0", "id": request_id, "result": {"tools": TOOLS}})
    if method == "tools/call":
        params = body.get("params", {})
        return JSONResponse({"jsonrpc": "2.0", "id": request_id, "result": tool_call(params.get("name"), params.get("arguments", {}))})
    return JSONResponse({"jsonrpc": "2.0", "id": request_id, "error": {"code": -32601, "message": f"Method not found: {method}"}}, status_code=400)

@app.get("/", response_class=HTMLResponse)
async def demo():
    return HTMLResponse(open("web/index.html", encoding="utf-8").read())
