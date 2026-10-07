import json
from server import INVOICES, tool_call

def test_summary():
    result = json.loads(tool_call("invoice_summary", {})["content"][0]["text"])
    assert result["invoice_count"] == 3
    assert result["outstanding_eur"] == 1840.0
    assert result["overdue_eur"] == 640.0

def test_create_invoice():
    before = len(INVOICES)
    result = json.loads(tool_call("create_invoice", {"customer": "Test Co", "amount": 100})["content"][0]["text"])
    assert len(INVOICES) == before + 1
    assert result["status"] == "draft"

def test_list_overdue():
    result = json.loads(tool_call("list_invoices", {"status": "overdue"})["content"][0]["text"])
    assert len(result) >= 1
    assert all(x["status"] == "overdue" for x in result)
