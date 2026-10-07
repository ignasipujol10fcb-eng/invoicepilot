# Amazon Developer Hackathon 2026 — Submission Pack

## Project
**InvoicePilot × Alexa+**

## Primary track
Alexa+

## Mini challenge
AWS Builder

## Open Source
Yes — MIT licensed.

## One-line pitch
InvoicePilot lets Alexa+ turn natural-language business questions into safe, structured invoice actions through a self-hosted Streamable HTTP MCP server.

## Problem
Freelancers and small businesses lose time switching between dashboards to answer simple questions: What is overdue? What is outstanding? Did a client pay? Can I create the next invoice?

## Solution
InvoicePilot exposes business actions as MCP tools. An Alexa+ experience can discover the tools and call them from natural language. The browser demo makes the same flow visible to judges without requiring an Alexa device.

## Demo flow (under 3 minutes)
1. 0:00–0:20 — “What invoices need my attention?”
2. 0:20–0:50 — Show the MCP `tools/list` contract.
3. 0:50–1:20 — Call `list_invoices(status=overdue)`.
4. 1:20–1:50 — Create a draft invoice.
5. 1:50–2:20 — Ask for an AI business summary.
6. 2:20–2:50 — Show AWS Bedrock integration and explain the architecture.
7. 2:50–3:00 — Show GitHub repository and open-source license.

## What changed during the hackathon
The original InvoicePilot concept predates the event. The hackathon work adds:
- Alexa+ integration architecture
- Self-hosted MCP endpoint
- MCP initialization and tool discovery
- Invoice action tool contracts
- Streamable HTTP transport endpoint
- AWS Bedrock business-summary path
- Judge-facing browser demo
- Test coverage and hackathon documentation

## Product feedback

### Alexa+ / MCP
**Used for:** exposing invoice actions as discoverable tools.

**Worked well:** the tool abstraction makes business actions explicit and auditable. It is easy to map a natural-language request to a narrowly scoped operation.

**Needs work:** local onboarding would benefit from a first-party MCP validator and a one-command Alexa+ integration smoke test.

**Would build again:** Yes.

### AWS Bedrock
**Used for:** turning structured invoice metrics into concise business language.

**Worked well:** structured metrics plus a small prompt are enough for a useful summary.

**Needs work:** model availability and regional prerequisites could be surfaced more clearly during setup.

**Would build again:** Yes.

## Friction log

### MCP onboarding
- Task: validate a self-hosted Streamable HTTP server.
- Expected: quick local protocol validation.
- Actual: protocol details require careful manual testing.
- Severity: Important.
- Workaround: added explicit `initialize`, `tools/list`, and `tools/call` test paths and documented the endpoint.

### AWS model setup
- Task: add Bedrock summarization.
- Expected: simple local test.
- Actual: model access and region availability depend on AWS account configuration.
- Severity: Important.
- Workaround: deterministic local fallback keeps the demo functional without credentials.
