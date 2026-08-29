# InvoicePilot — Revenue Priority

Last reviewed: 2026-08-29

## Highest-impact objective

Move from a static/free invoice utility to a product that can complete and verify a legitimate paid conversion.

## Current verified status

- Verified paying customers: 0
- Verified revenue: €0
- No financial result is claimed until a real payment is confirmed.

## Priority #1 — secure paid conversion

1. Use a merchant-hosted checkout provider.
2. Keep secret/API credentials server-side; never place secret keys in the static GitHub Pages frontend.
3. Connect successful payment to a paid entitlement/account.
4. Add customer-visible success/cancel paths.
5. Test the complete flow in the provider's test mode before enabling live sales.
6. Only enable live payments after the merchant account and product terms are properly configured.

This is the current bottleneck because the public product cannot yet complete an independently verified Pro/Business purchase.

## Positioning

Do not compete as another generic accounting suite. Lead with the concrete workflow:

**Create invoice → add payment link → track unpaid → send a professional follow-up.**

Initial customer segments:
- freelancers/consultants
- tutors and online teachers
- small service businesses

The promise must remain factual. Do not claim InvoicePilot processes payments unless the product actually does so.

## Funnel

Visitor → useful free invoice → saved/reusable workflow → Pro/Business value → secure checkout → verified paid account → retention.

Measure each stage before scaling traffic. If traffic is low, improve acquisition; if visitors do not start an invoice, improve positioning/UX; if users create invoices but do not buy, improve offer/trust/checkout; if paid users churn, improve retention.

## Revenue target reality

€5,000/week is approximately €21,667/month. A €9/month plan alone would require about 2,408 active subscribers to reach €21,667 in monthly recurring revenue. Therefore the long-term model needs higher-value Business/team/agency customers in addition to Pro.

## Acquisition

Start narrow and learn:
- create useful, search-intent pages for invoice/payment problems;
- target freelancers, tutors and small service businesses;
- use permission-based communities and personalized outreach where allowed;
- provide genuine value before asking for a sale;
- track source → activation → checkout → paid conversion;
- do not spam, scrape private data, buy fake traffic, fabricate testimonials or fabricate customer numbers.

## Next product improvements after checkout

1. Accounts and cloud-saved clients/invoices.
2. Reusable client profiles and invoice templates.
3. Recurring invoices for Pro/Business.
4. Reminder scheduling and payment-status automation.
5. Business/team roles and higher-value workflow features.

## Implementation plan

**Phase 1 — transaction:** real hosted checkout, test-mode validation, secure payment verification, success/cancel paths.

**Phase 2 — measurement:** privacy-conscious funnel events for visit, invoice creation, Pro interest, checkout start and confirmed payment. A click is not a sale.

**Phase 3 — focused acquisition:** test freelancers and tutors separately, record qualified traffic and conversion, and stop channels that produce no evidence of demand.

**Phase 4 — retention/ARPU:** build cloud accounts, client history, recurring billing and team features only after real users show demand. Use paid-customer feedback to choose priorities.

## Guardrails

No deceptive claims, fake customers, fake revenue, fabricated conversion rates, spam, undisclosed financial/legal actions, or irreversible changes. Financial/legal configuration requires appropriate owner/provider review before going live.
