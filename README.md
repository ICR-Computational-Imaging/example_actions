# example_actions

Example GitHub Actions workflows for use in a lecture series. More examples will be added over time.

## Getting started

1. Fork [this repository](https://github.com/ICR-Computational-Imaging/example_actions) into your own GitHub account using the **Fork** button.

2. Clone your fork locally, replacing `YOUR-USERNAME` with your GitHub username:

   ```bash
   git clone https://github.com/YOUR-USERNAME/example_actions.git
   cd example_actions
   ```

3. Move one or more example YAML files from `example_workflows/` into `.github/workflows/` to enable them. For example:

   ```bash
   mkdir -p .github/workflows
   git mv example_workflows/helloworld.yaml .github/workflows/
   ```

   Repeat the `git mv` command for any other examples you want to try. Only workflows in `.github/workflows/` are picked up by GitHub Actions.

4. Commit your changes and push them back to your fork on GitHub:

   ```bash
   git commit -m "Enable example workflows"
   git push origin HEAD
   ```

   Open the **Actions** tab in your fork to view workflow runs. If GitHub prompts you to enable Actions for the fork, enable them, then push another commit or use **Run workflow** for examples that support manual runs.

## Example workflows

This table will grow as new examples are added. Filenames below refer to files in `example_workflows/` before you move them.

| Workflow | What it demonstrates |
| --- | --- |
| `helloworld.yaml` | Checks out the repository, sets up Python 3.12, and runs Python using an inline command, multiple shell commands, and a script file. Runs on branch pushes, pull requests targeting `main` or `dev`, or a manual trigger. |
