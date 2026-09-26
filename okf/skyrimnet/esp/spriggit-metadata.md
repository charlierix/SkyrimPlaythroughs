---
type: Tooling Metadata
title: "Spriggit Metadata"
description: "spriggit-meta.json, root RecordData.json and GroupRecordData.json files describing the Spriggit serialization of SkyrimNet.esp."
resource: "sources/SkyrimNet-GamePlugin/spriggit/SkyrimNet/spriggit-meta.json"
tags: [skyrimnet, esp, records]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Spriggit serialization metadata for `SkyrimNet.esp`: package meta (`Spriggit.Json.Skyrim` 0.40.1, SkyrimSE), the root `RecordData.json`, and per-group `GroupRecordData.json` index files. Rebuild the ESP with `Spriggit.CLI.exe convert-to-plugin -i spriggit/SkyrimNet -o SkyrimNet.esp`.

# Build usage

```
# Rebuild the ESP from this tree (Spriggit CLI 0.40.x)
Spriggit.CLI.exe convert-to-plugin -i spriggit/SkyrimNet -o SkyrimNet.esp

# Compile the Papyrus scripts (see scripts/core-runtime)
papyrus.exe -nocache -h headers -i Source/Scripts -output Scripts
```

# Member files

All 5 member items assigned to this concept (verified against the manifest):

| Source file | Size | Lines | Summary |
|---|---|---|---|
| `spriggit/SkyrimNet/Cells/9/3/GroupRecordData.json` | 90.0B | 5 | { |
| `spriggit/SkyrimNet/Cells/9/GroupRecordData.json` | 87.0B | 5 | { |
| `spriggit/SkyrimNet/Cells/GroupRecordData.json` | 29.0B | 3 | { |
| `spriggit/SkyrimNet/RecordData.json` | 335.0B | 18 | { |
| `spriggit/SkyrimNet/spriggit-meta.json` | 125.0B | 6 | { |

# Citations

[1] `sources/SkyrimNet-GamePlugin/spriggit/SkyrimNet/spriggit-meta.json`
[2] `sources/SkyrimNet-GamePlugin/RecordData.json`
[3] `sources/SkyrimNet-GamePlugin/Cells/**/GroupRecordData.json`

