# Figure Export Audit

## Source Guide

AAA Manuscript Preparation Guide: https://aaahq.org/Research/Journals/Manuscript-Preparation-Guide

The guide states that figure files may be submitted in EPS, PS, TIFF, PDF, JPEG, or PNG format and that line art should use 600 dpi black/white bitmap graphics.

## Exported Files

| Figure | Source SVG | PNG | PNG Dimensions | PDF |
|---|---|---|---|---|
| Figure 1 | `Figure_1_Retrieval_Environment_Validity.svg` | `Figure_1_Retrieval_Environment_Validity.png` | 3600 x 2940 | `Figure_1_Retrieval_Environment_Validity.pdf` |
| Figure 2 | `Figure_2_Methodological_Demonstration_Pipeline.svg` | `Figure_2_Methodological_Demonstration_Pipeline.png` | 4200 x 3300 | `Figure_2_Methodological_Demonstration_Pipeline.pdf` |

## QA Notes

- PNG files were exported using Microsoft Edge headless from SVG source files.
- PDF files were exported using Microsoft Edge headless print-to-PDF.
- Both PNG files were visually inspected after export.
- Figure 2 was adjusted after inspection to widen the bottom box and prevent tight text placement.
- Edge emitted non-fatal browser warnings during export, but output files were created successfully and visually inspected.

## Upload Recommendation

If the submission system accepts PNG, upload the PNG files as separate figure files. If it requests vector or document format, upload the PDF files. Keep the SVG files as editable source files but do not rely on SVG as the sole upload format unless the system explicitly accepts it.
