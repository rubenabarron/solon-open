# Product principles

Status: living | Date: 2026-09-30
Source: curated from the internal product requirements document (August 2026).

## What Solon is

Solon is the operational policy-as-code layer for agent-driven business workflows. It
starts with one workflow: support refunds and exceptions.

Three primitives:

1. Policy files: versioned YAML in Git that encode business decision logic.
2. Decision evidence: for every consequential decision, a structured, immutable record of
   the context, the matched rule, the outcome, and any human override.
3. Precedent reconciliation: when a human overrides a decision, Solon extracts the implied
   policy change and proposes a pull request. Repeated overrides compound into better
   policy.

## The bet

Agents can increasingly be run securely, observed, and audited. What remains open is
business decision correctness: whether the decision was right, and whether the
organization learned from the last time a person disagreed. Solon is built around the loop
that closes it: override, cluster, propose, human merge.

## Principles

1. Durable policy over ephemeral corrections. An override is a signal, not a fix.
2. A human merges. Solon never merges its own proposals; the human click is the product,
   not a limitation.
3. Deterministic where it matters. The allow, deny, or escalate evaluation is
   deterministic; no model sits in that path.
4. Evidence is append-only, and redaction happens before storage, driven by the policy
   file.
5. Policy is code. Changes arrive through Git history, reviewable as diffs.
6. No lock-in. Policy files, evidence, and history are exportable and portable.

## What Solon is not

- Not a runtime control plane.
- Not an agent security or trust-boundary product.
- Not a model observability or evaluation tool.
- Not an infrastructure policy engine.
- Not a compliance document platform.
- Not a workflow builder or an agent framework.

Solon consumes context and evidence from the surrounding stack; it replaces none of it.

## Scope of the first release

One governed workflow end to end (refunds and exceptions): policy files, the `@governed`
SDK, decision evidence, the escalation and review surface, reconciliation to pull
requests, and basic precedent retrieval. Multi-team and hosted capabilities are
deliberately out of the first release.
