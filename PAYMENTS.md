# InvoicePilot — payment strategy

## Highest-impact revenue improvement

The product must make the path from **invoice → payment** genuinely easy. A beautiful invoice generator alone is commoditized: current competitors already offer free invoicing, payment processing, reminders, recurring billing, and client portals. InvoicePilot should therefore position itself around a lightweight cash-collection workflow rather than generic invoice creation.

## Payment architecture

Use a merchant-hosted payment provider rather than collecting card details inside the static GitHub Pages application. Stripe Payment Links and Stripe-hosted invoice/payment pages support multiple payment methods, languages and currencies, and keep sensitive payment credentials outside the frontend. Verify the merchant account and exact product/price links before enabling any paid buttons.

Reference: https://stripe.com/payments/payment-links

## Product sequence

1. Free invoice creation.
2. Add a verified payment link to an invoice.
3. Track unpaid / paid status.
4. Prepare polite reminders.
5. Add recurring invoices and recurring payments after a real backend/account system exists.
6. Add analytics: outstanding amount, days overdue, collection rate.

## Pricing hypothesis

- Free: basic invoice generation and local tracking.
- Pro: €9/month — payment workflow, reminders, saved clients and recurring invoice tools when implemented.
- Business: €29/month — team features, shared client records and deeper automation when implemented.

These are hypotheses, not guaranteed market prices. Validate willingness to pay with real users.

## Revenue target math

€5,000/week is about €21,667/month on a 4.33-week approximation. At €9/month, that would require roughly 2,408 active subscribers. At €29/month, roughly 747. A blended plan mix is therefore much more realistic than relying on €9 subscriptions alone.

## Trust rules

- Never claim a payment has succeeded unless the payment provider confirms it.
- Never store card numbers, CVV, private API keys, or payment credentials in the static site.
- Never advertise features as available before they are implemented.
- Never fabricate customer counts, revenue, testimonials, or reviews.
