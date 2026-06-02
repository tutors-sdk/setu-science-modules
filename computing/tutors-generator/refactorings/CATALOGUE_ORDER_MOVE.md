# Catalogue Order Configuration Move

## Change Made

Moved `.catalogue-order.yaml` from project root into `module-catalogue/` directory.

### Before
```
setu-comp-sci-modules/
├── .catalogue-order.yaml          # In root
├── module-catalogue/
├── tutors-catalogue/
└── tutors-generator/
```

### After
```
setu-comp-sci-modules/
├── module-catalogue/
│   ├── .catalogue-order.yaml      # ⭐ Moved here
│   ├── descriptors/
│   ├── images/
│   └── ...
├── tutors-catalogue/
└── tutors-generator/
```

## Rationale

The `.catalogue-order.yaml` file defines the ordering of programmes and clusters in the generated catalogue. Since it's configuration data for the module catalogue (not generator code or build configuration), it belongs with the source data in `module-catalogue/`.

**Benefits:**
1. **Logical grouping** - Configuration with the data it configures
2. **Source of truth** - All catalogue source data in one place
3. **Cleaner root** - One less configuration file in project root

## What Was Updated

### 1. **File Moved**
```bash
.catalogue-order.yaml → module-catalogue/.catalogue-order.yaml
```

### 2. **Generator Updated**
`tutors-generator/generate-catalogue.py`:
```python
# Before
order_file = Path(".catalogue-order.yaml")

# After
order_file = self.source_dir / ".catalogue-order.yaml"
```

Now reads from `module-catalogue/.catalogue-order.yaml` automatically.

### 3. **Documentation Updated**
- ✅ `tutors-generator/GENERATOR_README.md`
- ✅ `tutors-generator/FOLDER_STRUCTURE.md`
- ✅ `tutors-generator/ORGANIZATION_SUMMARY.md`

## File Purpose

The `.catalogue-order.yaml` file controls the display order of:
- **Programmes** - Order in unit-1-programmes
- **Clusters** - Order in unit-2-clusters

### Example Content
```yaml
programmes:
  - WD_KINFT_D
  - WD_KINTE_B
  - WD_KCRCO_B
  # ... etc

clusters:
  - "Automotive, Automation and IoT"
  - "Business"
  - "Database and Analytics"
  # ... etc
```

## Usage

No changes to user workflow - the generator automatically finds the file in the new location.

### Generate Catalogue
```bash
./generate
```

The generator reads `module-catalogue/.catalogue-order.yaml` automatically.

### Edit Ordering
```bash
# Edit the file in its new location
vim module-catalogue/.catalogue-order.yaml

# Regenerate
./generate
```

## Current Root Directory

Now only contains essential user-facing files:

```
setu-comp-sci-modules/
├── .env.example                   # Environment template
├── .gitignore                     # Git configuration
├── generate                       # Generator command
├── readme.md                      # Main README
├── QUICKSTART.md                  # Quick start guide
├── module-catalogue/              # Source data ⭐
│   ├── .catalogue-order.yaml      # Ordering config (moved here)
│   └── ...
├── tutors-catalogue/              # Generated output
└── tutors-generator/              # Generator code
```

## Testing

Verified functionality:

```bash
# Generate catalogue
./generate
# ✅ Successfully reads module-catalogue/.catalogue-order.yaml
# ✅ Programmes and clusters in correct order

# Check file location
ls module-catalogue/.catalogue-order.yaml
# ✅ File exists in new location

# Check root
ls -la | grep catalogue-order
# ✅ No file in root (moved)
```

## Migration Notes

### If Pulling This Change

After pulling:

1. **File moved** - `.catalogue-order.yaml` now in `module-catalogue/`
2. **Generator updated** - Automatically reads from new location
3. **No action needed** - Just pull and continue working

### To Edit Ordering

```bash
# Old location (no longer used)
vim .catalogue-order.yaml

# New location
vim module-catalogue/.catalogue-order.yaml
```

## Verification Checklist

- [x] File moved to `module-catalogue/.catalogue-order.yaml`
- [x] Generator updated to read from new location
- [x] `./generate` runs successfully
- [x] Programmes and clusters in correct order
- [x] Documentation updated
- [x] Root directory cleaner

---

*Move completed: June 1, 2026*
*`.catalogue-order.yaml` now in `module-catalogue/` with other source data*
