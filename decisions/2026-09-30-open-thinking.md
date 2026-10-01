# Decision: open the thinking

Date: 2026-09-30 | Status: published | Decision maker: the project owner, via merge

## Context

Solon sells decision governance: evidence, transparency, and a human merge for every
change. Meanwhile our own planning lived in a closed workspace: the product documents,
the session notes, and the reasoning behind each call. For a .org product built on an open
core, that gap started to show.

## Options

1. Stay closed. Keep everything internal and publish only the marketing site.
2. Open raw. Publish internal documents largely as they are, minus redactions.
3. Open the thinking, curated. Publish the layer that serves trust, distribution, and
   standards; keep the tactical layer private; put every publication through a gate and a
   human merge.

## Choice

Option 3. The open layer is product principles, architecture, decisions, and build notes.
The private layer keeps competitive analysis, legal and naming work, pricing, and partner
material. The rules live in PUBLISHING.md; the mechanical checks live in scripts/gate.py.

## Consequences

- The .org story becomes true: the engine's thinking is legible in the open.
- Transparency becomes dogfood: every change here arrives as a pull request a human
  merges, the same rule the product enforces.
- Publishing costs real editing time, budgeted at each session close.
- Two audiences, one repository for now: developers read here; buyers are served
  second-hand, and later by their own layer.
- This repository can move under an organization name later at near zero cost.
