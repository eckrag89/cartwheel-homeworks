# Cartwheel course repository

Cartwheel is the support agent used throughout "Evaluating and Improving AI Agents." Students complete the starter code and use the same repository for later evaluation exercises.

## Before each session: sync Erik's fork with the course repo

This clone is Erik's fork. `origin` is `eckrag89/cartwheel-homeworks` (where Erik pushes his homework). `upstream` is `ai-evals-course/cartwheel-homeworks` (the course repo, push disabled). The course releases assignments incrementally, so check for new upstream work at the start of every session, before reading handouts or writing code.

```bash
git fetch upstream
git log --oneline HEAD..upstream/main
```

If upstream is ahead, report what changed and ask Erik before syncing. Once he agrees:

```bash
gh repo sync eckrag89/cartwheel-homeworks --source ai-evals-course/cartwheel-homeworks
git pull --ff-only origin main
```

Never force a sync that would discard Erik's committed homework. If the fast-forward fails because his work has diverged, stop and show him the conflict rather than resetting or rebasing on your own. Re-read any handout that the sync changed.

## Find the relevant instructions

- Read [README.md](README.md) for setup and commands. Run commands from the repository root.
- For homework help, identify the assignment from the request and existing work. If it is unclear, ask which assignment the student is working on. The [homework index](homework/README.md) lists released assignments.
- For HW1, HW2, or HW3, read the relevant handout in `homework/module-1/` and follow its requirements and deliverables. When the student invokes a handout's interactive walkthrough, follow its pacing and review points. For HW3, also read and follow `scenarios/skill/SKILL.md`; keep query generation separate from application execution and stop for the required human reviews.
- For repository maintenance, follow the requested change directly. Preserve unfinished homework functions unless implementing them is part of the request.

## Shared rules

- Read [SPEC.md](SPEC.md) and the relevant function contracts before changing agent behavior. Policy numbers come from `facts.yaml`. Editing the specification alone does not change the running application.
- Reuse the supplied database and authorization helpers and return structured tool results.
- Preserve permission checks, refund thresholds, human approval, and kill-switch protections. Keep evaluation cases as regression tests and keep evaluation inputs out of prompts.
- Preserve existing student work and settings. Before regenerating data, check whether it would erase work the student wants to keep. Generate demo data through the seed tools and preserve the pinned demo orders. Confine adversarial fixtures to temporary database copies and keep their generated data out of commits.
- Handle API keys locally through `.env`. Never request keys in chat, print their values, or commit them. Refer to credentials by environment variable name.
- Homework placeholders intentionally raise `NotImplementedError`. Expected failures are unfinished work, not proof of completion. Follow the handout's focused tests and run relevant regression checks; resolve mismatches without weakening requirements or tests merely to pass.
- Report which checks ran offline and which used a live model, and record only observed conversations and tool results. When helping with a submission, leave the student's assessments and recording to the student, and keep unverified deliverables marked as pending.

The repository root `AGENTS.md` is the canonical instruction file. The root `CLAUDE.md` is a relative symlink to it; edit the target rather than maintaining a second copy.
