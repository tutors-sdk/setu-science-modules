# Image Management Scripts

This directory contains scripts and documentation for managing images and icons in the module catalogue.

## Contents

### Scripts

#### `copy-flowbite-illustrations.py`
Copies MIT-licensed SVG illustrations from the Flowbite Illustrations repository.

**Usage:**
```bash
# Clone Flowbite repo first
git clone https://github.com/themesberg/flowbite-illustrations.git /tmp/flowbite-illustrations

# Run the copy script
python3 copy-flowbite-illustrations.py
```

**Output:**
- Copies SVG files to `module-catalogue/images/clusters/`
- Copies SVG files to `module-catalogue/images/programmes/`

#### `download-github-illustrations.py`
Attempts to download illustrations directly from GitHub (deprecated - use copy script instead).

#### `download-undraw-images.py`
Script for downloading unDraw illustrations (requires manual download via browser).

**Note:** unDraw doesn't have a public API, so use `UNDRAW_DOWNLOAD_GUIDE.md` for manual instructions.

### Documentation

#### `ICONS.md`
Documentation for module icons using Iconify/Lucide/Carbon icon sets.

**Topics:**
- Icon selection guidelines
- How to update module icons in `module-catalogue/module-icons.yaml`
- Available icon sets and how to choose icons
- Color palette recommendations

#### `ILLUSTRATIONS_SUMMARY.md`
Summary of the open-source illustration implementation.

**Topics:**
- Flowbite Illustrations (MIT license)
- Downloaded SVG files mapping
- Image sources and licenses
- Benefits of using SVG format

#### `UNDRAW_DOWNLOAD_GUIDE.md`
Manual guide for downloading unDraw illustrations.

**Topics:**
- Step-by-step download instructions
- Search terms for each cluster and programme
- Color customization (#014771 - SETU blue)
- Filename conventions

## Current Implementation

The catalogue uses **Flowbite Illustrations** (MIT license):
- 16 cluster illustrations
- 12 programme illustrations
- All in SVG format for scalability
- Located in `module-catalogue/images/`

## Quick Start

### To Update Images

1. **Clone Flowbite repository:**
   ```bash
   git clone https://github.com/themesberg/flowbite-illustrations.git /tmp/flowbite-illustrations
   ```

2. **Run copy script:**
   ```bash
   python3 tutors-generator/images/copy-flowbite-illustrations.py
   ```

3. **Regenerate catalogue:**
   ```bash
   ./generate
   ```

### To Change Image Mappings

Edit the mappings in `copy-flowbite-illustrations.py`:

```python
cluster_mappings = {
    "Cluster Name": "flowbite-illustration-name.svg",
    # ...
}

programme_mappings = {
    "PROGRAMME_CODE": "flowbite-illustration-name.svg",
    # ...
}
```

### To Update Icons

Edit `module-catalogue/module-icons.yaml`:

```yaml
A13443:  # Module code
  type: lucide:code
  color: "394B53"
```

See `ICONS.md` for detailed icon documentation.

## Image Locations

### Source Images
```
module-catalogue/images/
├── clusters/          # Cluster topic images (SVG)
│   ├── Automotive_Automation_and_IoT.svg
│   ├── Business.svg
│   └── ...
└── programmes/        # Programme topic images (SVG)
    ├── WD_KINFT_D.svg
    ├── WD_KINTE_B.svg
    └── ...
```

### Generated Output
When running `./generate`, images are copied to:
```
tutors-catalogue/tutors/
├── unit-1-programmes/
│   └── topic-XX-*/topic.svg       # Programme images
└── unit-2-clusters/
    └── topic-XX-*/topic.svg       # Cluster images
```

## Licenses

### Flowbite Illustrations
- **License:** MIT
- **Source:** https://github.com/themesberg/flowbite-illustrations
- **Usage:** Free for commercial and personal use
- **Attribution:** Optional but appreciated

### Icon Sets
Module icons use:
- **Lucide:** ISC License
- **Carbon:** Apache 2.0
- **Iconify:** Various open-source licenses

## Related Files

- `module-catalogue/module-icons.yaml` - Icon definitions for all modules
- `module-catalogue/.catalogue-order.yaml` - Display ordering
- `module-catalogue/images/` - Source image files

## Troubleshooting

### Images not appearing after generation

1. Check source files exist:
   ```bash
   ls module-catalogue/images/clusters/
   ls module-catalogue/images/programmes/
   ```

2. Verify generator copied them:
   ```bash
   find tutors-catalogue/tutors -name "topic.svg" | wc -l
   # Should show 56 files (or similar)
   ```

3. Regenerate:
   ```bash
   ./generate
   ```

### Want to use different images

1. Place new SVG files in:
   - `module-catalogue/images/clusters/<ClusterName>.svg`
   - `module-catalogue/images/programmes/<PROGRAMME_CODE>.svg`

2. Regenerate:
   ```bash
   ./generate
   ```

The generator automatically uses SVG files when available (falls back to PNG/JPEG).

## More Information

- Full generator documentation: `../GENERATOR_README.md`
- Icon guidelines: `ICONS.md`
- Illustration details: `ILLUSTRATIONS_SUMMARY.md`
- unDraw guide: `UNDRAW_DOWNLOAD_GUIDE.md`
