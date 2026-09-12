# Fork changes

Personal modifications to [openai/codex](https://github.com/openai/codex).

This file tracks active differences from upstream. Update the relevant entry when
changing or removing a feature, and record any upstream PR or maintenance notes
that will help when syncing the fork.

## Model picker shortcut

- Ctrl+Shift+P opens the model picker while preserving the current draft on
  terminals that support enhanced keyboard reporting. Legacy terminals collapse
  it to Ctrl+P, which does not open the picker.
- Configurable through `tui.keymap.global.open_model_picker`.
- Motivation: switch models without typing a slash command.
- Introduced in: `e6fc7fa73` (`feat(tui): add model picker shortcut`).

## Fork installation target

- `just install-codex` installs the local fork's `codex`, `logs_client`, and
  `codex-code-mode-host` binaries. On Unix, it installs them under
  `~/.local/bin`.
- The code-mode host build resolves the native Rust host target and downloads
  the matching checksum-verified `rusty_v8` archive and generated binding from
  the Codex release. The pinned V8 version is not available from the upstream
  `rusty_v8` release location.
- Use this target instead of the upstream curl, npm, or Homebrew installers when
  installing this fork.
- Introduced in: `09c6e2b43` (`chore(fork): add local install target`); code-mode
  host installation added in `41df6d8c4` (`fix(build): install code mode host`).

## Local release build recursion limits

- `codex-exec` and `codex-tui` use a recursion limit of 256 so release builds can
  lay out the deeply nested in-process app-server future.
- Keep these crate-level limits aligned with `codex-app-server` when syncing
  changes that affect its async request dispatch.
