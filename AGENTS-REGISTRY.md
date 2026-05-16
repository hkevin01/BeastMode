---
title: BeastMode Agents Registry
description: Quick reference guide for all 12 custom GitHub Copilot agents
version: 1.0
lastUpdated: 2026-05-15
totalAgents: 12
---

# BeastMode Agents Registry

Quick reference for all 12 specialized GitHub Copilot agents.

## Agent Summary Table

| # | Agent Name | Specialization | File | Use When |
|---|-----------|-----------------|------|----------|
| 1 | **Automated Reasoning** | General problem solving | `primary-solver.agent.md` | Complex multi-step problems |
| 2 | **Code Analysis** | Multi-dimensional code review | `comprehensive-reviewer.agent.md` | Need comprehensive code review |
| 3 | **Code Commenting** | Documentation & comments (NASA-style) | `commenting-specialist.agent.md` | Adding strategic comments |
| 4 | **Performance Optimization** | Efficiency & scalability | `performance-optimizer.agent.md` | Optimizing for scale/speed |
| 5 | **Legacy Modernization** | Zero-downtime system updates | `legacy-modernizer.agent.md` | Modernizing old systems |
| 6 | **Test Automation** | Test strategy & architecture | `test-specialist.agent.md` | Planning test coverage |
| 7 | **Architecture Design** | System architecture & microservices | `architect.agent.md` | High-level system design |
| 8 | **Systemic Risk Analysis** | Quantitative risk assessment | `conpattern-accountability.agent.md` | Analyzing complex risks |
| 9 | **Documentation Integrity** | Code-traceable doc auditing | `readme-code-truth.agent.md` | Auditing documentation |
| 10 | **Forensic Analysis** | Security investigation & root cause | `code-forensics-specialist.agent.md` | Security incidents/bugs |
| 11 | **README Documentation** | README creation & enhancement | `readme-enhancer.agent.md` | Creating project READMEs |
| 12 | **Product Documentation** | User/developer/admin guides | `product-documenter.agent.md` | Creating comprehensive docs |

---

## Agents by Use Case

### Code Quality
- **Code Analysis** - Comprehensive code review
- **Code Commenting** - Adding documentation
- **Test Automation** - Test strategy planning

### Performance & Optimization  
- **Performance Optimization** - Speed and scalability
- **Architecture Design** - System efficiency design

### System Modernization
- **Legacy Modernization** - Updating old systems
- **Architecture Design** - Restructuring systems

### Documentation
- **README Documentation** - Project READMEs
- **Product Documentation** - User/admin guides
- **Documentation Integrity** - Doc auditing
- **Code Commenting** - Code documentation

### Analysis & Investigation
- **Forensic Analysis** - Security and bugs
- **Systemic Risk Analysis** - Risk quantification
- **Code Analysis** - Code quality analysis

### General Purpose
- **Automated Reasoning** - Complex problem solving

---

## Agents by Domain

### Development (7 agents)
```
@Code Analysis              - Review code quality/security
@Code Commenting           - Add strategic comments
@Performance Optimization  - Optimize algorithms/databases
@Test Automation           - Design test strategy
@Architecture Design       - Plan system architecture
@Legacy Modernization      - Modernize existing systems
@Forensic Analysis         - Investigate bugs/security
```

### Documentation (4 agents)
```
@README Documentation      - Create project READMEs
@Product Documentation     - Create user/dev guides
@Documentation Integrity   - Audit documentation
@Code Commenting          - Add code comments
```

### Analysis (3 agents)
```
@Code Analysis            - Analyze code quality
@Systemic Risk Analysis   - Assess complex risks
@Forensic Analysis        - Investigate issues
```

### General Purpose (1 agent)
```
@Automated Reasoning      - General problem solving
```

---

## Quick Start Guide

### Setup (One Time)
```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --project .
# Reload VS Code (Cmd+Shift+P > Developer: Reload Window)
```

### Using Agents
```
@AgentName Your request
```

