You are a senior forensic risk analyst and investigative data scientist specializing in systemic corruption network modeling, cascade analysis, and evidence-based policy briefing.

Given the following ConPattern proof-of-concept report, produce an enhanced version that strengthens it across every dimension below. Do not remove any existing content. Extend, correct, and deepen it.

---

## EVIDENCE QUALITY

**Event Ledger Hardening**
- For every event in the evidence table, add:
  - Exact case number, docket ID, or public record identifier
  - Jurisdiction (federal / state / civil / congressional)
  - Date of original offense, date of accountability outcome, and current legal status
  - Confidence tier: [HIGH] corroborated primary source / [MEDIUM] partial corroboration / [LOW] single-source or synthesized
- Flag every $0 harm estimate with an explicit explanation of why it is zero (e.g., no quantifiable financial loss, harm is non-monetary, or not yet assessed)
- Flag every round-number harm estimate (e.g., $280,000, $32,000,000) with [ESTIMATE BASIS NEEDED] and note the methodology used to derive it
- Identify any events where harm may double-count losses already captured in another row and add a [POTENTIAL OVERLAP] note

**Source Traceability**
- Replace vague source notes like "Congressional and public investigative record synthesis" with specific named sources, report titles, and dates
- Every harm figure must trace to either a court judgment, regulatory finding, government estimate, or clearly labeled model inference marked [MODELED]
- Add a source confidence matrix at the end of the evidence section rating each citation on: specificity, recency, independence, and corroboration

---

## MODEL ASSUMPTION DEFENSE

**Coefficient Justification**
- The 0.35 compounding rate in M(t) = (1 + 0.35)^t is currently asserted without basis. Add a dedicated subsection that:
  - Cites the empirical or theoretical foundation for this specific coefficient
  - States the valid range and conditions under which it holds
  - Identifies what happens to outputs if the rate is 0.20 or 0.50 instead
  - Marks it [CALIBRATION REQUIRED] if no empirical basis exists

- The cascade depth of 3 is unexplained. Add justification covering:
  - Why 3 hops and not 2 or 4
  - What evidence or network structure supports this choice
  - How outputs change at depth 2 and depth 4

- The SRS weighting (0.4 R0 + 0.35 CC + 0.25 CHI_norm) is unexplained. Add:
  - Rationale for each weight
  - Sensitivity test showing SRS range if weights shift by ±0.10
  - Whether weights were empirically derived or expert-assigned

**R0 Decomposition**
- R0 = β/γ is stated but β and γ are never defined numerically. Add:
  - Exact values of β (spread rate) and γ (accountability removal rate) for this run
  - How each was derived from the evidence package
  - Why R0 = 75.5107 is plausible given the input data

---

## ENABLED ACTOR COMPLETENESS

**Full Actor Table**
- The enabled actor table is truncated at 15 of 44. Provide the complete table or explain the selection criteria for the 15 shown
- For each actor shown, add:
  - The specific relationship type connecting them to the root entity
  - The source document that establishes that relationship
  - Whether their propagated impunity figure is higher or lower than expected given their graph distance
- Flag any actor whose inclusion appears driven by organizational name concatenation artifacts (e.g., "Trump Organization LLC Michael Flynn") rather than a documented direct relationship

**Propagation Logic**
- Explain why all depth-1 actors share the same propagated impunity value (6.0678). Is this expected? Does it reflect a uniform assumption or a modeling artifact?
- Add a column showing each actor's pre-propagation baseline for comparison

---

## MATHEMATICAL TRANSPARENCY

**Worked Examples**
- Add a complete worked numerical example for each formula, not just M(t):
  - Show R0 = β/γ with actual β and γ values plugged in
  - Show CHI = H₀ × Σ(Nₖ × rᵏ) with actual Nₖ and r values for each depth k
  - Show SRS = min(1, 0.4×(R0/5) + 0.35×CC + 0.25×CHI_norm) with numbers
- Add a sensitivity table showing how SRS changes across a plausible input range

**Boundary Condition Documentation**
- What happens when unpunished event count is 0? Show M(t) = 1.0 explicitly
- What happens when R0 < 1? Show what that would look like in this network
- What is CHI_norm normalized against? State the normalization ceiling explicitly

---

## NETWORK AND GRAPH QUALITY

**Graph Construction Transparency**
- Add a section describing how the knowledge graph was built:
  - What entity types are nodes?
  - What relationship types are edges?
  - What weight scheme is used?
  - How were relationships extracted from the 8 source documents?
- Explain how eigenvector centrality = 1.0000 for the root. Is this because the root is the highest-centrality node in this graph, or because centrality is normalized to the root by design?

**Graph Limitations**
- Add an explicit graph limitation section covering:
  - What relationships are NOT modeled (e.g., informal pressure, non-documented connections)
  - How graph coverage affects centrality and R0 reliability
  - What additional data would materially change the topology

---

## HARM ESTIMATE RIGOR

- Add a harm classification column to the event table:
  - [DIRECT FINANCIAL] - court-ordered or regulatory-assessed loss
  - [ESTIMATED ECONOMIC] - derived from external economic analysis
  - [OPERATIONAL COST] - government or institutional cost estimate
  - [NON-QUANTIFIED] - documented but not yet monetized
- For the Deutsche Bank $630M figure: clarify whether this is the full settlement, the US-attributed portion, or a modeled proxy
- For the Ukraine aid $391M: clarify whether this is the withheld aid amount or a downstream harm estimate
- For the Mueller obstruction $32M: cite the specific cost component this represents (investigation cost? estimated downstream harm?)

---

## SCENARIO COVERAGE

**Add Missing Scenarios**
- Partial-accountability scenario: 4 of 8 unpunished events recoded to conviction
  - Show resulting M(t), R0, and SRS
- Sector-specific scenario: weight harm by domain (financial crimes vs democratic process vs national security)
  - Show how CHI shifts under domain weighting
- Time-decay scenario: apply a decay factor to older events (pre-2018)
  - Show whether staleness materially affects the composite score

---

## STRUCTURAL AND COMMUNICATION IMPROVEMENTS

**Non-Adjudication Reinforcement**
- Add a [MODEL BOUNDARY] callout box at the top of every major section reminding readers this is a triage tool, not a legal finding
- Add a "What this score cannot tell you" section covering:
  - Intent
  - Causation
  - Criminal liability
  - Comparative guilt across actors

**Appendix Consolidation**
- The current report has 26 appendices (A through Z). Audit each one and:
  - Merge appendices that cover the same theme
  - Remove appendices that restate content already in the main body without adding new information
  - Add a one-line purpose statement to each retained appendix so readers know whether to read it

**Readability**
- The current document repeats the same governance caveats in at least 8 separate locations. Consolidate into one canonical caveat block and cross-reference it rather than duplicating
- Add a document-level table of contents with section anchors

---

## OUTPUT FORMAT REQUIREMENTS

- Return the full enhanced report in markdown
- Add a changelog section at the very top listing every material change made and the reason for each change
- Mark every new addition with a [NEW] tag on first appearance
- Mark every assumption that lacks empirical grounding with [UNVERIFIED ASSUMPTION]
- Mark every harm estimate lacking a primary source with [UNVERIFIED ESTIMATE]
- Do not remove any existing section - only extend or correct
- Preserve all mermaid diagrams and add at least two new ones:
  - One showing the full 44-actor network structure schematically
  - One showing sensitivity of SRS to coefficient variation
