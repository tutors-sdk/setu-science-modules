# Directory Rename Summary

## Changes Made

Renamed `module_catalogue` to `module-catalogue` for consistency with kebab-case naming convention.

### Before
```
setu-comp-sci-modules/
├── module_catalogue/        # Underscore
├── tutors-catalogue/        # Hyphen
└── [scripts and docs]
```

### After
```
setu-comp-sci-modules/
├── module-catalogue/        # Hyphen (consistent)
├── tutors-catalogue/        # Hyphen
└── [scripts and docs]
```

## What Was Updated

### 1. **Directory Renamed**
```bash
module_catalogue/ → module-catalogue/
```

### 2. **Python Scripts Updated**
All references updated from `module_catalogue` to `module-catalogue`:
- ✅ `generate-catalogue.py`
- ✅ `copy-flowbite-illustrations.py`
- ✅ `download-github-illustrations.py`
- ✅ `download-undraw-images.py`

### 3. **Documentation Updated**
All references updated in:
- ✅ `readme.md`
- ✅ `GENERATOR_README.md`
- ✅ `QUICKSTART.md`
- ✅ `FOLDER_STRUCTURE.md`
- ✅ `REFACTORING_SUMMARY.md`
- ✅ `ICONS.md`
- ✅ `TEST_RESULTS.md`
- ✅ `UNDRAW_DOWNLOAD_GUIDE.md`
- ✅ `ILLUSTRATIONS_SUMMARY.md`

## Benefits

1. **Consistent Naming** - All directories now use kebab-case (hyphens)
2. **Convention Compliance** - Follows common Unix/web naming conventions
3. **Better Readability** - Hyphens are more readable than underscores in paths

## Testing

All functionality verified:
```bash
# Generate catalogue
python3 generate-catalogue.py
# ✅ Reads from: module-catalogue/
# ✅ Outputs to: tutors-catalogue/tutors/

# Build with Deno
cd tutors-catalogue/tutors
deno run -A jsr:@tutors/tutors
# ✅ Build successful
```

## Current Directory Structure

```
setu-comp-sci-modules/
├── module-catalogue/               # Source data (kebab-case)
│   ├── descriptors/
│   ├── images/
│   ├── modules/
│   ├── programmes/
│   ├── schedules/
│   └── module-icons.yaml
├── tutors-catalogue/               # Output (kebab-case)
│   ├── tutors/                     # Generated
│   └── tutors-reference/           # Reference
├── generate-catalogue.py
└── [other scripts and docs]
```

## Migration Notes

### If Pulling This Change

After pulling:

1. **Directory renamed** - `module_catalogue/` is now `module-catalogue/`
2. **Scripts updated** - All scripts already reference the new name
3. **No action needed** - Just pull and continue working

### Compatibility

- ✅ All scripts work with new name
- ✅ Generator defaults updated
- ✅ Documentation updated
- ✅ No breaking changes to workflow

## Files Modified

### Python Scripts (4 files)
- `generate-catalogue.py`
- `copy-flowbite-illustrations.py`
- `download-github-illustrations.py`
- `download-undraw-images.py`

### Documentation (9 files)
- `readme.md`
- `GENERATOR_README.md`
- `QUICKSTART.md`
- `FOLDER_STRUCTURE.md`
- `REFACTORING_SUMMARY.md`
- `ICONS.md`
- `TEST_RESULTS.md`
- `UNDRAW_DOWNLOAD_GUIDE.md`
- `ILLUSTRATIONS_SUMMARY.md`

## Verification Checklist

- [x] Directory renamed: `module_catalogue` → `module-catalogue`
- [x] Generator script updated and tested
- [x] Helper scripts updated
- [x] All documentation updated
- [x] Generator runs successfully
- [x] Deno build works
- [x] All references updated
- [x] No broken paths

---

*Rename completed: June 1, 2026*
*All directories now use consistent kebab-case naming*
