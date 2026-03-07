# CLAUDE.md — AI Assistant Guide for NewsCollector2

## Project Overview

**NewsCollector2** is a news aggregation and collection project. As of the initial commit, the repository is in its bootstrapping phase — only a `README.md` exists. This file establishes the conventions, workflows, and guidelines that AI assistants and contributors should follow as the project grows.

---

## Repository State

| Item | Status |
|------|--------|
| Source code | Not yet implemented |
| Tests | Not yet implemented |
| Configuration | Not yet implemented |
| Dependencies | Not yet defined |

---

## Git Workflow

### Branches

| Branch | Purpose |
|--------|---------|
| `main` / `master` | Stable, production-ready code |
| `claude/<feature>-<id>` | AI-assisted feature branches |

### Rules

- **Never push directly to `main` or `master`.**
- All changes should be developed on feature branches, then merged via pull request.
- Branch names for AI-assisted work must follow the pattern: `claude/<short-description>-<session-id>`.
- Always push with tracking: `git push -u origin <branch-name>`.
- Write clear, descriptive commit messages in the imperative mood (e.g., "Add article scraper module").

### Commit Message Convention

```
<type>: <short summary>

[optional body explaining why, not what]
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `build`

Example:
```
feat: add RSS feed parser for BBC News
```

---

## Development Guidelines for AI Assistants

### Language / 言語

- **常に日本語で返答してください。** すべての応答、説明、コメントは日本語で行ってください。

### General Principles

1. **Read before editing.** Always read existing files before modifying them.
2. **Minimal changes.** Only make changes directly requested or clearly necessary. Do not refactor surrounding code, add extra comments, or introduce new abstractions unless asked.
3. **No speculative features.** Do not add error handling, configuration options, or utilities for scenarios that don't exist yet.
4. **Security first.** Avoid introducing command injection, SQL injection, XSS, insecure deserialization, or hardcoded secrets.
5. **No backwards-compatibility shims.** If something is unused, delete it cleanly.

### When Implementing Features

- Prefer editing existing files over creating new ones.
- Do not create documentation files (`.md`) unless explicitly requested.
- Do not add type annotations, docstrings, or comments to code you didn't change.
- Keep functions focused and small.
- Validate only at system boundaries (user input, external APIs) — trust internal code.

### When Fixing Bugs

- Identify the root cause; don't work around safety checks.
- Do not clean up surrounding code as part of a bug fix.
- Do not retry failing operations in a loop — diagnose the cause.

---

## Project Intent & Expected Architecture

Based on the project name, **NewsCollector2** is expected to be a news aggregation system. Likely components as the project evolves:

```
NewsCollector2/
├── src/                  # Application source code
│   ├── collectors/       # Source-specific scrapers / RSS readers
│   ├── models/           # Data models (articles, sources, etc.)
│   ├── storage/          # Database / persistence layer
│   ├── api/              # HTTP API (if applicable)
│   └── utils/            # Shared utilities
├── tests/                # Test suite
├── config/               # Configuration files
├── .env.example          # Environment variable template (never commit .env)
├── README.md
└── CLAUDE.md             # This file
```

This structure should be adopted once implementation begins.

---

## Environment & Configuration

- Never commit `.env` files or secrets to the repository.
- Use `.env.example` to document required environment variables without values.
- All configurable values (API keys, URLs, intervals) must come from environment variables or a config file, never hardcoded.

---

## Testing

- All new features should include tests.
- Tests live in the `tests/` directory, mirroring the `src/` structure.
- Run tests before committing any code changes.
- No test framework has been chosen yet — document the choice in this file when one is selected.

---

## Useful Commands

> These will be populated once the tech stack is decided and implemented.

```bash
# Install dependencies
# (TBD based on language/framework)

# Run the application
# (TBD)

# Run tests
# (TBD)

# Lint / format code
# (TBD)
```

---

## Metadata

- **Repository**: `Master-Misoshiru/NewsCollector2`
- **Remote**: `http://local_proxy@127.0.0.1:35765/git/Master-Misoshiru/NewsCollector2`
- **Last updated**: 2026-03-07
- **Author**: Master-Misoshiru
