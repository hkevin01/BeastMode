# BeastMode Agents - Quick Reference

## Setup (1 Minute)

```bash
cd /your/project
/home/kevin/Projects/BeastMode/setup-beastmode.sh --project .
```

Then reload VS Code: `Cmd+Shift+P > Developer: Reload Window`

---

## Use Agents in Copilot Chat

Click the `@` symbol in Copilot Chat, or type `@AgentName`:

## All 12 Agents

### Development & Code Quality (7 agents)

#### 1. **@Automated Reasoning** - General Problem Solving
For complex multi-step problems, extensive research needed
```
@Automated Reasoning Help me debug this race condition
```

#### 2. **@Code Analysis** - Code Review Specialist  
Multi-dimensional review: quality, security, performance, error handling
```
@Code Analysis Review this function for security vulnerabilities
```

#### 3. **@Code Commenting** - Documentation Expert
NASA-style code comments and documentation
```
@Code Commenting Add comprehensive comments to this function
```

#### 4. **@Performance Optimization** - Efficiency Analyst
Optimize algorithms, databases, memory, scalability
```
@Performance Optimization This query is slow, optimize for 10k users
```

#### 5. **@Legacy Modernization** - System Modernizer
Zero-downtime migration and modernization of old systems
```
@Legacy Modernization How do we upgrade from Node 10 to 18?
```

#### 6. **@Test Automation** - QA Strategist
Test planning, architecture, coverage strategies
```
@Test Automation Help me plan a test strategy with 80% coverage
```

#### 7. **@Architecture Design** - System Architect
High-level system design, microservices, scalability
```
@Architecture Design Should we split this monolith into microservices?
```

---

### Documentation (4 agents)

#### 8. **@README Documentation** - README Expert
Create exceptional project READMEs with 16 sections
```
@README Documentation Create a professional README for my library
```

#### 9. **@Product Documentation** - Product Documenter
User guides, API docs, getting started, administrator guides
```
@Product Documentation Create a user guide for my SaaS product
```

#### 10. **@Documentation Integrity** - Doc Auditor
Audit docs for accuracy, code traceability, completeness
```
@Documentation Integrity Is our API documentation accurate?
```

#### 11. **@Code Commenting** - Comment Specialist
*(Also useful for doc tasks)*
```
@Code Commenting Improve code comments for maintainability
```

---

### Analysis & Investigation (3 agents)

#### 12. **@Forensic Analysis** - Investigator
Security vulnerabilities, root cause analysis, bug investigation
```
@Forensic Analysis Investigate this security vulnerability
```

#### 13. **@Systemic Risk Analysis** - Risk Analyst
Quantitative risk analysis, accountability, complex systems
```
@Systemic Risk Analysis Analyze risks in this system design
```

#### 14. **@Code Analysis** - Code Quality Analyzer
*(Also useful for analysis)*
```
@Code Analysis What are the quality issues in this code?
```

---

## Common Use Cases

### "I need to review code"
Use: `@Code Analysis`

### "Performance is slow"
Use: `@Performance Optimization`

### "Need to modernize legacy system"
Use: `@Legacy Modernization` or `@Architecture Design`

### "Security vulnerability found"
Use: `@Forensic Analysis`

### "Create project documentation"
Use: `@README Documentation` or `@Product Documentation`

### "Need test strategy"
Use: `@Test Automation`

### "Complex problem, need help"
Use: `@Automated Reasoning`

### "Document this code"
Use: `@Code Commenting` or `@Documentation Integrity`

---

## Handy Commands

```bash
# List all agents
/home/kevin/Projects/BeastMode/setup-beastmode.sh --list

# Verify setup
/home/kevin/Projects/BeastMode/setup-beastmode.sh --verify

# Setup a project
/home/kevin/Projects/BeastMode/setup-beastmode.sh --project .

# Get help
/home/kevin/Projects/BeastMode/setup-beastmode.sh --help
```

---

## Key Facts

- **12 Specialized Agents** covering development, documentation, and analysis
- **One-Time Setup** - Run setup script in any project
- **Automatic Discovery** - Agents appear in VS Code Copilot Chat
- **No Installation** - All agents ready to use
- **Zero Cost** - Uses your GitHub Copilot subscription

---

## Documentation

- **GITHUB-COPILOT-SETUP.md** - Complete setup instructions
- **AGENTS-REGISTRY.md** - Detailed agent reference
- **AGENT_CATALOG.md** - Full specifications for each agent
- **README.md** - BeastMode project overview

---

**Location**: `/home/kevin/Projects/BeastMode`  
**Status**: Production Ready ✓
