---
title: GitHub Copilot Custom Agents Setup Guide
description: Complete guide to configuring all 12 BeastMode agents in VS Code GitHub Copilot
lastUpdated: 2026-05-15
---

# GitHub Copilot Custom Agents Setup Guide

This guide explains how to enable and use all 12 specialized custom agents in VS Code GitHub Copilot.

## What Are Custom Agents?

Custom agents are specialized Copilot personas optimized for specific tasks. Each BeastMode agent is configured to excel in its domain with tailored instructions, tone, and tool access.

**Total Agents Available**: 12 specialized domains

---

## Quick Setup

### 1. One-Time Configuration

Run this in any VS Code project:

```bash
cd /path/to/your/project
/home/kevin/Projects/BeastMode/setup-beastmode.sh --project .
```

**What it does:**
- Creates `.vscode/` directory if needed
- Adds BeastMode agent paths to VS Code settings
- Enables automatic agent discovery in Copilot Chat

### 2. Reload VS Code

```
Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows/Linux)
> Developer: Reload Window
```

### 3. Start Using Agents

In Copilot Chat, use `@AgentName` syntax:

```
@Automated Reasoning - Multi-step problem solving
@Code Analysis - Code review specialist
@Code Commenting - Documentation expert
@Performance Optimization - Efficiency analyst
@Legacy Modernization - System modernizer
@Test Automation - QA strategist
@Architecture Design - System architect
@Systemic Risk Analysis - Risk analyst
@Documentation Integrity - Doc auditor
@Forensic Analysis - Investigator
@README Documentation - README expert
@Product Documentation - Product documenter
```

---

## All 12 Agents

### 1. Automated Reasoning (BeastMode)
**Agent**: `@Automated Reasoning`  
**File**: `primary-solver.agent.md`  
**Specialization**: General-purpose autonomous problem solving with extensive research

**Use for:**
- Multi-step coding problems
- Complex debugging scenarios
- Research-intensive tasks
- Iterative solution development
- Edge case handling

**Tools**: 26 specialized tools including search, code analysis, terminal execution

---

### 2. Code Analysis  
**Agent**: `@Code Analysis`  
**File**: `comprehensive-reviewer.agent.md`  
**Specialization**: Multi-dimensional code review across 6 dimensions

**Use for:**
- Pull request reviews
- Code quality assessment
- Security vulnerability identification
- Performance bottleneck analysis
- Best practices enforcement

**Review Dimensions:**
- Code Quality
- Security
- Performance  
- Best Practices
- Error Handling
- Concurrency

---

### 3. Code Commenting
**Agent**: `@Code Commenting`  
**File**: `commenting-specialist.agent.md`  
**Specialization**: NASA-style documentation and strategic commenting

**Use for:**
- Adding comprehensive code comments
- Creating API documentation
- Implementing documentation standards
- Preparing code for maintenance
- Safety-critical system documentation

**Styles Supported:**
- JSDoc (JavaScript/TypeScript)
- Docstring (Python)
- Javadoc (Java)
- Doxygen (C/C++)
- GoDoc (Go)
- Rustdoc (Rust)

---

### 4. Performance Optimization
**Agent**: `@Performance Optimization`  
**File**: `performance-optimizer.agent.md`  
**Specialization**: Efficiency analysis and scalability planning

**Use for:**
- Algorithm optimization
- Database query analysis
- Memory leak investigation
- Scalability planning
- Benchmarking and metrics

**Areas:**
- Algorithm complexity (Big O)
- Database optimization
- Memory and resources
- Concurrency improvements
- Caching strategies
- Scalability to 10x growth

---

### 5. Legacy Modernization
**Agent**: `@Legacy Modernization`  
**File**: `legacy-modernizer.agent.md`  
**Specialization**: Zero-downtime system modernization

**Use for:**
- Planning legacy code modernization
- Technology stack upgrades
- Zero-downtime migrations
- Data migration strategies
- Knowledge preservation

**Migration Patterns:**
- Strangler Fig (gradual, recommended)
- Big Bang Rewrite (complete, higher risk)
- Component-by-Component (incremental)