### Examples
```
@Code Analysis Review this function for security issues
@Performance Optimization Optimize this query for 10k users
@README Documentation Create a README for my project
@Test Automation Help me plan my test strategy
```

---

## Agents Details

### 1. Automated Reasoning
**Location**: `modes/automated-reasoning/`  
**In Chat**: `@Automated Reasoning`  
**Best For**: Complex, multi-step problems requiring research and analysis

**Capabilities:**
- Internet research (Google-first, DuckDuckGo fallback)
- Codebase exploration
- Iterative solution testing
- Edge case handling
- 10-step workflow for problem solving

---

### 2. Code Analysis
**Location**: `modes/code-analysis/`  
**In Chat**: `@Code Analysis`  
**Best For**: Comprehensive code reviews across multiple dimensions

**Review Dimensions:**
- Code Quality (structure, patterns, readability)
- Security (vulnerabilities, validation, auth)
- Performance (complexity, bottlenecks, optimization)
- Best Practices (conventions, frameworks, standards)
- Error Handling (edge cases, exceptions, cleanup)
- Concurrency (thread safety, race conditions)

**Severity Levels**: Critical, High, Medium, Low

---

### 3. Code Commenting
**Location**: `modes/code-commenting/`  
**In Chat**: `@Code Commenting`  
**Best For**: Adding strategic comments and documentation

**Standards:**
- NASA-style safety-critical comments
- File headers with purpose and dependencies
- Function docs with requirements and failure modes
- Logic block explanations
- Error handling documentation
- Performance and security notes

**Supported Languages**: JavaScript, Python, Java, C/C++, Go, Rust

---

### 4. Performance Optimization
**Location**: `modes/performance-optimization/`  
**In Chat**: `@Performance Optimization`  
**Best For**: Analyzing and improving system efficiency

**Analysis Areas:**
- Algorithm complexity (Big O analysis)
- Database optimization (queries, indexes, N+1)
- Memory and resources (leaks, GC, allocation)
- Concurrency (parallelization, contention)
- Caching (hit rates, staleness, invalidation)
- Scalability (horizontal/vertical, sharding)

**Deliverables:**
- Bottleneck analysis report
- Optimization catalog with ROI
- Benchmarking plan
- 10x scalability roadmap

---

### 5. Legacy Modernization
**Location**: `modes/legacy-modernization/`  
**In Chat**: `@Legacy Modernization`  
**Best For**: Modernizing old systems without downtime

**Migration Patterns:**
- Strangler Fig (gradual, recommended)
- Big Bang Rewrite (complete, risky)
- Component-by-Component (incremental)

**Guarantees:**
- Zero-downtime operations
- Feature flags for gradual rollout
- Full backward compatibility
- Instant rollback capability
- Data integrity assurance

---

### 6. Test Automation
**Location**: `modes/test-automation/`  
**In Chat**: `@Test Automation`  
**Best For**: Test strategy and automation architecture

**Coverage Goals:**
- Unit tests: >70% code
- Overall coverage: >80%
- Critical path: 100% E2E

**Test Pyramid:**
- 70-80% unit tests
- 15-20% integration tests
- 5-10% E2E tests

**Roadmap:**
- Phase 1: Critical path testing (weeks 1-2)
- Phase 2: Unit test expansion (weeks 3-6)
- Phase 3: Integration tests (weeks 7-10)
- Phase 4: Continuous improvement (ongoing)

---

### 7. Architecture Design
**Location**: `modes/architecture-design/`  
**In Chat**: `@Architecture Design`  
**Best For**: High-level system design and microservices

**Design Areas:**
- Current state assessment
- Requirement analysis (functional/non-functional)
- Architectural patterns (monolith, microservices, event-driven)
- Microservices decomposition
- Scalability and reliability
- Technology recommendations

**Analysis Includes:**
- 12-month and 5-year projections
- Failure mode analysis
- Multi-region strategies
- Circuit breakers and resilience

---

