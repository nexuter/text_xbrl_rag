# Response-To-Reviewers Outline: Replication Package Cleanup

## Reviewer Concern

Reviewers may question whether the replication package is too complex, whether stale pilot artifacts could be confused with manuscript evidence, or whether reported counts and metadata are fully aligned with the revised manuscript.

## Revision Summary

We revised the replication package documentation to make the authoritative evidence trail easier to inspect. The package now includes a reviewer-facing file map, updated count tables, updated checksum metadata, and clearer separation between manuscript evidence and deprecated or pilot artifacts.

## Specific Changes

1. Added `REVIEWER_FILE_MAP.md`, which maps each major manuscript claim to the exact replication-package files reviewers should inspect.
2. Updated `AUTHORITATIVE_FILES.md` to include the newest evidence artifacts:
   - XBRL construct-coverage diagnostics;
   - NKE XBRL worked example;
   - context-volume diagnostics;
   - source-environment perturbation diagnostics;
   - bounded sensitivity decision matrix;
   - independent coding materials.
3. Updated `README_REPLICATION.md` to include all diagnostic pipeline steps and the latest expected counts.
4. Updated `PACKAGE_CONTENTS.md` and checksum documentation to remove stale count references.
5. Regenerated the replication-package checksum manifest.

## Suggested Response-Letter Language

We strengthened the replication package documentation to make the evidence trail easier for reviewers to inspect. The revised package now includes a new `REVIEWER_FILE_MAP.md`, which maps each major manuscript claim to the relevant evidence files and states what those files do and do not support. We also updated `AUTHORITATIVE_FILES.md`, `PACKAGE_CONTENTS.md`, and `README_REPLICATION.md` to reflect the full second-revision evidence package, including the XBRL construct-coverage diagnostics, bounded sensitivity decision matrix, independent coding evidence, and checksum manifest.

We also regenerated the checksum manifest and removed stale count references from the package documentation. Pilot, smoke, dry-run, and older `gemma4:latest` artifacts remain separated in `DEPRECATED_OR_PILOT_ARTIFACTS.md` and are explicitly marked as non-authoritative.

## Evidence Locations

- `submission/replication_package/REVIEWER_FILE_MAP.md`
- `submission/replication_package/AUTHORITATIVE_FILES.md`
- `submission/replication_package/README_REPLICATION.md`
- `submission/replication_package/PACKAGE_CONTENTS.md`
- `submission/replication_package/data/processed/checksums/checksum_manifest.csv`
- `submission/replication_package/docs/73_ollama_model_metadata_note.md`
- `submission/replication_package/docs/74_checksum_manifest_package.md`

## Boundary To Preserve

The cleanup improves transparency and file-level reproducibility. It does not convert the package into a model-performance benchmark, an audit-evidence validation package, or a source of population-level inference.
