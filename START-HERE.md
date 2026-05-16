# START HERE: BeastMode Agents for GitHub Copilot

You now have **12 specialized GitHub Copilot agents** ready to use. Follow these simple steps.

---

## 1. ONE-TIME SETUP (2 minutes)

### Option A: Setup Single Project

In your VS Code project:

```bash
cd /path/to/your/project
/home/kevin/Projects/BeastMode/setup-beastmode.sh --project .
```

Then reload VS Code:
- Mac: `Cmd+Shift+P` > "Developer: Reload Window"
- Windows/Linux: `Ctrl+Shift+P` > "Developer: Reload Window"

### Option B: Setup Multiple Projects

```bash
/home/kevin/Projects/BeastMode/SETUP-ALL-PROJECTS.sh ~/Projects
```

This configures all projects in `~/Projects` directory.

---

## 2. START USING AGENTS

In VS Code Copilot Chat, type `@` to see agents or click the agent dropdown.

### By Use Case

**Need Code Review?**
```
@Code Analysis Review this function for security and performance issues
```

**Optimizing Performance?**
```
@Performance Optimization This query is slow for 10k concurrent users
```

**Modernizing Legacy Code?**
```
@Legacy Modernization How do we upgrade from Node 10 to Node 18?
```

**Testing Strategy?**
```
@Test Automation Help me design a test strategy for 80% coverage
```

**System Design?**
```
@Architecture Design Should we migrate to microservices?
```

**Documentation?**
```
@README Documentation Create a professional README for my project
```

**Security Incident?**
```
@Forensic Analysis Investigate this security vulnerability
```

**Adding Comments?**
```
@Code Commenting Add strategic comments to this function
```

**Complex Problem?**
```
@Automated Reasoning Help me solve this multi-step problem
```

---

## 3. ALL 12 AGENTS

| Agent | Use For | Chat Command |
|-------|---------|--------------|
| **Automated Reasoning** | Complex multi-step problems | `@Automated Reasoning` |
| **Code Analysis** | Code review (quality, security, performance) | `@Code Analysis` |
| **Code Commenting** | Strategic comments & documentation | `@Code Commenting` |
| **Performance Optimization** | Speed & scalability optimization | `@Performance Optimization` |
| **Legacy Modernization** | Updating old systems without downtime | `@Legacy Modernization` |
| **Test Automation** | Test planning and coverage strategy | `@Test Automation` |
| **Architecture Design** | System architecture & microservices | `@Architecture Design` |
| **Systemic Risk Analysis** | Risk quantification and analysis | `@Systemic Risk Analysis` |
| **Documentation Integrity** | Audit docs for accuracy | `@Documentation Integrity` |
| **Forensic Analysis** | Security vulnerabilities & root cause | `@Forensic Analysis` |
| **README Documentation** | Create project READMEs | `@README Documentation` |
| **Product Documentation** | User/dev/admin guides | `@Product Documentation` |

---

## 4. VERIFY SETUP

Check that agents are discoverable:

```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --verify
```

List all available agents:

```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --list
```

---

## 5. DOCUMENTATION

- **QUICK-REFERENCE.md** - Cheat sheet with common commands
- **GITHUB-COPILOT-SETUP.md** - Complete setup instructions
- **AGENTS-REGISTRY.md** - Detailed agent reference
- **AGENT_CATALOG.md** - Full technical specifications

---

## QUICK EXAMPLES

### Example 1: Code Review
```
@Code Analysis Review this TypeScript function:
[paste code]
```

Agent will review for:
- ✓ Code quality
- ✓ Security vulnerabilities
- ✓ Performance issues
- ✓ Best practices
- ✓ Error handling
- ✓ Concurrency safety

### Example 2: Performance Analysis
```
@Performance Optimization This N+1 query is slow. How do I optimize it for 10,000 users?
[paste query]
```

Agent will provide:
- ✓ Bottleneck analysis
- ✓ Optimization recommendations
- ✓ Performance benchmarking plan
- ✓ Scalability roadmap

### Example 3: Create Documentation
```
@README Documentation Create a README for my Node.js REST API with these features:
- User authentication
- CRUD operations
- Rate limiting
```

Agent will create:
- ✓ Complete 16-section README
- ✓ Installation instructions
- ✓ Quick start guide
- ✓ API reference
- ✓ Contributing guidelines

### Example 4: Security Investigation
```
@Forensic Analysis Investigate this vulnerability:
[describe security issue]
```

Agent will provide:
- ✓ Root cause analysis
- ✓ Impact assessment
- ✓ Reproduction steps
- ✓ Remediation roadmap
- ✓ Test cases

---

## TROUBLESHOOTING

### Agents Not Showing?

1. Check setup was applied:
   ```bash
   cat .vscode/settings.json | grep agentFilesLocations
   ```

2. Verify agent files exist:
   ```bash
   /home/kevin/Projects/BeastMode/setup-beastmode.sh --verify
   ```

3. Reload VS Code again:
   - `Cmd+Shift+P` > "Developer: Reload Window"

### Still Not Working?

Run full setup from scratch:
```bash
/home/kevin/Projects/BeastMode/setup-beastmode.sh --project /path/to/project
```

---

## WHAT'S INCLUDED

✓ 12 specialized GitHub Copilot agents  
✓ One-command setup  
✓ Auto-discovery in VS Code  
✓ Works with your existing GitHub Copilot subscription  
✓ No additional costs  
✓ Production-ready  

---

## NEXT STEPS

1. **Setup**: `./setup-beastmode.sh --project .`
2. **Reload**: VS Code reload window
3. **Use**: Type `@` in Copilot Chat
4. **Explore**: Try different agents for different tasks

---

**Location**: `/home/kevin/Projects/BeastMode`  
**Status**: Ready to use ✓  
**Questions?**: See GITHUB-COPILOT-SETUP.md for complete guide
