# Code Analysis Mode

## Overview

The Code Analysis mode provides comprehensive, multi-dimensional code reviews covering quality, security, performance, and best practices.

## Files

- **`comprehensive-reviewer.agent.md`** - Comprehensive code review specialist

## Target Audience

- Code reviewers and maintainers
- Pull request reviewers
- Code quality advocates
- Senior engineers mentoring junior developers

## Review Dimensions

- **Code Quality**: Structure, patterns, readability, maintainability
- **Security**: Vulnerabilities, input validation, authentication, authorization
- **Performance**: Algorithm complexity, bottlenecks, optimization opportunities
- **Best Practices**: Language conventions, framework patterns, standards compliance
- **Error Handling**: Edge cases, exception management, resource cleanup
- **Concurrency**: Thread safety, race conditions, deadlocks

## Severity Levels

- **Critical**: Must fix before merge
- **High**: Should fix before merge
- **Medium**: Should fix, can defer
- **Low**: Nice-to-have improvements

## Use Cases

- Pre-merge code review
- Architecture review
- Security audit
- Performance bottleneck identification
- Best practices enforcement
- Knowledge sharing and mentoring

## Research-First Workflow

When reviewing code:

1. **Research Phase**
   - Query Google or DuckDuckGo for current best practices in the language/framework
   - Gather security advisories for identified vulnerabilities
   - Review coding standards evolution

2. **Context Phase**
   - Understand the codebase structure
   - Identify architectural patterns and conventions
   - Map dependencies and interactions

3. **Analysis Phase**
   - Review code across all quality dimensions
   - Identify issues by severity
   - Cross-reference against standards and patterns

4. **Feedback Phase**
   - Provide specific, actionable recommendations
   - Include references and best practice links
   - Suggest code examples and patterns
