# Code Commenting & Documentation Mode

## Overview

The Code Commenting mode specializes in adding clear, meaningful comments and documentation to code following NASA-style engineering standards for mission-critical systems.

## Files

- **`commenting-specialist.agent.md`** - Code commenting and documentation specialist

## Target Audience

- Technical writers and documentation specialists
- Senior engineers implementing code review standards
- Teams adopting safety-critical development practices
- Maintainers improving code clarity
- Open source projects requiring better documentation

## Commenting Standards

### File Headers
- Purpose and scope
- Dependencies and imports
- Exports and public APIs
- Modification history

### Function Documentation (NASA-Style)
- Requirement: What it must do
- Purpose: Why it exists
- Inputs/Outputs: Types and ranges
- Pre/Postconditions: State guarantees
- Side Effects: State changes and I/O
- Failure Modes: How it fails
- Error Handling: Mitigation strategies
- Constraints: Performance and resource limits
- References: Standards and algorithms

### Comment Types
- **Logic Blocks**: Explain algorithm phases
- **TODO**: With owner and due date
- **FIXME**: Priority, root cause, solution
- **HACK**: Workaround explanation and review date
- **Performance**: Complexity analysis and optimizations
- **Security**: Risk assessment and mitigation

## Quality Standards

### Good Comments
- Explain WHY, not WHAT
- Document design decisions
- Include relevant constraints and assumptions

## Research-First Workflow

When adding comments:

1. **Research Phase**
   - Query Google or DuckDuckGo for best practices in NASA-style documentation
   - Research domain-specific standards (safety-critical systems, cryptography, etc.)
   - Gather reference implementations and style guides

2. **Code Understanding Phase**
   - Analyze algorithm purpose and complexity
   - Identify mission-critical logic and edge cases
   - Map pre/postconditions and failure modes

3. **Documentation Phase**
   - Add structured comments following NASA standards
   - Document inputs, outputs, and constraints
   - Explain design decisions and rationale

4. **Verification Phase**
   - Ensure comments match implementation
   - Validate completeness of safety documentation
   - Review clarity and accessibility
- Clarify non-obvious code
- Guide future maintainers
- Provide practical examples

### Avoid
- Stating obvious facts
- Repeating code in English
- Complaining about architecture
- Outdated information
- Vague or ambiguous statements

## Supported Languages

- JavaScript/TypeScript (JSDoc)
- Python (docstring)
- Java (Javadoc)
- C/C++ (Doxygen)
- Go (GoDoc)
- Rust (Rustdoc)
- Language-agnostic concepts

## Deliverables

1. **Fully Commented Source Code** - Production-ready with comprehensive documentation
2. **Module Documentation** - Purpose, dependencies, performance characteristics
3. **API Documentation** - Function signatures with working examples
4. **Comment Audit Report** - Coverage percentage, gaps, priority recommendations
5. **Commenting Guidelines** - Project-specific standards and best practices

## Use Cases

- Adding comprehensive documentation to new projects
- Improving legacy code clarity with strategic comments
- Implementing NASA-style standards for safety-critical systems
- Creating team-wide commenting guidelines
- Auditing existing code for documentation gaps
- Preparing code for team onboarding
- Implementing code review standards
- Writing API documentation
- Documenting complex algorithms
- Creating maintainer guides

## Integration

Works with:
- Code Review processes
- Documentation Integrity audits
- Automated documentation generation tools
- API reference generation systems
- Code quality metrics and reporting