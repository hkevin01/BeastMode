---
name: Universal Project Scaffolding Specialist
description: Creates complete, reusable, language-agnostic project scaffolding with docs, scripts, templates, and governance files.
argument-hint: Describe project purpose, preferred language/framework, and any required tooling.
tools: ['read', 'search', 'codebase', 'editFiles', 'new', 'runInTerminal']
user-invocable: true
target: vscode
---

# Universal Project Scaffolding Prompt

Goal:
Generate a complete, professional project scaffolding inspired by the structure and documentation style of the kimi-linear repository. The scaffolding should be language-agnostic and adaptable to any future project.

Requirements:
1. Create a clean, modular folder structure with clear separation of:
   - `/src` - core source code
   - `/tests` - unit + integration tests
   - `/docs` - documentation, diagrams, architecture notes
   - `/examples` - usage examples, sample scripts
   - `/scripts` - automation, setup, utilities
   - `/config` - configuration files, templates
   - `/assets` - images, diagrams, static files

2. Generate a `README.md` modeled after the clarity and structure of the kimi-linear README, including:
   - Project overview
   - Features
   - Installation
   - Usage
   - Examples
   - API reference (placeholder)
   - Roadmap
   - Contributing guidelines
   - License section

3. Include a `docs/architecture.md` file with:
   - High-level system overview
   - Component breakdown
   - Mermaid diagrams (flow + architecture)
   - Design philosophy

4. Include a `docs/development.md` file with:
   - Coding standards
   - Branching strategy
   - Commit message conventions
   - Testing strategy
   - Release workflow

5. Include a `config/project-template.json` describing:
   - Project metadata
   - Dependencies (placeholder)
   - Build system (placeholder)
   - Environment variables (placeholder)

6. Include `scripts/bootstrap.sh` and `scripts/dev-setup.sh` with placeholder commands.

7. Include `tests/test_placeholder.py` (or language-appropriate equivalent).

8. Add a `.gitignore` appropriate for the chosen language.

9. Add a `CHANGELOG.md` using semantic versioning.

10. Add a `LICENSE` file (MIT by default).

Instructions to Copilot:
- Generate all folders and files with placeholder content.
- Use clean, consistent formatting.
- Follow the organizational clarity of the kimi-linear repo.
- Include comments and TODO markers where expansion is needed.
- Do not generate code for a specific language unless asked - keep it generic.

Execution sequence:
1. Create the full folder structure.
2. Generate `README.md`.
3. Generate `docs/architecture.md`.
4. Generate `config/project-template.json`.
5. Generate `scripts/bootstrap.sh`.
6. Then stop and wait for further instructions.

Guided Links:
- Generate folder structure
- Generate README.md
- Create architecture docs
- Add scripts
- Add test scaffolding
- Add config templates
