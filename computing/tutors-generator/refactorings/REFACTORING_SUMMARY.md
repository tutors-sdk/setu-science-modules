# Folder Refactoring Summary

## Changes Made

Reorganized the tutors-related directories into a single parent folder for better organization.

### Before
```
setu-comp-sci-modules/
├── module-catalogue/
├── tutors/                  # Generated output
├── tutors-reference/        # Reference implementation
└── [scripts and docs]
```

### After
```
setu-comp-sci-modules/
├── module-catalogue/
├── tutors-catalogue/        # New parent folder
│   ├── tutors/              # Generated output (moved)
│   └── tutors-reference/    # Reference implementation (moved)
└── [scripts and docs]
```

## What Was Updated

### 1. **Directory Structure**
- Created `tutors-catalogue/` folder
- Moved `tutors/` → `tutors-catalogue/tutors/`
- Moved `tutors-reference/` → `tutors-catalogue/tutors-reference/`

### 2. **Generator Script** (`generate-catalogue.py`)
- Default output path: `"tutors"` → `"tutors-catalogue/tutors"`
- Reference path: `"tutors-reference"` → `"tutors-catalogue/tutors-reference"`

### 3. **Documentation Updated**
- ✅ `readme.md` - Updated all paths and examples
- ✅ `GENERATOR_README.md` - Updated output paths and reference paths
- ✅ `QUICKSTART.md` - Updated all workflow examples
- ✅ `FOLDER_STRUCTURE.md` - Updated directory structure and all references
- ✅ `ILLUSTRATIONS_SUMMARY.md` - Updated build commands

### 4. **Git Configuration**
- Updated `.gitignore`:
  - `tutors-test` → `tutors-catalogue/tutors-test`
  - Added `/tmp/flowbite-illustrations`

## Benefits

1. **Better Organization** - All tutors-related output in one place
2. **Cleaner Root** - Fewer top-level directories
3. **Logical Grouping** - Generated and reference implementations together
4. **Future-Proof** - Easy to add more tutors variants (e.g., tutors-test, tutors-preview)

## Testing

All functionality verified:
```bash
# Generate catalogue
python3 generate-catalogue.py
# ✅ Output: tutors-catalogue/tutors/

# Build with Deno
cd tutors-catalogue/tutors
deno run -A jsr:@tutors/tutors
# ✅ Build successful

# Check structure
ls tutors-catalogue/
# ✅ Shows: tutors/ and tutors-reference/
```

## Usage Examples

### Generate and Build
```bash
# Generate to default location
python3 generate-catalogue.py

# Build the course
cd tutors-catalogue/tutors
deno run -A jsr:@tutors/tutors
```

### Generate to Test Location
```bash
# Generate to test folder
python3 generate-catalogue.py tutors-catalogue/tutors-test

# Build test version
cd tutors-catalogue/tutors-test
deno run -A jsr:@tutors/tutors

# Compare with reference
diff -r tutors-catalogue/tutors-reference tutors-catalogue/tutors-test
```

### Custom Output
```bash
# You can still specify custom paths
python3 generate-catalogue.py custom-output-dir
```

## Migration Notes

### If Pulling This Change

After pulling these changes:

1. **Old directories are moved** - If you had local `tutors/` or `tutors-reference/`, they're now in `tutors-catalogue/`

2. **Scripts still work** - The generator defaults to the new location automatically

3. **Build commands changed** - Update your local scripts:
   ```bash
   # OLD
   cd tutors && deno run -A jsr:@tutors/tutors
   
   # NEW
   cd tutors-catalogue/tutors && deno run -A jsr:@tutors/tutors
   ```

4. **Regenerate if needed**:
   ```bash
   python3 generate-catalogue.py
   cd tutors-catalogue/tutors
   deno run -A jsr:@tutors/tutors
   ```

## No Breaking Changes

- ✅ Generator still works with default `python3 generate-catalogue.py`
- ✅ Can still specify custom output paths
- ✅ All source data in `module-catalogue/` unchanged
- ✅ All scripts and tools still functional

## Files Modified

- `generate-catalogue.py` - Updated default paths
- `readme.md` - Updated documentation
- `GENERATOR_README.md` - Updated documentation
- `QUICKSTART.md` - Updated examples
- `FOLDER_STRUCTURE.md` - Updated structure docs
- `.gitignore` - Updated ignore paths

## Verification Checklist

- [x] Generator runs successfully
- [x] Output goes to `tutors-catalogue/tutors/`
- [x] Reference files copied from `tutors-catalogue/tutors-reference/`
- [x] Deno build works in new location
- [x] SVG images present in generated output
- [x] All documentation updated
- [x] `.gitignore` updated

---

*Refactoring completed: June 1, 2026*
*All tutors directories now under `tutors-catalogue/` parent folder*
