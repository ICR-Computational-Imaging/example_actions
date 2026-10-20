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
| `test.yaml` | Installs the project and pytest with uv, then tests the hello-world output and time formatting. A failing test makes the workflow fail. Uses the same triggers as `helloworld.yaml`. |
| `lint.yaml` | Uses Ruff to check Python files for common mistakes, such as unused imports. Runs on branch pushes, PRs targeting `main` or `dev`, or manually. |
| `matrix.yaml` | Runs the unit tests in separate jobs for Python 3.12 and 3.13. Runs on branch pushes, PRs targeting `main` or `dev`, or manually. |
| `artifact.yaml` | Saves the hello-world output to a text report and uploads it for download. Runs on branch pushes or manually. |
| `matplotlib.yaml` | Runs `src/examples/plot.py` without a graphical display, saves `plot.png`, and uploads it as a downloadable artifact. Runs on branch pushes or manually. |
| `inputs.yaml` | Adds a greeting field and a repetition dropdown to the manual **Run workflow** form. |
| `dependent_jobs.yaml` | Uses `needs` to run a report job only after the unit tests pass. Runs on branch pushes, PRs targeting `main` or `dev`, or manually. |
| `conditions.yaml` | Uses `if` to select steps based on the branch or trigger event. Runs on branch pushes, PRs targeting `main` or `dev`, or manually. |
| `schedule.yaml` | Runs hello world daily at 09:17 UTC, or manually. The schedule requires the workflow on the default branch. |
| `secret.yaml` | Manual teaching example that prints a dummy secret to demonstrate GitHub's log masking. **Use a dummy value only; real secrets must never be printed or shared.** See setup below. |

The uv example installs the dependencies declared in `pyproject.toml` at the versions recorded in `uv.lock`. After changing dependencies, run `uv lock` locally and commit both files before running the workflow.

## Running the unit tests

Run the hello-world tests locally with uv:

```bash
uv sync --locked --group dev
uv run --locked --group dev python -m pytest -v
```

The tests in `tests/test_helloworld.py` check time formatting and the ten numbered output lines using simple assertions. Pytest's `capsys` fixture collects the printed output so it can be checked. The tests run the real script, including its pauses. Pytest and Ruff are declared in the `dev` dependency group in `pyproject.toml`.

Copy `example_workflows/test.yaml` into `.github/workflows/` to run the same commands on GitHub. Commit and push the tests, workflow, `pyproject.toml`, and updated `uv.lock` together.

## Trying the other examples

Enable each example by copying it into `.github/workflows/` using the steps above.

- **Linting:** Run `uv run --locked --group dev ruff check src tests` locally. For a lecture demonstration, add an unused import to a Python file and see the check fail; remove it to make the check pass again.
- **Matrix:** Open the workflow run to see a separate test job for each Python version. Edit `strategy.matrix.python-version` to change the versions tested; each version must satisfy the project's Python requirement.
- **Artifacts:** Open a completed **Downloadable report** run and download `hello-world-report` from its **Artifacts** section. It contains `hello-world.txt` and is retained for seven days.
- **Matplotlib:** Enable `matplotlib.yaml`, then download `example-plot` from the completed run's **Artifacts** section to view `plot.png`. The workflow sets `MPLBACKEND=Agg` and the script uses `savefig()` to save an image. To try it locally, run `uv run --locked python src/examples/plot.py`; the image is saved in your current directory.
- **Inputs:** Open **Manual inputs → Run workflow**, enter a greeting, and choose how many times to print it.
- **Dependent jobs:** The report job waits for the test job. If a test fails, the report job is skipped. When tests pass, the run's summary page shows the success report.
- **Conditions:** Compare a branch push, a PR, and a manual run to see which steps run or are skipped. The main-branch step checks the branch name `main`; change it if your default branch has another name.
- **Schedule:** The daily trigger uses UTC (09:17 UTC is 09:17 UK winter time or 10:17 UK summer time). GitHub runs scheduled workflows from the default branch and may delay runs. Scheduled workflows are disabled by default in forks; enable the workflow in the Actions tab. In public repositories, schedules are automatically disabled after 60 days without repository activity. You can also try the example manually.

See GitHub's documentation on [workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [artifacts](https://github.com/actions/upload-artifact), and [scheduled events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

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
