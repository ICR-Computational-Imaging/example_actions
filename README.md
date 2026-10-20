# Example GitHub Actions

Example GitHub Actions workflows for use in a lecture series. More examples will be added over time.

## Getting started

1. Fork [this repository](https://github.com/ICR-Computational-Imaging/example_actions) into your own GitHub account using the **Fork** button.

2. Clone your fork locally, replacing `YOUR-USERNAME` with your GitHub username:

   ```bash
   git clone https://github.com/YOUR-USERNAME/example_actions.git
   cd example_actions
   ```

3. Copy one or more example YAML files from `example_workflows/` into `.github/workflows/` to enable them. For example:

   ```bash
   mkdir -p .github/workflows
   cp -f example_workflows/helloworld.yaml .github/workflows/
   ```

   Repeat the `cp` command for any other examples you want to try. Only workflows in `.github/workflows/` are picked up by GitHub Actions.

   Some examples may already be enabled in `.github/workflows/`. Copying an identical file won't create a change to commit; you can instead view existing runs or use **Run workflow** in the Actions tab for examples that support manual runs.

4. Commit your changes and push them back to your fork on GitHub:

   ```bash
   git add .github/workflows
   git commit -m "Enable example workflows"
   git push origin HEAD
   ```

   Open the **Actions** tab in your fork to view workflow runs. If GitHub prompts you to enable Actions for the fork, enable them, then push another commit or use **Run workflow** for examples that support manual runs.

   **Manual runs:** The workflow file must exist in `.github/workflows/` on your repository's default branch (usually `main`) with `workflow_dispatch` enabled before **Run workflow** is available. Once it does, you can select another branch, such as `dev`, from the **Branch** dropdown to run that branch's version. The workflow on the selected branch must also have `workflow_dispatch` enabled.

## Example workflows

This table will grow as new examples are added. Filenames below refer to files in `example_workflows/` before you copy them.

| Workflow | What it demonstrates |
| --- | --- |
| `helloworld.yaml` | Checks out the repository, sets up Python 3.12, and runs Python using an inline command, multiple shell commands, and a script file. Runs on branch pushes, pull requests targeting `main` or `dev`, or a manual trigger. |
| `helloworld_uv.yaml` | Uses uv to set up Python 3.12, install the project and its dependencies with `uv sync --locked`, and run the example script with `uv run`. Uses the same triggers as `helloworld.yaml`. |
| `secret.yaml` | Manual teaching example that prints a dummy secret to demonstrate GitHub's log masking. **Use a dummy value only; real secrets must never be printed or shared.** See setup below. |

The uv example installs the dependencies declared in `pyproject.toml` at the versions recorded in `uv.lock`. After changing dependencies, run `uv lock` locally and commit both files before running the workflow.

## Secrets

GitHub Actions secrets store sensitive values, such as API tokens, outside your source code. Workflows access them through the `secrets` context and can pass them to individual steps as environment variables. Never commit real secrets to the repository or share them in logs, screenshots, or artifacts.

To try `secret.yaml` with a harmless dummy value:

1. In your fork on GitHub, open **Settings → Secrets and variables → Actions**.
2. Select **New repository secret**.
3. Set the name to `DEMO_SECRET` and the value to `lecture-demo-value-only`. This is a dummy value, not a real credential.
4. Select **Add secret**. Configure this in your own fork; the original repository's secrets are not copied into forks.
5. Copy `example_workflows/secret.yaml` into `.github/workflows/`, commit, and push as described above.
6. If on the `main` branch you can also open **Actions → Secret masking example → Run workflow**, select a branch, and run it.

The workflow passes `${{ secrets.DEMO_SECRET }}` to the step as the `DEMO_SECRET` environment variable. If the secret is missing or empty, the step fails with a setup message. Otherwise, GitHub should mask its value in the log:

```text
Dummy secret (expected to be masked): ***
```

This print statement is for teaching only. In real workflows, pass secrets directly to the tools that need them without printing them. Masking is not guaranteed, particularly when values are transformed, so never use it as a reason to log real credentials. Local shell runs do not provide GitHub's automatic masking.

See GitHub's documentation on [setting up and using secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets) and [secret masking](https://docs.github.com/en/actions/concepts/security/secrets).
