# Contributing to GDstats

This document is intended to guide those interested in contributing to the GDstats project through bug reports or pull requests on how to contribute.
Our GDstats project primarily uses **English** as the common language for the benefit of contributors worldwide.
Therefore, please write issues, feature requests, pull requests, and commit messages in English.
## Table of contents
- [Reporting bugs](#reporting-bugs)
- [Proposing features or improvements](#proposing-features-or-improvements)
- [Pull Request & Commit Guidelines](#pull-request--commit-guidelines)
- [Communicating with developers](#communicating-with-developers)

## Reporting bugs
[Report bugs](https://github.com/maldron0309/GDstats/issues/new?assignees=&labels=&template=bug_report.yml).
If you encounter any issues with GDstats functionality, please write an issue detailing the specific error or problem you are experiencing.
Here is the [Issue Template](https://github.com/maldron0309/GDstats/blob/main/ISSUE_TEMPLATE.md).

## Proposing features or improvements
Proposing features or improvements is always welcome! Please use the [features Template](https://github.com/maldron0309/GDstats/blob/main/FEATURE_TEMPLATE.md) and fill out the form to make your feature suggestion.

## Pull Request & Commit Guidelines

### Simple Methodology for PRs
- **Single Topic PRs**: Try to make simple PRs that handle one specific topic. Just like for reporting issues, it's better to open 3 different PRs that each address a different issue than one big PR with three commits. This makes it easier to review, approve, and merge the changes independently.
- **One Issue per PR**: Only open PRs that solve one specific problem. If there are five different issues to fix, create a separate PR for each issue. This approach is more thorough and makes it easier for maintainers to review, approve, and merge changes.

### Commit Guidelines

##### Avoid Creating "Merge Commits"
- When updating your fork with upstream changes, use `git pull --rebase` to avoid creating "merge commits." These commits unnecessarily pollute the git history and make it harder to track changes.

##### Writing Commit Messages
- Use imperative mood in commit messages. This means starting with a command verb like "Add," "Fix," or "Update."
- Examples:
  - `Add Godot engine playtime`
  - `Fix rank not increasing despite meeting experience requirements`
  - `Core: Fix Object::has_method() for script static methods`
- Start the commit message with a capital letter.
- Keep commit messages short and concise. Provide detailed explanations in the PR description instead.

##### Linking Issues
- If a commit addresses a specific issue, include the issue number in parentheses at the end of the commit message. For example, `Fix card bug (Fixes #223)`.
- Use GitHub's closing keywords in the commit message or PR description to automatically close issues when the PR is merged. Keywords like `Closes #123` or `Fixes #123` will automatically close the issue with the given number when the PR is merged.

By following these guidelines, you help ensure a clean and manageable project history and facilitate the review and integration process for your contributions.


## Communicating with developers
Please contact me via email at parkdev640@gmail.com or on Discord at park_0812.