---

### 6. Test Automation
**Agent**: `@Test Automation`  
**File**: `test-specialist.agent.md`  
**Specialization**: Test strategy and automation architecture

**Use for:**
- Test strategy design
- Coverage planning
- CI/CD integration
- Test automation architecture
- Quality metrics

**Coverage Goals:**
- Unit tests: >70%
- Overall coverage: >80%
- Critical path: 100%

---

### 7. Architecture & Microservices
**Agent**: `@Architecture Design`  
**File**: `architect.agent.md`  
**Specialization**: System design and microservices decomposition

**Use for:**
- High-level system design
- Microservices architecture
- Scalability planning
- High-availability design
- Technology recommendations

**Analysis Includes:**
- Current state assessment
- 12-month and 5-year projections
- Failure mode analysis
- Multi-region strategies

---

### 8. Systemic Risk Analysis
**Agent**: `@Systemic Risk Analysis`  
**File**: `conpattern-accountability.agent.md`  
**Specialization**: Quantitative analysis of complex systems

**Use for:**
- Risk quantification
- Accountability analysis
- Corruption pattern modeling
- Evidence-based assessment
- Scenario analysis

**Confidence Tiers:**
- High: Multiple independent sources
- Medium: Single source with logic
- Low: Logical inference

---

### 9. Documentation Integrity
**Agent**: `@Documentation Integrity`  
**File**: `readme-code-truth.agent.md`  
**Specialization**: Code-traceable documentation auditing

**Use for:**
- Documentation audits
- Spec compliance checking
- Gap identification
- Code traceability
- Accuracy verification

**8 Audit Rules:**
1. All outputs traced to code locations
2. Placeholders explicitly flagged
3. Content-origin tables provided
4. Real vs example content separated
5. Extension paths documented
6. AI layer scope honest
7. Redundancy identified
8. Integration specifics clear

---

### 10. Forensic Analysis
**Agent**: `@Forensic Analysis`  
**File**: `code-forensics-specialist.agent.md`  
**Specialization**: Security investigation and root cause analysis

**Use for:**
- Security vulnerability investigation
- Root cause analysis
- Bug forensics
- Impact assessment
- Timeline reconstruction

**Investigation Protocol:**
1. Evidence Collection
2. Trace Execution
3. Impact Assessment
4. Root Cause Analysis
5. Evidence Timeline

---

### 11. README Documentation
**Agent**: `@README Documentation`  
**File**: `readme-enhancer.agent.md`  
**Specialization**: Exceptional README creation and enhancement

**Use for:**
- Creating new project READMEs
- Improving existing documentation
- README structure optimization
- Quick start documentation
- API reference generation

**16-Section Structure:**
1. Header & Visual
2. Table of Contents
3. Overview
4. Features
5. Installation
6. Quick Start
7. Usage & Examples
8. Architecture
9. API Reference
10. Configuration
11. Development
12. Testing
13. Roadmap
14. Contributing
15. License
16. Acknowledgments

---

### 12. Product Documentation
**Agent**: `@Product Documentation`  
**File**: `product-documenter.agent.md`  
**Specialization**: Comprehensive product documentation

**Use for:**
- User guides
- Getting started guides
- API documentation
- Integration guides
- FAQ and troubleshooting

**Documentation Types:**
- User-facing (guides, walkthroughs, FAQ)
- Developer-facing (architecture, APIs, SDKs)
- Administrator-facing (installation, maintenance, security)

---

## Using Agents in Copilot Chat

### Syntax

```
@AgentName Your request here
```

### Examples

**Code Review:**
```
@Code Analysis Please review this function for security issues and performance concerns
```

**Performance Analysis:**
```
@Performance Optimization Analyze this database query and suggest optimizations for 10k concurrent users
```

**Documentation:**
```
@README Documentation Create a comprehensive README for this Node.js library
```

**Testing:**
```
@Test Automation Help me design a test strategy with 80% coverage goal
```

**Architecture:**
```
@Architecture Design Recommend a microservices split for this monolithic application
```

