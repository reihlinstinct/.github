# Default repository funding

This public repository supplies a default Sponsor button for repositories owned by this account. The only inherited community file is `.github/FUNDING.yml`; it links to the owner's public PayPal page. No payment is initiated here.

GitHub applies defaults to public and private repositories that do not define their own funding file. An existing per-repository `.github/FUNDING.yml` takes precedence. Nothing is copied into destination repositories.

See [architecture](ARCHITECTURE.md) and [maintainer guide](docs/maintainer-guide.md). Validate locally with `python tools/check_repo_layout.py` and `python -m unittest discover -s tests -v`. CI runs the same offline checks. No private data, tokens or destination-repo inventory belongs here.
