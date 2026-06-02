# Images Subfolder Refactoring

## Change Made

Created `tutors-generator/images/` subfolder and moved all image-related scripts and documentation there.

### Before
```
tutors-generator/
├── generate-catalogue.py
├── copy-flowbite-illustrations.py
├── download-github-illustrations.py
├── download-undraw-images.py
├── requirements.txt
├── GENERATOR_README.md
├── ICONS.md
├── ILLUSTRATIONS_SUMMARY.md
├── UNDRAW_DOWNLOAD_GUIDE.md
└── [other docs]
```

### After
```
tutors-generator/
├── generate-catalogue.py
├── requirements.txt
├── GENERATOR_README.md
├── images/                           # ⭐ NEW subfolder
│   ├── copy-flowbite-illustrations.py
│   ├── download-github-illustrations.py
│   ├── download-undraw-images.py
│   ├── ICONS.md
│   ├── ILLUSTRATIONS_SUMMARY.md
│   ├── UNDRAW_DOWNLOAD_GUIDE.md
│   └── README.md                     # ⭐ NEW guide
└── [other docs]
```

## What Was Moved

### To `tutors-generator/images/`

**Scripts (3 files):**
- ✅ `copy-flowbite-illustrations.py` - Flowbite SVG downloader
- ✅ `download-github-illustrations.py` - GitHub illustrations (deprecated)
- ✅ `download-undraw-images.py` - unDraw downloader

**Documentation (3 files):**
- ✅ `ICONS.md` - Icon guidelines and documentation
- ✅ `ILLUSTRATIONS_SUMMARY.md` - Illustration implementation summary
- ✅ `UNDRAW_DOWNLOAD_GUIDE.md` - Manual unDraw download guide

**New File:**
- ✅ `README.md` - Images folder guide with usage instructions

### Remained in `tutors-generator/`

**Main Generator:**
- `generate-catalogue.py` - Core generator script
- `requirements.txt` - Python dependencies

**Documentation:**
- `GENERATOR_README.md` - Full generator documentation
- `FOLDER_STRUCTURE.md` - Directory structure guide
- `TEST_RESULTS.md` - Test results
- `REFACTORING_SUMMARY.md` - Refactoring notes
- `RENAME_SUMMARY.md` - Rename notes
- `CATALOGUE_ORDER_MOVE.md` - Catalogue order move notes
- `ORGANIZATION_SUMMARY.md` - Organization summary

## Benefits

1. **Better Organization** - Image-related code grouped together
2. **Cleaner Structure** - Main generator folder less cluttered
3. **Clear Purpose** - Easy to find image management tools
4. **Logical Grouping** - Related functionality in one place

## Updated References

### `QUICKSTART.md`
- Updated `tutors-generator/ICONS.md` → `tutors-generator/images/ICONS.md`

### `tutors-generator/ORGANIZATION_SUMMARY.md`
- Updated file structure diagrams
- Updated documentation paths

## Usage

### To Update Images

```bash
# Clone Flowbite repository
git clone https://github.com/themesberg/flowbite-illustrations.git /tmp/flowbite-illustrations

# Run copy script from new location
python3 tutors-generator/images/copy-flowbite-illustrations.py

# Regenerate catalogue
./generate
```

### To View Documentation

```bash
# Image management guide
cat tutors-generator/images/README.md

# Icon documentation
cat tutors-generator/images/ICONS.md

# Illustration details
cat tutors-generator/images/ILLUSTRATIONS_SUMMARY.md

# unDraw guide
cat tutors-generator/images/UNDRAW_DOWNLOAD_GUIDE.md
```

## Current Structure

```
setu-comp-sci-modules/
├── generate                          # Generator command
├── readme.md
├── QUICKSTART.md
│
├── module-catalogue/                 # Source data
│   ├── .catalogue-order.yaml
│   ├── images/                       # Image files
│   │   ├── clusters/                 # Cluster SVGs
│   │   └── programmes/               # Programme SVGs
│   ├── module-icons.yaml             # Icon definitions
│   └── [other source data]
│
├── tutors-catalogue/                 # Generated output
│   ├── tutors/
│   └── tutors-reference/
│
└── tutors-generator/                 # Generator code
    ├── generate-catalogue.py         # Main generator
    ├── requirements.txt
    ├── images/                       # ⭐ Image management
    │   ├── *.py scripts
    │   ├── *.md documentation
    │   └── README.md
    └── *.md (other docs)
```

## Testing

Verified functionality:

```bash
# Generator still works
./generate
# ✅ Success

# Image scripts accessible
ls tutors-generator/images/*.py
# ✅ All scripts present

# Documentation accessible
ls tutors-generator/images/*.md
# ✅ All docs present + README
```

## Image Workflow

### Current Images
The catalogue uses **Flowbite Illustrations** (MIT licensed SVGs):
- 16 cluster images in `module-catalogue/images/clusters/`
- 12 programme images in `module-catalogue/images/programmes/`

### To Update
1. Edit mappings in `tutors-generator/images/copy-flowbite-illustrations.py`
2. Run: `python3 tutors-generator/images/copy-flowbite-illustrations.py`
3. Regenerate: `./generate`

### To Change Icons
1. Edit `module-catalogue/module-icons.yaml`
2. See `tutors-generator/images/ICONS.md` for guidelines
3. Regenerate: `./generate`

## Migration Notes

### If Pulling This Change

After pulling:

1. **Scripts moved** - Image scripts now in `tutors-generator/images/`
2. **Docs moved** - Icon/illustration docs now in `tutors-generator/images/`
3. **New README** - Image folder has its own README.md
4. **Updated paths** - Documentation references updated

### Compatibility

- ✅ Generator unchanged: `./generate` still works
- ✅ Image scripts: New paths but same functionality
- ✅ Documentation: Updated references
- ✅ No workflow changes

## Verification Checklist

- [x] Scripts moved to `images/` subfolder
- [x] Documentation moved to `images/` subfolder
- [x] New `README.md` created in `images/`
- [x] References updated in main docs
- [x] Generator still works: `./generate`
- [x] Structure is cleaner and more organized

---

*Refactoring completed: June 1, 2026*
*All image-related code and docs now in `tutors-generator/images/`*
