# Documentation Integrity Mode

## Overview

The Documentation Integrity mode is specialized for auditing and rewriting technical documentation using code-traceable references and implementation-grounded analysis. It ensures documentation stays synchronized with actual code behavior and clearly identifies gaps or unimplemented features.

## Files

- **`code-truth-auditor.agent.md`** - Primary auditing agent with 8-rule specification

## Target Audience

- Technical writers and documentation teams
- Product engineers requiring honest documentation
- Open-source maintainers
- Developers contributing to unfamiliar codebases
- Security auditors reviewing implementation gaps

## The 8 Rules

### RULE 1: Replace Intention with Mechanism
Transform prose descriptions into code-grounded explanations with specific:
- Function names and file paths
- Data structures and type signatures
- Actual formula outputs
- Implementation-specific details

### RULE 2: Every Algorithm Shows Actual Numbers
Required for each formula:
- Function signature or pseudocode
- Complete worked example with real inputs
- Actual output value produced
- Specific file location

### RULE 3: End-to-End Traceability
Required sections:
- "How a Trip Is Actually Built" (or domain equivalent)
- Complete execution path walkthrough
- Data transformation at each step
- All intermediate values documented

### RULE 4: Separate Real from Example Content
Deliverable: Content-origin table
- Every output field listed
- Origin (formula, static, template, lookup)
- File location
- Computed vs static vs hardcoded classification
- [ORIGIN UNKNOWN] flagging where needed

### RULE 5: Developer Extension Path (Explicit)

## Research-First Workflow

When auditing documentation:

1. **Research Phase**
   - Query Google or DuckDuckGo for documentation best practices in your domain
   - Gather reference implementations and architecture patterns
   - Review compliance and technical accuracy standards

2. **Code Analysis Phase**
   - Trace complete execution paths through codebase
   - Identify all data transformations and side effects
   - Extract actual behavior vs documented behavior

3. **Documentation Audit Phase**
   - Compare documentation against actual implementation
   - Identify gaps, omissions, and inaccuracies
   - Document evidence locations with file paths and line numbers

4. **Correction Phase**
   - Rewrite sections to match implementation
   - Add missing technical details with examples
   - Flag undocumented features or behaviors
Required: Step-by-step technical guide including:
- Exact file locations for creation/modification
- Required data structure exports and types
- Fallback behavior on missing fields
- Specific code changes (not generic instructions)
- Failure modes if steps are skipped
- Architecture gaps marked [ARCHITECTURE GAP]

### RULE 6: AI Layer (Honestly Scoped)
For each AI endpoint, document:
- Actual system prompt (or summarized instruction)
- Deterministic fallback behavior (specific values/structures)
- User indication of fallback mode active/inactive
- Meaningful vs cosmetic fallback assessment
- Mark [FALLBACK IS COSMETIC] if real value requires live AI

### RULE 7: Redundancy Audit
Identify and resolve:
- Duplicated descriptions across sections
- Conflicting explanations for same behavior
- Inconsistent terminology
- Canonical version for all variants
- [REDUNDANCY] flagging with resolution

### RULE 8: Integration Specifics (No Abstraction)
For all third-party integrations:
- Actual API endpoint URLs
- SDK package names and versions
- Authentication method specifics
- Field mapping to output structures
- Unavailability fallback behavior
- Caching policy and TTL
- Request/response JSON schema or examples
- [INTEGRATION GAP] marking for unimplemented specs

## Output Format

**Required sections:**
1. **Changelog** - All additions, corrections, and gaps identified
2. **Gap flags** - [PLACEHOLDER], [AI DELEGATED], [HARDCODED], [ARCHITECTURE GAP], [INTEGRATION GAP], [REDUNDANCY], [ORIGIN UNKNOWN], [FALLBACK IS COSMETIC], [SENSITIVITY RISK], [UNVERIFIED]
3. **Content-origin tables** - One per major data structure
4. **Extension guides** - Step-by-step with exact file locations and code samples
5. **Third-party specifics** - All explicitly named, no generic descriptions
6. **Confidence levels** - Where applicable

## Available Tools

read, search, codebase, usages

## Use Cases

- README auditing for accuracy
- Architecture documentation verification
- API documentation synchronization
- Integration guide creation with real specifications
- Developer onboarding documentation
- Code comment clarity assessment
- Gap documentation and planning
- Open-source quality assurance

## Philosophy

"This transparency is more valuable than hiding the gaps."

Honest documentation about what's implemented, what's placeheld, and what's missing is superior to aspirational documentation that diverges from reality.