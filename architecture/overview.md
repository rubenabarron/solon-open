# Architecture overview

Status: living | Date: 2026-09-30
Source: curated from the build.

## The loop

A decision enters through the SDK decorator, is evaluated deterministically against the
policy files, and produces one of three outcomes: allow, deny, or escalate. Escalations
land in a review queue with an evidence packet. The human decision is recorded. Similar
overrides cluster, and once a pattern is clear Solon drafts a policy rule and opens a pull
request. A human reviews and merges. The next matching case resolves without escalation.

## Packages

| Package | Purpose |
|---|---|
| `packages/sdk` | The `@governed` decorator: evaluate, then run, deny, or escalate; records evidence asynchronously |
| `packages/policy-service` | Policy DSL, validation, the git-aware loader, and the deterministic evaluator |
| `packages/evidence-service` | Append-only decision ledger, redaction before storage, precedent rows |
| `packages/escalation-service` | Review queue, evidence packets, override recording |
| `packages/reconciliation-service` | Override clustering and policy proposal generation; opens pull requests |
| `packages/graph-service` | Precedent retrieval: banding vocabulary, an embedder chain, and a provenance graph linking decisions, rules, and ratifications |
| `apps/reviewer-ui` | Queue, detail, and response screens, plus the reasoning view |
| `infra/` | Postgres with pgvector, migrations, compose stacks |
| `policies/` | The policy files; Git is the only source of truth |

## Decision flow, concretely

1. The application calls a function wrapped by `@governed`.
2. The evaluator loads the current policy and returns allow, deny, or escalate, with the
   matched rule.
3. Every outcome is recorded as evidence, with redaction applied on the way in.
4. Escalations go to the review UI. The reviewer sees the context, the matched rule, and
   related precedents.
5. The reviewer's override carries a justification and becomes evidence.
6. Three similar overrides are enough signal to propose a rule. The proposal arrives as a
   pull request with its evidence attached.
7. A human merges or rejects. Merged rules apply to every future decision.

## Deliberate constraints

- No model in the allow, deny, or escalate path. Evaluation is deterministic.
- No auto-merge. Every policy change needs a human click.
- Evidence is append-only.
- One workflow end to end (refunds and exceptions), by design for the first release.

## Planned extension points

The codebase grows by implementing behind interfaces, not by forking:

- Evidence store: from the local database to hosted storage.
- Precedent provider: from structured lookup to the full provenance graph.
- Reconciliation engine: from the on-demand local loop to a continuous controller.
- Auth provider: from a bearer token to single sign-on and roles.
- Runtime adapters: from a reference stub to platform integrations.
- Export formatter: from raw JSONL to formatted compliance exports.
