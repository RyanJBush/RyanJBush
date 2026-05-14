# Release Guide

## Create and push v1.0.0 tag

Run:

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

## Verify release artifacts

- Ensure GitHub Actions `Deploy GitHub Pages` workflow completed successfully.
- Confirm README badges resolve and Pages is accessible.
- Update `CHANGELOG.md` for future releases before tagging.
