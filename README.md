A plugin for [pre-commit](https://pre-commit.com/) to add modifications introduced during the pre-commit phase to the index.

To use, add the following to your .pre-commit-config.yaml:
```
- repo: https://github.com/shahin/pre-commit-git-add
  rev: v0.4.0
  hooks:
  - id: update
```
