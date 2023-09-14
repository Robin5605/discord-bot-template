# Discord Bot Template

A Discord bot template using discord.py that works very well for me. 
Discord bots can actually end up having a lot of boilerplate code for more serious Discord bot projects,
so I've created this repository to help expedite that process of getting started.

# Pre-requisites
- [Python Poetry](https://python-poetry.org/) - This project uses Poetry as the package manager
- [Python 3.11+](https://www.python.org/downloads/) - Python 3.11 is the minimum supported version
- [Docker Engine](https://www.docker.com/get-started/) - Docker Engine is required if you plan on containerizing your Discord bot for deployment
- [Discord Application](https://discord.com/developers/applications) - A Discord application (and a bot) is required. Make sure you have the token on hand.

# Usage
1. Click the "Use this template" button to use this template
2. Clone the newly created repository locally using `git clone`
3. Create an initial `.env` with your bot token:
   ```
   BOT_TOKEN=<YOUR BOT TOKEN HERE>
   ```
4. Install all dependencies using `poetry install --with dev`
5. Activate the Poetry shell with `poetry shell`
6. Run the bot using `python -m bot`

### Cogs and Extensions
Cogs and extensions should go in the `bot/exts/` directory. All extensions **MUST** have a `setup()` function, or they will not be loaded. See [here](https://discordpy.readthedocs.io/en/stable/ext/commands/extensions.html) for more information.

### Tests
Tests should go in the `tests/` directory. This template uses `pytest` for automated tests.

### Linting
Install pre-commit hooks using `pre-commit install`. It will now run on all `git commit`s. This pre-commit is composed of tools like [Black](https://github.com/psf/black) and [Ruff](https://github.com/astral-sh/ruff) which can each be configured under the `[tool.black]` and `[tool.ruff]` sections of `pyproject.toml` respectively. Feel free to customize and tweak these settings to your liking.

### Continuous Integration (CI)
This template comes with a few GitHub Actions for building and publishing Docker images to the GitHub Container Registry, and linting and testing Python code on commits and pull requests. 

# Licensing
This template uses a MIT license. You are free to do whatever you want with it, including copying it, redistributing it (for personal and for commerical), without credit. 
