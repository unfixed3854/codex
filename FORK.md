# Fork changes

Personal modifications to [openai/codex](https://github.com/openai/codex).

This file tracks active differences from upstream. Update the relevant entry when
changing or removing a feature, and record any upstream PR or maintenance notes
that will help when syncing the fork.

## Model picker shortcut

- F2 opens the model picker while preserving the current draft.
- Configurable through `tui.keymap.global.open_model_picker`.
- Motivation: switch models without typing a slash command.
- Introduced in: `e6fc7fa73` (`feat(tui): add model picker shortcut`).

## Fork installation target

- `just install-codex` installs the local fork into `~/.local/bin/codex` on Unix.
- Use this target instead of the upstream curl, npm, or Homebrew installers when installing this fork.

## Local release build recursion limits

- `codex-exec` and `codex-tui` use a recursion limit of 256 so release builds can
  lay out the deeply nested in-process app-server future.
- Keep these crate-level limits aligned with `codex-app-server` when syncing
  changes that affect its async request dispatch.
