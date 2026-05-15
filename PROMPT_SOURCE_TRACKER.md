---
title: BeastMode Prompt Source Tracker
description: Documentation of where each BeastMode agent originated from Claude-prompts repository
lastUpdated: "2026-05-15"
---

# BeastMode Prompt Source Tracker

This document tracks the origin of each BeastMode agent mode and the Claude-prompts they were derived from.

## Source Repository

**Location**: `/home/kevin/Projects/claude-prompts/`

**Main Categories**:
- `prompts/coding/` - Software engineering and development prompts
- `prompts/workflow/` - Process and workflow prompts
- `prompts/priority/` - Priority and planning prompts

## Mode Mapping to Source Prompts

### Automated Reasoning Mode
**Source**: Original BeastMode 3.1 development  
**Status**: Core agent, continuously refined  
**Agent Files**:
- `primary-solver.agent.md` - Modern VS Code format
- `beastmode_kevin.agent.md` - Primary agent
- `beastmode_kevin.md` - Profile content
- `legacy-format.chatmode.md` - Legacy compatibility

---

### Systemic Risk Analysis Mode
**Source**: Custom domain specialization  
**Status**: Specialized for policy research and corruption modeling  
**Agent Files**:
- `conpattern-accountability.agent.md` - Derived from systemic analysis requirements

---

### Documentation Integrity Mode
**Source**: Custom domain specialization  
**Status**: Specialized for code-traceable documentation  
**Agent Files**:
- `readme-code-truth.agent.md` - Derived from documentation audit requirements

---

### Forensic Analysis Mode
**Source**: Custom domain specialization  
**Status**: Specialized for security investigation  
**Agent Files**:
- `code-forensics-specialist.agent.md` - Derived from security audit requirements

---

### Code Analysis Mode
**Source**: Claude-prompts `/prompts/coding/`  
**Related Prompts**:
- `comprehensive-code-review.md` - Primary source ✓
- `code-review-assistant.md` - Additional reference
- `security-code-review.md` - Security dimension reference

**Agent**: `comprehensive-reviewer.agent.md`  
**Status**: Active and maintained  
**Specialization**: Multi-dimensional code review (quality, security, performance, best practices)

---

### Performance Optimization Mode
**Source**: Claude-prompts `/prompts/coding/`  
**Related Prompts**:
- `performance-code-review.md` - Primary source ✓
- `systematic-debugger.md` - Debugging reference
- `dependency-upgrade-strategy-prompt.md` - Related

**Agent**: `performance-optimizer.agent.md`  
**Status**: Active and maintained  
**Specialization**: Algorithm efficiency, database optimization, scalability planning

---

### Legacy Modernization Mode
**Source**: Claude-prompts `/prompts/coding/`  
**Related Prompts**:
- `legacy-code-modernizer.md` - Primary source ✓
- `project-setup-modernizer.md` - Setup reference
- `dependency-upgrade-strategy-prompt.md` - Dependencies

**Agent**: `legacy-modernizer.agent.md`  
**Status**: Active and maintained  
**Specialization**: Legacy system modernization with zero-downtime migration

---

### Test Automation Mode
**Source**: Claude-prompts `/prompts/coding/`  
**Related Prompts**:
- `test-automation-strategy-prompt.md` - Primary source ✓
- `phased-test-strategy.md` - Strategy reference
- `simple-poc-development.md` - Testing approach

**Agent**: `test-specialist.agent.md`  
**Status**: Active and maintained  
**Specialization**: Test strategy, coverage planning, automation architecture

---

### Architecture & Microservices Design Mode
**Source**: Claude-prompts `/prompts/coding/`  
**Related Prompts**:
- `microservices-architecture-prompt.md` - Primary source ✓
- `system-architecture-design-prompt.md` - Architecture reference
- `microservices-architect.md` - Additional details

**Agent**: `architect.agent.md`  
**Status**: Active and maintained  
**Specialization**: System architecture, microservices decomposition, scalability

---

## Unmapped Claude-Prompts (Available for Future Modes)

