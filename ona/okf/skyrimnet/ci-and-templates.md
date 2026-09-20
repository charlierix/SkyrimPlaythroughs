---
type: Repository Config
title: "CI Workflows & Issue Templates"
description: "GitHub Actions workflows (validate, publish-base-index, cleanup-prereleases) and issue-template forms."
resource: "sources/SkyrimNet-GamePlugin/.github/ISSUE_TEMPLATE/bug_report.yml"
tags: [skyrimnet, project]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Continuous-integration assets: the `Validate Assets` workflow runs on `windows-latest`, downloading Spriggit CLI 0.40.0 (to verify/rebuild the ESP from the spriggit tree) and the Papyrus compiler 2025.03.18 (to compile `Source/Scripts` against `headers/`).

# Member files

All 5 member items assigned to this concept (verified against the manifest):

| Source file | Size | Lines | Summary |
|---|---|---|---|
| `.github/ISSUE_TEMPLATE/bug_report.yml` | 5.5KB | 175 | name: Bug Report |
| `.github/ISSUE_TEMPLATE/feature_request.yml` | 2.8KB | 81 | name: Feature Request |
| `.github/workflows/cleanup-prereleases.yml` | 791.0B | 27 | name: Cleanup test prereleases |
| `.github/workflows/publish-base-index.yml` | 3.6KB | 94 | name: Publish base-index |
| `.github/workflows/validate.yml` | 4.2KB | 118 | name: Validate Assets |

# Citations

[1] `sources/SkyrimNet-GamePlugin/.github/ISSUE_TEMPLATE/bug_report.yml`
[2] `sources/SkyrimNet-GamePlugin/.github/ISSUE_TEMPLATE/feature_request.yml`
[3] `sources/SkyrimNet-GamePlugin/.github/workflows/cleanup-prereleases.yml`
[4] `sources/SkyrimNet-GamePlugin/.github/workflows/publish-base-index.yml`
[5] `sources/SkyrimNet-GamePlugin/.github/workflows/validate.yml`