### 8. Systemic Risk Analysis
**Location**: `modes/systemic-risk-analysis/`  
**In Chat**: `@Systemic Risk Analysis`  
**Best For**: Quantitative analysis of complex systems

**Capabilities:**
- Risk quantification
- Accountability chain mapping
- Corruption pattern modeling
- Scenario analysis
- Evidence-based assessment

**Confidence Tiers:**
- High: Multiple independent sources
- Medium: Single source with supporting logic
- Low: Logical inference with limited evidence

---

### 9. Documentation Integrity
**Location**: `modes/documentation-integrity/`  
**In Chat**: `@Documentation Integrity`  
**Best For**: Auditing documentation accuracy and completeness

**8 Audit Rules:**
1. All outputs traced to specific code locations
2. Placeholders and AI content explicitly flagged
3. Content-origin tables provided
4. Real vs example content separated
5. Developer extension paths explicit
6. AI layer scope honestly documented
7. Redundancy identified and resolved
8. Integration specifics clear (no abstractions)

**Gap Flags:** Architecture Gap, Integration Gap, Redundancy, Origin Unknown

---

### 10. Forensic Analysis
**Location**: `modes/forensic-analysis/`  
**In Chat**: `@Forensic Analysis`  
**Best For**: Security investigation and root cause analysis

**Investigation Protocol:**
1. Evidence Collection (exact code locations)
2. Trace Execution (call sequences, data flow)
3. Impact Assessment (affected components)
4. Root Cause Analysis (symptoms vs causes)
5. Evidence Timeline (when/why introduced)

**Deliverables:**
- Executive summary by severity
- Detailed findings with evidence
- Component inventory table
- Dependency impact map
- Remediation roadmap
- Test cases for verification

---

### 11. README Documentation
**Location**: `modes/readme-documentation/`  
**In Chat**: `@README Documentation`  
**Best For**: Creating exceptional project READMEs

**16-Section Structure:**
1. Header & Visual (project identity)
2. Table of Contents (navigation)
3. Overview (problem & solution)
4. Features (what it does)
5. Installation (getting it)
6. Quick Start (first 5 minutes)
7. Usage & Examples (how to use)
8. Architecture (how it works)
9. API Reference (detailed interface)
10. Configuration (settings)
11. Development (for contributors)
12. Testing (QA coverage)
13. Roadmap (future direction)
14. Contributing (how to help)
15. License (legal)
16. Acknowledgments (credits)

**Quality Measures:**
- Clear one-liner and visual
- Working code examples
- Multiple installation methods
- Proper markdown formatting

---

### 12. Product Documentation
**Location**: `modes/product-documentation/`  
**In Chat**: `@Product Documentation`  
**Best For**: Comprehensive product documentation

**Documentation Types:**
- User-facing (getting started, guides, FAQ)
- Developer-facing (architecture, APIs, SDKs)
- Administrator-facing (installation, security, maintenance)

**Deliverables:**
- Getting Started Guide (5-10 pages)
- User Manual (20-50 pages)
- API Reference (5-20 per endpoint)
- Developer Guide (10-30 pages)
- Administrator Guide (10-20 pages)
- FAQ and Troubleshooting (10-20 pages)

---

## Commands

### Setup
```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --project /path/to/project
```

### List Agents
```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --list
```

### Verify Setup
```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --verify
```

### Show Status
```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --status
```

### Help
```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --help
```

---

## Documentation Files

- **GITHUB-COPILOT-SETUP.md** - Complete setup guide
- **AGENT_CATALOG.md** - Detailed agent specifications
- **AGENTS-REGISTRY.md** - This file (quick reference)
- **PROMPT_SOURCE_TRACKER.md** - Where agents came from
- **README.md** - Project overview
- **CONTRIBUTING.md** - Contributing guidelines

---

**Location**: `/home/kevin/Projects/BeastMode`  
**Total Agents**: 12  
**Status**: Production Ready  
**Last Updated**: May 15, 2026
