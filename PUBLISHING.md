# Publishing rules

These rules decide what may appear in this repository and how it gets here.

## The boundary

Open by default, once an artifact passes the gate:

- Product principles, scope, and non-goals.
- Architecture: packages, interfaces, and how the loop works.
- Decisions: dated entries with context, options, choice, and consequences.
- Build log: curated notes from work sessions.
- Technical specs and plans, close to their working form.
- Partner-facing guides (integration, policy authoring, security notes) when they
  stabilize.

Never published here:

- Competitive analysis, market comparisons, or competitor names.
- Legal, trademark, entity, or naming-conflict material.
- Pricing, commercial terms, fundraising, or investor material.
- Partner and customer identities, agreements, or their data.
- Raw session notes, internal reports, agent transcripts, or scratch files.
- Secrets or personal data. Ever.

## The gate

Before an artifact enters a pull request, it passes this checklist:

1. Identity: we are "Solon"; never the bare phrase "Solon AI"; solonai.org appears only as
   a literal web address; the string "SolonAI" appears nowhere.
2. House style: no em dashes; no double-hyphen punctuation in prose; US English.
3. No tactical content: nothing from the never-published list, in any form.
4. No secrets or personal data beyond the public contact address.
5. Accuracy: claims match what actually shipped, with verification named; internal or
   synthetic numbers are labeled as such.
6. A date and a status (living or frozen) on every artifact.
7. Provenance noted when useful.

`scripts/gate.py` checks the mechanical parts (checks 1, 2, and secret patterns). The human
review covers the rest.

## How changes arrive

1. Draft the artifact on a branch.
2. Run `python scripts/gate.py`.
3. Open a pull request.
4. A human reviews and merges. Nothing is published without that merge.
