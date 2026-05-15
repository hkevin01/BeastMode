# Legacy Modernization Mode

## Overview

The Legacy Modernization mode specializes in assessing and incrementally modernizing outdated codebases while maintaining zero-downtime operations and full backward compatibility.

## Files

- **`legacy-modernizer.agent.md`** - Legacy code modernization specialist

## Target Audience

- Modernization project leads
- Architecture decision makers
- Database migration specialists
- DevOps engineers
- Technical program managers

## Modernization Dimensions

- **Legacy Assessment**: Technology audit, security review, performance analysis
- **Business Logic Documentation**: Preserving tribal knowledge, edge cases
- **Modernization Strategy**: Technology stack, architecture, migration approach
- **Implementation Roadmap**: Phased approach with safety nets and rollback plans
- **Data Migration**: Zero-downtime database migrations with validation
- **Risk Mitigation**: Failure modes, automatic rollback, communication plans

## Migration Patterns

- **Strangler Fig** (Recommended): Gradual replacement behind facade
- **Big Bang Rewrite**: Complete rewrite (higher risk, faster cutover)
- **Component-by-Component**: Incremental module replacement

## Zero-Downtime Constraint

All recommendations maintain:
- Production availability throughout migration
- Feature flags for gradual rollout
- Backward compatibility
- Instant rollback capability at any point
- Data integrity assurance

## Deliverables

1. Legacy Assessment Report
2. Modernization Architecture Design
3. Detailed Migration Roadmap
4. Technical Implementation Guides
5. Failure Mode Analysis
6. Knowledge Preservation Documentation

## Use Cases

- Legacy system modernization
- Technology stack upgrades
- Database migrations
- API modernization
- Compliance and security updates
- Performance improvements in aging systems
- Preparing for cloud migration
