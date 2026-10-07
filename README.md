# InvoicePilot Alexa+ — Hackathon 2026

InvoicePilot gives Alexa+ a practical business skill: create, inspect, summarize, and track invoices through a self-hosted MCP server.

## Hackathon tracks
- Primary: Alexa+
- Mini challenge: AWS Builder
- Optional: Open Source

## What it demonstrates
The server implements an MCP-style Streamable HTTP endpoint at `/mcp` and exposes invoice tools:
- `list_invoices`
- `get_invoice`
- `create_invoice`
- `invoice_summary`

The demo UI simulates an Alexa+ conversation and calls the same MCP tools. AWS Bedrock can optionally generate a natural-language business summary.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn server:app --reload --port 8000
```

Open `http://localhost:8000`.

### Optional AWS Builder mode

Set:
```
AWS_REGION=eu-west-1
BEDROCK_MODEL_ID=amazon.nova-lite-v1:0
```

Then use the **AI Summary** action in the demo.

## MCP endpoint

POST Streamable HTTP requests to:
`http://localhost:8000/mcp`

The server supports MCP-style `initialize`, `tools/list`, and `tools/call` requests and returns JSON responses suitable for an Alexa+ MCP integration adapter.

## Submission notes

This project was substantially built for the Amazon Developer Hackathon 2026. The original InvoicePilot concept existed before the hackathon; the Alexa+/MCP integration, demo experience, AWS Bedrock integration, tool contracts, and hackathon documentation are the new work.

## Product feedback

### MCP / Alexa+
What worked: the tool-oriented contract maps naturally to business actions and keeps the integration auditable.
What needs work: clearer local development tooling and a first-party validator for Streamable HTTP MCP integrations would reduce onboarding time.
Would build again: yes.

### AWS Bedrock
What worked: a small model is enough to turn structured invoice metrics into useful business language.
What needs work: clearer model-availability messaging by region and a simpler local test mode.
Would build again: yes.
