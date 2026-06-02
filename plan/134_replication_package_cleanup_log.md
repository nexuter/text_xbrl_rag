# Replication Package Cleanup Log

## Purpose

This revision implements SR-13 from the second-revision workflow. The objective is to keep the replication package aligned with the manuscript's traceability standard and prevent reviewer confusion about authoritative evidence files, stale counts, model metadata, or deprecated artifacts.

## Implemented Revisions

1. Updated `submission/README_REPLICATION.md` and `submission/replication_package/README_REPLICATION.md`.
2. Added pipeline steps for:
   - context-volume diagnostics;
   - source-environment perturbation diagnostics;
   - bounded sensitivity decision matrix;
   - hybrid integration mechanism diagnostics.
3. Updated expected counts:
   - XBRL construct-coverage filer-construct rows: 18;
   - bounded sensitivity decision-matrix rows: 18;
   - checksum manifest rows: 418.
4. Updated package file references from stale `plan/` paths to current `docs/` paths for model metadata and checksum notes.
5. Updated `submission/replication_package/PACKAGE_CONTENTS.md` to include `REVIEWER_FILE_MAP.md` and current counts.
6. Updated `submission/replication_package/AUTHORITATIVE_FILES.md` to include:
   - independent coding validation sample;
   - hybrid integration mechanism evidence;
   - XBRL construct-coverage diagnostics;
   - retrieval perturbation diagnostics;
   - bounded sensitivity decision matrix;
   - new authoritative scripts.
7. Added `submission/replication_package/REVIEWER_FILE_MAP.md`.
8. Updated `submission/replication_package/docs/74_checksum_manifest_package.md` to match the current checksum manifest.
9. Regenerated the replication-package checksum manifest.

## Verified Counts

| Item | Verified Count |
|---|---:|
| Text chunks | 1,377 |
| XBRL facts | 2,566 |
| XBRL relation paths | 1,619 |
| Retrieval contexts | 72 |
| Retrieval log rows | 464 |
| Main run manifest rows | 24 |
| Extension run manifest rows | 48 |
| Main coded claims | 94 |
| Extension coded claims | 187 |
| Independent coder rows | 240 |
| Retrieval perturbation rows | 90 |
| Bounded sensitivity decision-matrix rows | 18 |
| XBRL construct-coverage filer-construct rows | 18 |
| Hybrid integration mechanism rows | 89 |
| Replication-package checksum manifest rows | 418 |

## Reviewer-Facing Position

The replication package now separates:

1. authoritative manuscript evidence files;
2. reviewer navigation files;
3. deprecated/pilot artifacts;
4. model metadata and checksum notes;
5. source-environment diagnostics and sensitivity outputs.

## Files Revised Or Added

- `submission/README_REPLICATION.md`
- `submission/replication_package/README_REPLICATION.md`
- `submission/replication_package/PACKAGE_CONTENTS.md`
- `submission/replication_package/AUTHORITATIVE_FILES.md`
- `submission/replication_package/REVIEWER_FILE_MAP.md`
- `submission/replication_package/docs/74_checksum_manifest_package.md`
- `submission/replication_package/data/processed/checksums/checksum_manifest.csv`
- `submission/replication_package/data/processed/checksums/checksum_summary.md`
- `plan/112_second_revision_comprehensive_revise_plan.md`

## Remaining Boundary

The package still does not include raw SEC source files by default. Raw sources remain publicly reconstructable using `sec_download.py`, `config/filer_manifest.json`, accession metadata, and SEC EDGAR. The package supports Tier 1 protocol validation, not model-performance validation or audit evidence sufficiency.
