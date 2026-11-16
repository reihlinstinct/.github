# Maintenance and security

Use one issue and a small branch/PR per change. Describe what changed, why, tests and limits. Require independent exact-head review and green CI before squash merge. Never commit secrets or private information. Report vulnerabilities using this repository's private vulnerability reporting feature once enabled; do not post secret values in issues. Do not claim this feature is enabled until settings have been verified.

Publication checklist: public repository, main default branch, meaningful description/topics, private vulnerability reporting and available free secret-scanning/push-protection features enabled, branch protection with required CI and independent review, no bypass, and administrator verification of the rendered Sponsor link. No paid service should be enabled. GitHub settings are not configured by these files.

CI is read-only and offline. Dependabot updates pinned GitHub Actions weekly. Code ownership requires review by @reihl. Layout checking rejects root Python, unlisted folders and unexpected types. The funding regression checks the exact approved URL, shape and inherited-file boundary. There is no executable product requiring a container or browser test. Confirm the visible button on representative destination repositories after publication.
