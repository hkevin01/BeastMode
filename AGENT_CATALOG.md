---
title: BeastMode Agent Modes Catalog
description: Complete catalog of all 11 specialized agent modes in the BeastMode repository
lastUpdated: "2026-05-15"
modeCount: 11
---

# Agent Modes Catalog

This document catalogs all available agent modes in the BeastMode repository. Each mode represents a specialized configuration for a distinct problem domain or workflow.

**Total Modes:** 11 | **Status:** Production-ready

---

## Directory Structure

```
modes/
├── automated-reasoning/           # General-purpose autonomous problem solving
│   ├── primary-solver.agent.md   # Modern VS Code agent format
│   ├── beastmode_kevin.agent.md  # Primary Beast Mode agent
│   ├── beastmode_kevin.md        # Profile content variant
│   ├── profile.md                # Profile configuration
│   ├── legacy-format.chatmode.md # Legacy format for backward compatibility
│   └── README.md
│
├── code-analysis/                 # Multi-dimensional code review
│   ├── comprehensive-reviewer.agent.md
│   └── README.md
│
├── performance-optimization/      # Efficiency, scalability, bottleneck analysis
│   ├── performance-optimizer.agent.md
│   └── README.md
│
├── legacy-modernization/          # Zero-downtime legacy system modernization
│   ├── legacy-modernizer.agent.md
│   └── README.md
│
├── test-automation/               # Test strategy and automation architecture
│   ├── test-specialist.agent.md
│   └── README.md
│
├── architecture-design/           # System architecture and microservices
│   ├── architect.agent.md
│   └── README.md
│
├── systemic-risk-analysis/        # Quantitative analysis of complex systems
│   ├── conpattern-accountability.agent.md
│   └── README.md
│
├── documentation-integrity/       # Technical documentation auditing
│   ├── readme-code-truth.agent.md
│   └── README.md
│
├── forensic-analysis/             # Detailed investigation and evidence-based analysis
│   ├── code-forensics-specialist.agent.md
│   └── README.md
│
├── readme-documentation/          # README creation and enhancement
│   ├── readme-enhancer.agent.md
│   └── README.md
│
└── product-documentation/         # Product-specific documentation review
    └── README.md
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

**Format Variants:**
- `primary-solver.agent.md` - Modern VS Code agent format (recommended)
- `profile.md` - Configuration profile content
- `legacy-format.chatmode.md` - Legacy `.chatmode.md` format

**Tools Available:**
- agent, browser, changes, codebase, edit, editFiles, execute, extensions, fetch, findTestFiles
- githubRepo, githubTextSearch, new, problems, read, runInTerminal, runNotebooks
- runTasks, runTests, search, searchResults, selection, terminalLastCommand, terminalSelection
- testFailure, todos, usages, vscode/askQuestions, vscodeAPI, web

---

### 2. Code Analysis
**Location:** `/modes/code-analysis/`

**Purpose:** Comprehensive multi-dimensional code reviews covering quality, security, performance, best practices, error handling, and concurrency.

**Primary File:** `comprehensive-reviewer.agent.md`

**Audience:** Code reviewers, pull request reviewers, code quality advocates, senior engineers.

**Review Dimensions:**
- **Code Quality**: Structure, patterns, readability, maintainability
- **Security**: Vulnerabilities, input validation, authentication, authorization
- **Performance**: Algorithm complexity, bottlenecks, optimization opportunities
- **Best Practices**: Language conventions, framework patterns, standards compliance
- **Error Handling**: Edge cases, exception management, resource cleanup
- **Concurrency**: Thread safety, race conditions, deadlocks

**Severity Levels:** Critical, High, Medium, Low

**Deliverables:**
- Executive summary of key findings
- Line-by-line feedback with context
- Refactored code examples
- Priority remediation roadmap

**Tools Available:** read, search, codebase, web

---

### 3. Performance Optimization
**Location:** `/modes/performance-optimization/`

**Purpose:** Analyze code and systems for efficiency, scalability, and bottleneck identification with concrete optimization recommendations.

**Primary File:** `performance-optimizer.agent.md`

**Audience:** Performance engineers, database administrators, DevOps, infrastructure specialists, backend engineers.

**Optimization Dimensions:**
- Algorithm complexity (Big O analysis)
- Database optimization (queries, indexes, N+1 problems)
- Memory & resources (leaks, GC pressure, allocation)
- Concurrency (parallelization, thread contention, async)
- Caching (hit rates, staleness, invalidation)
- Scalability (horizontal/vertical, sharding, load distribution)

**Analysis Includes:**
- Current performance baseline
- Bottleneck identification and ranking by impact
- Optimization recommendations ranked by ROI
- Scalability roadmap for 10x growth
- Benchmarking and regression detection

**Deliverables:**
- Bottleneck analysis report
- Optimization catalog with effort/benefit analysis
- Benchmarking plan with baselines
- Scalability roadmap and growth projections

**Tools Available:** read, search, codebase, web, fetch

---

### 4. Legacy Modernization
**Location:** `/modes/legacy-modernization/`

**Purpose:** Assess and incrementally modernize outdated codebases while maintaining zero-downtime operations and full backward compatibility.

**Primary File:** `legacy-modernizer.agent.md`

**Audience:** Modernization project leads, architecture decision makers, database migration specialists, DevOps, technical program managers.

**Modernization Dimensions:**
- Legacy assessment (technology audit, security review, performance)
- Business logic documentation (preserving tribal knowledge)
- Modernization strategy (technology stack, architecture approach)
- Implementation roadmap (phased, zero-downtime)
- Data migration (without service interruption)
- Risk mitigation (failure modes, rollback plans)

**Migration Patterns:**
- Strangler Fig (gradual replacement, recommended)
- Big Bang Rewrite (complete rewrite, higher risk)
- Component-by-Component (incremental replacement)

**Zero-Downtime Guarantee:**
- Production availability throughout migration
- Feature flags for gradual rollout
- Full backward compatibility
- Instant rollback capability
- Data integrity assurance

**Deliverables:**
- Legacy assessment report
- Modernization architecture design
- Detailed 6-phase migration roadmap
- Technical implementation guides
- Failure mode analysis
- Knowledge preservation documentation

**Tools Available:** read, search, codebase, usages, changes, web, fetch

---

### 5. Test Automation
**Location:** `/modes/test-automation/`

**Purpose:** Design comprehensive testing strategies with coverage planning, automation architecture, and CI/CD integration.

**Primary File:** `test-specialist.agent.md`

**Audience:** QA engineers, test automation specialists, development leads, DevOps, quality assurance managers, team leads.

**Test Strategy Dimensions:**
- Coverage analysis and gap identification
- Test pyramid (unit 70-80%, integration 15-20%, E2E 5-10%)
- Test types (unit, integration, E2E, performance, security, smoke)
- Automation framework selection and organization
- CI/CD integration and regression detection

**Coverage Goals:**
- Unit tests: >70% application code
- Overall test suite: >80% code coverage
- Critical path: 100% E2E coverage
- Performance: Baseline and regression detection
- Security: Vulnerability scanning included

**Four-Phase Roadmap:**
1. Critical Path Testing (weeks 1-2)
2. Unit Test Expansion (weeks 3-6)
3. Integration Tests (weeks 7-10)
4. Continuous Improvement (ongoing)

**Deliverables:**
- Test strategy document
- Test plan by component
- Implementation roadmap
- Test case catalog
- CI/CD integration guide
- Automation best practices guide

**Tools Available:** read, search, codebase, runTests, web, fetch

---

### 6. Architecture & Microservices Design
**Location:** `/modes/architecture-design/`

**Purpose:** Specialize in system architecture, high-level design, microservices decomposition, and scalability planning.

**Primary File:** `architect.agent.md`

**Audience:** Solutions architects, system architects, technical leads, infrastructure/DevOps architects, microservices specialists, CTO/VP Engineering.

**Architecture Dimensions:**
- Current state assessment (components, dependencies, bottlenecks)
- Requirements analysis (functional and non-functional)
- Architectural patterns (monolith, microservices, event-driven, CQRS)
- Microservices decomposition (service boundaries, data ownership)
- Scalability design (horizontal/vertical strategies)
- Reliability design (HA, disaster recovery, fault isolation)

**Scalability Analysis:**
- Current throughput and bottleneck identification
- 12-month and 5-year load projections
- Scaling strategies for each constraint
- ROI comparison of different approaches
- Technology recommendations for scale

**Reliability & Resilience:**
- Failure mode analysis
- Detection and recovery strategies
- Multi-region deployment options
- Circuit breakers and graceful degradation
- High-availability design patterns

**Deliverables:**
- Architecture assessment report
- Target architecture design
- Microservices decomposition plan (if applicable)
- Implementation roadmap
- Operational considerations
- Technology stack recommendations

**Tools Available:** read, search, codebase, web, fetch, vscodeAPI

---

### 7. Systemic Risk Analysis
**Location:** `/modes/systemic-risk-analysis/`

**Purpose:** Provide quantitative analysis of complex systems with focus on accountability, corruption patterns, and evidence-based risk assessment.

**Primary File:** `conpattern-accountability.agent.md`

**Audience:** Policy researchers, compliance officers, risk analysts, organizational auditors, research teams.

**Key Capabilities:**
- Corruption pattern modeling with quantitative evidence
- Accountability chain analysis
- Evidence-based risk categorization
- Scenario completeness verification
- Analytical gap identification
- Confidence tier assignment (High/Medium/Low)

**Analysis Requirements:**
- Event-level evidence documentation
- Model assumptions made explicit
- Scenario completeness verification
- All analytical gaps identified
- [MODELED INFERENCE] flagging for inferences beyond evidence

**Confidence Tiers:**
- **High**: Multiple independent evidence sources
- **Medium**: Single evidence source with supporting logic
- **Low**: Logical inference with limited evidence

**Deliverables:**
- Risk quantification report
- Accountability chain mapping
- Corruption pattern analysis
- Scenario analysis with confidence tiers
- Evidence documentation
- Recommendations with risk context

**Tools Available:** read, search, web, fetch, vscodeAPI

---

### 8. Documentation Integrity
**Location:** `/modes/documentation-integrity/`

**Purpose:** Specialize in technical documentation auditing with emphasis on code-traceable documentation and specification accuracy.

**Primary File:** `readme-code-truth.agent.md`

**Audience:** Technical writers, documentation reviewers, architects, senior engineers, quality assurance teams.

**8-Rule Specification:**

**RULE 1:** All outputs traced to specific code locations (file paths, line numbers)

**RULE 2:** Placeholder and delegated work flagged:
- [PLACEHOLDER] - Missing implementation
- [AI DELEGATED] - AI-generated without review
- [HARDCODED] - Configuration not externalized

**RULE 3:** Content-origin tables for major outputs showing sources

**RULE 4:** Separate real from example content clearly

**RULE 5:** Developer extension paths must be explicit with real file locations

**RULE 6:** AI layer scope documented with deterministic fallback behavior

**RULE 7:** Redundancy audit identifying duplicated/contradictory information

**RULE 8:** Integration specifics documented (real APIs, SDKs, auth methods, not abstractions)

**Gap Flags:**
- [ARCHITECTURE GAP] - Design decision needed
- [INTEGRATION GAP] - External system integration unclear
- [REDUNDANCY] - Duplicated information across docs
- [ORIGIN UNKNOWN] - Source cannot be traced

**Deliverables:**
- Complete documentation audit
- Gap identification and flagging
- Compliance assessment against 8 rules
- Remediation recommendations
- Updated documentation with proper tracing

**Tools Available:** read, search, codebase, usages, web

---

### 9. Forensic Analysis
**Location:** `/modes/forensic-analysis/`

**Purpose:** Specialize in detailed investigation and evidence-based analysis for security vulnerabilities, bugs, and root cause analysis.

**Primary File:** `code-forensics-specialist.agent.md`

**Audience:** Security engineers, forensic investigators, incident response teams, architects, senior engineers.

**Investigation Protocol:**
1. **Evidence Collection** - Locate exact code with file paths and line numbers
2. **Trace Execution** - Show complete call sequence and data flow
3. **Impact Assessment** - Identify all affected components and scope
4. **Root Cause Analysis** - Distinguish symptoms from underlying causes
5. **Evidence Timeline** - Document when and why issue was introduced

**Finding Documentation Includes:**
- Severity classification (Critical/High/Medium/Low)
- Exact reproduction steps
- All affected components inventory
- Remediation roadmap with effort estimates
- Test cases for verification

**Confidence Marking:**
- [UNCONFIRMED] - Suspected but not verified
- [REQUIRES TESTING] - Needs test case verification
- [ENVIRONMENTAL] - Specific to certain environments
- [DESIGN ASSUMPTION] - Design choice, not a bug
- [DOCUMENTATION GAP] - Working as intended, undocumented

**Deliverables:**
- Executive summary with top findings by severity
- Detailed findings with evidence sections
- Affected components inventory table
- Dependency map showing cascade impact
- Remediation roadmap and test cases
- References to commits and related issues

**Tools Available:** read, search, codebase, usages, changes, web, fetch

---

### 10. README Documentation
**Location:** `/modes/readme-documentation/`

**Purpose:** Specialize in creating, enhancing, and maintaining exceptional project README files for multiple audiences with clear developer experience focus.

**Primary File:** `readme-enhancer.agent.md`

**Audience:** Project maintainers, documentation specialists, open source contributors, onboarding coordinators.

**16-Section README Structure:**
1. Header & Visual (Project identity)
2. Table of Contents (Navigation)
3. Overview (Problem & solution)
4. Features (What it does)
5. Installation (Getting it)
6. Quick Start (First 5 minutes)
7. Usage & Examples (How to use)
8. Architecture (How it works)
9. API Reference (Detailed interface)
10. Configuration (Settings)
11. Development (For contributors)
12. Testing (Quality assurance)
13. Roadmap (Future direction)
14. Contributing (How to help)
15. License (Legal)
16. Acknowledgments (Credits)

**Quality Standards:**
- Clear one-liner and visual representation
- All sections customized for project type
- Working code examples (copy-paste ready)
- Multiple installation methods
- Proper markdown formatting and links
- Audience-appropriate language

**Audience Test (Time-Based):**
- 10 seconds: "What does this project do?"
- 1 minute: "Do I need it?"
- 2 minutes: "How do I install it?"
- 5 minutes: "How do I use it?"
- 15 minutes: "How do I extend/contribute?"

**Deliverables:**
- Complete, well-structured README.md
- Optional supporting files (CONTRIBUTING, TROUBLESHOOTING, ARCHITECTURE, API_REFERENCE, FAQ)
- Enhancement report (if improving existing README)

**Tools Available:** read, search, codebase, web, fetch, vscodeAPI

---

### 11. Product Documentation
**Location:** `/modes/product-documentation/`

**Purpose:** Specialized agent modes for product-specific technical documentation review and creation.

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
   - "@Automated Reasoning"
   - "@Code Analysis"
   - "@Performance Optimization"
   - "@Legacy Modernization"
   - "@Test Automation"
   - "@Architecture Design"
   - "@Systemic Risk Analysis"
   - "@Documentation Integrity"
   - "@Forensic Analysis"
   - "@README Documentation"

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
5. Create `README.md` documenting the mode
6. Update `AGENT_CATALOG.md` with the new mode specification

---

## Discovery and Registration

All agents in this repository are automatically discoverable via:
- **Local Discovery:** `.agent.md` files in the BeastMode modes/ folders
- **VS Code Discovery:** Via `chat.agentFilesLocations` setting in `.vscode/settings.json`
- **Automatic Registration:** Run `setup-beastmode.sh` to configure all projects

No manual registration required - place the agent file in the correct folder structure and it becomes available.

---

## Mode Selection Guide

### For Code Quality Tasks
- **Code Analysis** - Multi-dimensional code reviews
- **Performance Optimization** - Efficiency and scalability
- **Test Automation** - Testing strategy and automation

### For System Design Tasks
- **Architecture Design** - System architecture and microservices
- **Legacy Modernization** - Modernizing existing systems

### For Documentation Tasks
- **README Documentation** - Creating and maintaining READMEs
- **Documentation Integrity** - Auditing documentation accuracy

### For Investigation & Analysis Tasks
- **Forensic Analysis** - Security investigations and root cause analysis
- **Systemic Risk Analysis** - Quantitative analysis of complex systems

### For General Problem Solving
- **Automated Reasoning** - Multi-step autonomous problem solving

---

## Maintenance Notes

- Keep README.md files in each mode synchronized with agent specifications
- Update this catalog when adding new modes or modifying existing ones
- Legacy format files (`.chatmode.md`) maintained for backward compatibility only
- Test each agent mode with sample inputs before deployment
- Review and update mode READMEs annually or when major changes occur

---

**Last Updated:** May 15, 2026  
**Catalog Version:** 2.0  
**Total Modes:** 11  
**Status:** Production Ready
