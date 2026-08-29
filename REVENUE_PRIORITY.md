# InvoicePilot — Revenue Priority

## Current objective
Reach €5,000/week in sustainable revenue without deceptive marketing, fabricated customers, spam, or unverified payment claims.

## Highest-impact bottleneck
The product has a useful free invoice workflow, but the paid path is still not a live self-serve transaction. The current checkout page intentionally keeps purchase buttons inactive until a real merchant payment account/link exists. Therefore the immediate priority is **not another generic invoice feature**: it is turning the paid path into a real, measurable, trustworthy transaction.

## New finding — hard dependency
A secure checkout cannot be activated honestly from the static repository alone. It requires a merchant payment account and a real hosted checkout/payment URL or a server-side payment integration with credentials supplied by the owner. Those credentials must never be committed to GitHub or embedded in the static frontend.

Until that dependency exists, the correct state is to keep checkout clearly unavailable rather than pretending that a payment was completed.

## Priority order
1. **Verified checkout** — connect a merchant-hosted payment flow and verify payment status server-side before granting Pro/Business access.
2. **Conversion instrumentation** — measure landing-page visit → invoice creation → Pro interest → checkout start → successful payment. Never infer a sale from a click or email.
3. **Vertical landing pages** — focus acquisition on one high-fit segment at a time (initially freelancers and tutors/online teachers) and compare conversion rates.
4. **Retention value** — after checkout works, add client history, reusable client records, recurring invoices and automated reminders only where they directly improve retention or willingness to pay.
5. **Higher-value plans** — €5,000/week is approximately €21,667/month. A €9/month plan alone would require roughly 2,408 active subscribers to reach that monthly revenue level. Therefore Business/team/agency plans and/or higher-value workflow features will be necessary for a credible path to the target.

## Immediate implementation checklist
- Obtain/create the merchant payment account outside the code repository.
- Create the real Pro and Business hosted checkout products/prices.
- Add only the public checkout URLs to the site.
- Keep payment verification/webhooks on a secure server; never put secret keys in `index.html`.
- Test a real payment in the provider's test mode before production activation.
- Record the first production payment only after it is actually confirmed.

## Sales principles
- Be helpful, polite and professional.
- Solve a concrete payment-follow-up problem instead of selling a generic "invoice generator."
- Use honest claims only.
- Do not buy leads, spam communities, fabricate testimonials, create fake urgency, or claim payment processing before it is actually implemented.
- Do not collect card details directly in the static frontend.

## Next implementation
The next code-side improvement should be a minimal checkout integration that accepts only verified public hosted-payment URLs, followed by server-side payment verification and privacy-conscious funnel measurement. Once the first verified purchase exists, use actual objections and conversion data to decide the next product change.

## Verified results
As of this review: **0 verified paying customers and €0 verified revenue**. No revenue result is claimed until a real payment is confirmed.
