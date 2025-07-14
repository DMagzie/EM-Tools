# LCCA Track – EM Tools (v0.03)

This module supports Life Cycle Cost Analysis (LCCA) for multifamily new construction projects in California. It combines energy model outputs with cost, utility rate, and emissions data.

## 📁 Folder Structure

- **Scripts/** – Python scripts to process and convert energy model data.
- **Inputs/** – Sample input files (energy results, PVWatts, cost data).
- **Outputs/** – Generated outputs from LCCA processing.
- **Docs/** – Documentation and changelogs.
- **Reference/** – Utility rates and cost reference files.

## 🚀 Usage

1. Set up a  file with the following keys:
    ```
    DROPBOX_LCCA_PATH=/Users/<yourname>/Dropbox/EM_LCCA/
    GITHUB_LCCA_REPO=github.com/vca-green/em-lcca
    PVWATTS_API_KEY=your_api_key
    ```

2. Run  from the Scripts/ folder with configured inputs.

## 🔧 Dependencies

Install via pip:

```bash
pip install pandas openpyxl numpy python-dotenv
```

## 🏁 Roadmap

- [x] v0.01: Construction cost + EV energy calc
- [x] v0.03: Functional scripts + dashboard integration
- [ ] v0.04: Full Excel + Python integration
- [ ] v1.0: Public release with UI toggles

