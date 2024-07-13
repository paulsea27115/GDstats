# Contributing to GDstats

This document provides guidelines for contributing to the GDstats project through bug reports, feature proposals, pull requests, and communications. GDstats uses **English** as the primary language to accommodate contributors globally. Please ensure all communications, including issues, feature requests, pull requests, and commit messages, are written in English.

## Table of Contents
- [Reporting Bugs](#reporting-bugs)
- [Proposing Features or Improvements](#proposing-features-or-improvements)
- [Pull Request & Commit Guidelines](#pull-request--commit-guidelines)
- [Branching Strategy](#branching-strategy)
- [Communicating with Developers](#communicating-with-developers)

---

## Reporting Bugs
To report bugs in GDstats functionality, please use our [Issue Template](https://github.com/maldron0309/GDstats/blob/main/ISSUE_TEMPLATE.md) to provide detailed descriptions of encountered issues. If you encounter a bug, please create an [issue](https://github.com/maldron0309/GDstats/issues/new?assignees=&labels=&template=bug_report.yml).

---

## Proposing Features or Improvements
We welcome and encourage proposals for new features or improvements. Please utilize our [Feature Template](https://github.com/maldron0309/GDstats/blob/main/FEATURE_TEMPLATE.md) and complete the form to submit your feature suggestions.

---

## Pull Request & Commit Guidelines

### Simple PR Methodology
- **Single Topic PRs**: For clarity and ease of review, submit separate PRs for each distinct issue or feature. This approach simplifies the review process and facilitates quicker merging of changes.
- **One Issue per PR**: Ensure each PR addresses a single specific issue. This practice enhances transparency and enables efficient management of contributions.

### Commit Guidelines

##### Avoiding "Merge Commits"
- Use `git pull --rebase` when updating your fork from upstream to avoid unnecessary "merge commits" that clutter the commit history.

##### Writing Commit Messages
- Start commit messages with an imperative verb (e.g., Add, Fix, Update).
- Examples:
  - `Add support for Python scripting`
  - `Fix issue with card profile display`
  - `Update README with installation instructions`
- Begin with a capital letter and keep messages concise. Detailed explanations should be provided in the PR description.

##### Linking Issues
- If a commit resolves a specific issue, include the issue number in parentheses at the end of the commit message (e.g., `Fix card profile display issue (Fixes #123)`).
- Use GitHub's closing keywords (`Closes #123`, `Fixes #123`) in commit messages or PR descriptions to automatically close related issues upon PR merge.

By adhering to these guidelines, you contribute to a clean project history and streamline the review process for your contributions.

---

## Branching Strategy
GDstats follows a structured branching strategy for development:

- **main**: The main branch for stable releases.
- **develop**: The development branch for ongoing development work.
- **x.x.x (Version Branches)**: Version-specific branches for ongoing version development. Branch names should reflect the related issue (e.g., "card-profile" for resolving issues related to card profile display).

When resolving issues, create PRs against the appropriate version branch.

---

## Communicating with Developers
For any queries or discussions related to development, please contact me via email at parkdev640@gmail.com or on Discord at park_0812.

---

These guidelines aim to provide clarity, efficiency, and collaboration in contributing to GDstats. Your contributions are highly valued and appreciated!
