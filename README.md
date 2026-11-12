# Default repository funding

This public repository supplies a default Sponsor button for repositories owned by this account. The inherited community files are `.github/FUNDING.yml`, which links to the owner's public PayPal page, and `.github/PULL_REQUEST_TEMPLATE.md`, a default pull request template (acceptance criteria with proof and a generic pre-merge checklist) that applies only to repositories without their own. No payment is initiated here.

GitHub applies defaults to public and private repositories that do not define their own funding file. An existing per-repository `.github/FUNDING.yml` takes precedence. Nothing is copied into destination repositories.

See [architecture](ARCHITECTURE.md) and [maintainer guide](docs/maintainer-guide.md). Validate locally with `python3 tools/check_repo_layout.py` and `python -m unittest discover -s tests -v`. CI runs the same offline checks. No private data, tokens or destination-repo inventory belongs here.
