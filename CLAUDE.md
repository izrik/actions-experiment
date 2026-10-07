# CLAUDE.md

Guidance for AI coding agents working in this repository. `AGENTS.md` is a
symlink to this file.

## What this repo is

A sandbox for experimenting with GitHub Actions. There is no application code,
build system, or test suite; the "product" is the workflow files themselves and
what they print when they run. Most changes are made to trigger workflows and
observe their behavior.

## Layout

- `.github/workflows/` — workflow definitions and message templates.
  - Active workflows (picked up by GitHub because they end in `.yml`/`.yaml`):
    - `pr_all.yaml` — runs on PRs to `master` that touch `info.yaml`; dumps
      `github.*` context values.
    - `pr_closed.yml` — runs when a PR to `master` touching `info.yaml` is
      closed; dumps context values. A Slack-style merge notification job is
      commented out.
    - `psql.yaml` — runs on every PR; checks `psql` availability on the runner
      and dumps context values.
  - Disabled workflows: files named `__<name>.yaml__` / `__<name>.yml__`. The
    trailing `__` stops GitHub from loading them. To re-enable one, rename it to
    drop the leading and trailing underscores. They cover building and pushing
    Docker images to `izrik/actions-experiment` on Docker Hub (per commit and
    per tag), re-tagging images, and on-create/on-release/on-push diagnostics.
  - `merge_template.txt`, `push_template.txt` — JSON message templates rendered
    with `envsubst` for Slack webhook notifications.
- `info.yaml` — arbitrary data; editing it is the usual way to trigger the
  path-filtered PR workflows.
- `Dockerfile` — minimal Ubuntu image used by the image-build workflows; bakes
  the `COMMIT` build arg into `/commit.md`.
- `README.md`, `example-file.txt` — filler content, often edited just to create
  a commit.

## Conventions

- Default branch is `master`.
- Workflows reference secrets `DOCKER_USERNAME`, `DOCKER_TOKEN`, and
  `SLACK_WEBHOOK_URL`; never hard-code their values.
- There are no tests to run. To validate a workflow change, check YAML syntax
  locally (e.g. `python -c 'import yaml,sys; yaml.safe_load(open(sys.argv[1]))' <file>`)
  and then observe the run on GitHub (`gh run list`, `gh run view`).
- Keep `CLAUDE.md` as the real file and `AGENTS.md` as a symlink to it.
