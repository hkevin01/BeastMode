# Agent Modes Catalog

This document catalogs all available agent modes in the BeastMode repository. Each mode represents a specialized configuration for a distinct problem domain or workflow.

## Directory Structure

```
modes/
├── automated-reasoning/           # General-purpose autonomous problem solving
│   ├── primary-solver.agent.md   # Modern VS Code agent format
│   ├── profile.md                # Profile content/configuration
│   └── legacy-format.chatmode.md # Legacy format for backward compatibility
│
├── systemic-risk-analysis/        # Quantitative analysis of complex systems
│   └── accountability-analyst.agent.md  # Corruption modeling & accountability analysis
│
├── documentation-integrity/       # Technical documentation auditing
│   └── code-truth-auditor.agent.md     # Code-traceable documentation verification
│
└── product-documentation/         # Product-specific documentation review
    └── README.md                  # Placeholder for product-specific agents
```

---

## Agent Modes Specifications

### 1. Automated Reasoning
**Location:** `/modes/automated-reasoning/`

**Purpose:** Autonomous multi-step problem solving through research, codebase investigation, and iterative development.

**Primary File:** `primary-solver.agent.md`

**Audience:** Developers needing autonomous assistance with complex coding problems.

**Key Capabilities:**
- Extensive internet research (Google-first with DuckDuckGo fallback)
- Codebase exploration and analysis
- Iterative solution implementation and testing
- Edge case handling and validation

**Tools Available:**
- agent, browser, changes, codebase, edit, editFiles, execute, extensions, fetch, findTestFiles
- githubRepo, githubTextSearch, new, problems, read, runInTerminal, runNotebooks
- runTasks, runTests, search, searchResults, selection, terminalLastCommand, terminalSelection
- testFailure, todos, usages, vscode/askQuestions, vscodeAPI, web

**Format Variants:**
- `primary-solver.agent.md` - Modern VS Code agent format (recommended)
- `profile.md` - Configuration profile content
- `legacy-format.chatmode.md` - Legacy `.chatmode.md` format

---

### 2. Systemic Risk Analysis
**Location:** `/modes/systemic-risk-analysis/`

**Purpose:** Quantitative analysis of systemic corruption, accountability cascades, and evidence-based risk modeling.

**File:** `accountability-analyst.agent.md`

**Target Audience:** Policy researchers, risk analysts, accountability advocates.

**Key Requirements:**
- Event-level evidence with citations (case numbers, dockets, public record IDs)
- Confidence tiers (High/Medium/Low) for all harm estimates
- Model assumption justification with sensitivity analysis
- Scenario completeness (baseline, partial intervention, delayed, full accountability)
- Analytical gap identification and evidence chain weakness assessment
- Societal impact mapping with reversibility analysis

**Output Format:**
- Full enhanced markdown report
- Changelog section documenting all material additions
- Flag every inference beyond evidence with [MODELED INFERENCE]
- Preserve non-adjudication framing throughout
- Citation format: [Source type | Institution | Date]

**Tools Available:**
- read, search, codebase, web, fetch

---

### 3. Documentation Integrity
**Location:** `/modes/documentation-integrity/`

**Purpose:** Audit and rewrite documentation using code-traceable references and implementation-grounded analysis.

**File:** `code-truth-auditor.agent.md`

**Target Audience:** Documentation teams, technical writers, product engineers requiring code-synchronized documentation.

**Core Rules (8 Total):**

**RULE 1: Replace Intention with Mechanism**
- Replace "what it does" with specific function names, file paths, data structures
- Show actual formula outputs and implementation details

**RULE 2: Every Algorithm Must Show Actual Numbers**
- Include function signatures, pseudocode, or concrete worked examples
- Show real output values produced
- Document which file/module contains the logic

**RULE 3: End-to-End Traceability**
- Add "How It's Actually Built" section
- Walk through complete execution path for example queries
- Show data transformations at each step

**RULE 4: Separate Real from Example Content**
- Create content-origin tables for each major output field
- Distinguish computed vs static vs hardcoded content
- Mark origin-unknown fields

**RULE 5: Developer Extension Path Must Be Explicit**
- Step-by-step technical guide with real file locations
- Required exports and data structures
- Fallback behavior documentation
- Specific code change instructions

**RULE 6: AI Layer Must Be Honestly Scoped**
- Document actual system prompts
- Specify deterministic fallback behavior
- Note whether fallback is meaningful or cosmetic

**RULE 7: Redundancy Audit**
- Identify duplicated or contradictory information
- Flag conflicts across sections
- Provide single canonical descriptions

**RULE 8: Integration Specifics (No Abstraction)**
- Real API endpoints and SDK package names
- Authentication methods and specific fields mapped
- Fallback behavior for unavailable services
- Request/response format with examples
- Caching policy and duration

**Output Format:**
- Changelog at top listing all additions and corrections
- Gap flags: [PLACEHOLDER], [AI DELEGATED], [HARDCODED], [ARCHITECTURE GAP], [INTEGRATION GAP], [REDUNDANCY], [ORIGIN UNKNOWN], [FALLBACK IS COSMETIC]
- Content-origin tables for major data structures
- Step-by-step extension guides with exact file locations
- All third-party specifics named explicitly
- Confidence levels where applicable

**Tools Available:**
- read, search, codebase, usages

---

### 4. Product Documentation
**Location:** `/modes/product-documentation/`

**Purpose:** Specialized agent modes for product-specific technical documentation review.

**Current Status:** Placeholder directory ready for product-specific agents.

**Expected Future Agents:**
- Week Trip Planner Product Engineer Documenter
- Additional domain-specific agents as needed

**File Naming Convention:** `[product-name]-documenter.agent.md`

---

## How to Use These Modes

### In VS Code

1. **Via Settings:** Configure `chat.agentFilesLocations` in `.vscode/settings.json`:
   ```json
   {
     "chat.agentFilesLocations": ["/home/kevin/Projects/BeastMode"]
   }
   ```

2. **In Chat:** Reference the agent by name:
   - "Use Automated Reasoning mode"
   - "Switch to Systemic Risk Analysis"
   - "Load Documentation Integrity auditor"

### Creating New Modes

1. Create a new folder under `/modes/[mode-name]/`
2. Create agent file: `[specific-name].agent.md`
3. Include YAML frontmatter:
   ```yaml
   ---
   name: Agent Display Name
   description: Brief description of purpose and specialization
   argument-hint: What kind of input this agent expects
   tools: [list of tools]
   ---
   ```
4. Add detailed instructions and rules
5. Document in this catalog

---

## Discovery and Registration

All agents in this repository are automatically discoverable via:
- **Local Discovery:** `.agent.md` files in the BeastMode folder
- **Remote Discovery:** Via `chat.agentFilesLocations` setting in any VS Code project

No manual registration required - place the file in the correct folder and it becomes available.

---

## Maintenance Notes

- Keep profile files (`profile.md`) synchronized with agent files
- Update this catalog when adding new modes
- Legacy format files (`.chatmode.md`) maintained for backward compatibility only
- Test each agent mode with sample inputs before deployment

---

**Last Updated:** May 15, 2026
**Version:** 1.0