---

## Setup for Multiple Projects

### Batch Setup Script

Setup all projects in a directory:

```bash
#!/bin/bash
for project in ~/Projects/*/; do
    if [ -d "$project/.git" ]; then
        echo "Setting up: $(basename $project)"
        /home/kevin/Projects/BeastMode/setup-beastmode.sh --project "$project"
    fi
done
```

### Verification

Verify agents are discoverable:

```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --verify
```

List available agents:

```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --list
```

---

## Agent Discovery Mechanism

### How It Works

1. **Configuration**: `.vscode/settings.json` contains agent paths
   ```json
   {
     "chat.agentFilesLocations": ["/home/kevin/Projects/BeastMode"]
   }
   ```

2. **Discovery**: VS Code Copilot scans for `.agent.md` files
3. **Registration**: Agents automatically appear in chat
4. **Activation**: Use `@AgentName` to invoke

### File Structure

```
BeastMode/
├── modes/
│   ├── automated-reasoning/
│   │   ├── primary-solver.agent.md
│   │   ├── README.md
│   │   └── ...
│   ├── code-analysis/
│   │   ├── comprehensive-reviewer.agent.md
│   │   └── README.md
│   ├── code-commenting/
│   │   ├── commenting-specialist.agent.md
│   │   └── README.md
│   └── [9 more modes...]
├── AGENT_CATALOG.md
└── setup-beastmode.sh
```

---

## Configuration Persistence

### Preventing Configuration Loss

VS Code sometimes resets custom settings during updates.

**Recovery:**
```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --project /path/to/project
```

**Prevention:**
- Use `.vscode/settings.json` in git for team consistency
- Reference: `.vscode-config-reference.md`

---

## Troubleshooting

### Agents Not Appearing

1. **Check configuration:**
   ```bash
   cat .vscode/settings.json | grep chat.agentFilesLocations
   ```

2. **Verify agent files exist:**
   ```bash
   ls -la /home/kevin/Projects/BeastMode/modes/*/
   ```

3. **Reload VS Code:**
   ```
   Cmd+Shift+P > Developer: Reload Window
   ```

### Agent Loading Slowly

- First load may take 10-30 seconds as VS Code indexes agents
- Subsequent loads are faster
- Check system resources if extremely slow

### Settings Keep Resetting

- This is normal after VS Code updates
- Re-run setup script after major updates
- Use recovery guide: `.vscode-config-reference.md`

---

## Agent Customization

### Modifying an Agent

Edit the `.agent.md` file directly:
```bash
vim /home/kevin/Projects/BeastMode/modes/[mode-name]/[agent-name].agent.md
```

Changes take effect after VS Code reload.

### Creating New Agents

1. Create new mode folder: `modes/my-mode/`
2. Create agent file: `modes/my-mode/my-agent.agent.md`
3. Include YAML frontmatter
4. Reload VS Code

---

## Advanced Usage

### Chaining Agents

Use output from one agent as input to another:

```
@Code Analysis Review this code
[Copy output]

@Performance Optimization Based on this review, optimize for scale
```

### Agent Tools Available

Each agent has access to:
- Code reading and analysis
- Web search and fetching
- Git history and changes
- Terminal execution (some agents)
- VS Code API
- Codebase search and usages

---

## Documentation

- **AGENT_CATALOG.md** - Detailed specifications for all 12 agents
- **PROMPT_SOURCE_TRACKER.md** - Where each agent came from
- **README.md** - BeastMode project overview
- **CONTRIBUTING.md** - How to contribute new agents

---

## Support

### Get Help

List available commands:
```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --help
```

View agent details:
```bash
cat /home/kevin/Projects/BeastMode/AGENT_CATALOG.md
```

### Report Issues

- Check `.vscode-config-reference.md` for troubleshooting
- Review agent capabilities in AGENT_CATALOG.md
- Verify setup with `--verify` flag

---

**Last Updated**: May 15, 2026  
**Total Agents**: 12  
**Setup Time**: ~2 minutes per project  
**Maintenance**: Re-run setup script after VS Code major updates