### High Priority (Good for Additional Modes)
- `rest-api-developer.md` - REST API design and development
- `graphql-api-developer.md` - GraphQL API specialization
- `api-code-generation-prompt.md` - API code generation
- `repo-cleanup-organizer.md` - Repository organization
- `simple-poc-development.md` - Proof-of-concept development
- `system-architecture-design-prompt.md` - Additional architecture focus

### Workflow/Process Prompts
- `beast-mode-tasksync.md` - Task synchronization (BeastMode-related)
- `iterative-improvement-workflow.md` - Iterative development
- `phase-implementation-guide.md` - Phased implementation
- `project-completion-audit.md` - Project completion verification
- `universal-project-initialization.md` - Project setup
- `universal-readme-generator.md` - README generation

### Medium Priority
- `graphql-api-development-prompt.md` - GraphQL specialization
- `api-code-generator.md` - Code generation focus
- `sam-contract-finder-improver.md` - Contract analysis

### Additional Tools
- `operational-rules-standards.md` - Operational guidelines
- `copilot-focus-config.md` - Copilot configuration

---

## Creation Process

### To Create a New Mode from Claude-Prompts

1. **Identify the prompt**: Browse `/home/kevin/Projects/claude-prompts/prompts/`
2. **Create the mode folder**: `modes/[mode-name]/`
3. **Read the prompt**: Extract key concepts and structures
4. **Create agent file**: `[specific-name].agent.md`
   - Convert prompt content to agent instructions
   - Add frontmatter with name, description, tools
   - Add specific rules, requirements, deliverables
5. **Create README**: Document purpose, audience, capabilities
6. **Update AGENT_CATALOG.md**: Add new mode to the catalog
7. **Update setup scripts**: Ensure new agent is discoverable

### Template for New Modes

```markdown
---
name: [Agent Name]
description: [Purpose and specialization]
argument-hint: [What input this agent expects]
tools: ['read', 'search', 'codebase', 'web', 'fetch']
---

# [Agent Purpose]

[Detailed agent instructions based on Claude prompt]

## [Key Dimension 1]
[Details]

## [Key Dimension 2]
[Details]

## DELIVERABLES
[What the agent outputs]

## REQUIREMENTS
[Quality standards]
```

---

## Prompt Library Statistics

**Total Prompts in Claude-Prompts**: ~35+  
**Currently Used**: 8 modes + 4 specialized  
**Remaining Available**: ~20+

**Distribution**:
- Coding: ~22 prompts (focused on development)
- Workflow: ~8 prompts (processes and methods)
- Priority: ~5 prompts (planning and organization)

---

## Maintenance & Updates

### Regular Review (Monthly)
- [ ] Check for new prompts in Claude-prompts repository
- [ ] Evaluate suitability for BeastMode modes
- [ ] Consider merging similar modes
- [ ] Update agent instructions based on feedback

### Update Cycle
- **Sources**: Listen to /home/kevin/Projects/claude-prompts for changes
- **Agent Files**: Update agent definitions when source prompts change
- **Catalog**: Update AGENT_CATALOG.md with new/modified agents
- **Testing**: Verify new agents work properly in VS Code

### Versioning
- Agent files tracked with timestamps
- AGENT_CATALOG.md maintains last-updated date
- Major changes documented in CHANGELOG.md (recommended)

---

## Automation Script Updates

The `setup-beastmode.sh` script automatically:
- Discovers all `.agent.md` files in `modes/*/`
- Lists available agents in setup output
- Configures VS Code settings for automatic discovery
- Handles updates without manual configuration

**Run Setup**:
```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh
```

---

## Future Enhancements

### Potential New Modes from Available Prompts
- **API Development Mode** (REST & GraphQL)
- **Project Initialization Mode** (Setup automation)
- **Repository Organization Mode** (Code organization)
- **Documentation Generation Mode** (README, API docs)
- **Contract Analysis Mode** (Legal/compliance)
- **DevOps & Infrastructure Mode** (Cloud, deployment)

### Infrastructure Improvements
- [ ] Automated prompt-to-agent converter
- [ ] Prompt versioning and tracking
- [ ] Agent update notifications
- [ ] Agent usage analytics
- [ ] Community contributions framework
- [ ] Agent marketplace/registry

---

**Maintained by**: BeastMode Development Team  
**Last Updated**: May 15, 2026  
**Next Review**: June 15, 2026
