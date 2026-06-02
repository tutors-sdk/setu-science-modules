# Quick Start Guide

## Prerequisites

- **Python 3.x** - For running the catalogue generator
- **Deno** - For building the Tutors course ([install from deno.land](https://deno.land/))

## Installation

```bash
# Install Python dependencies
pip install -r tutors-generator/requirements.txt

# Copy and configure environment variables
cp .env.example .env
# Edit .env if needed to change TUTORS_COURSE_ID
```

## Basic Usage

### Generate to default output (tutors-catalogue/tutors/)
```bash
./generate
```

### Generate to custom output directory
```bash
./generate tutors-catalogue/tutors-custom
```

### Build the Tutors course
After generating the catalogue structure, build it with Tutors:
```bash
cd tutors-catalogue/tutors
deno run -A jsr:@tutors/tutors
```

Or for a test build:
```bash
cd tutors-catalogue/tutors-test
deno run -A jsr:@tutors/tutors
```

## What It Does

Transforms this:
```
module-catalogue/
├── descriptors/yaml/    # Module details
├── modules/yaml/        # Module metadata  
├── programmes/yaml/     # Programme definitions
└── schedules/yaml/      # Semester schedules
```

Into this:
```
tutors-catalogue/tutors/
├── unit-1-programmes/   # Browse by programme & semester
└── unit-2-clusters/     # Browse by subject cluster
```

## Typical Workflow

### After updating source data

```bash
# 1. Edit YAML files in module-catalogue/
vim module-catalogue/descriptors/yaml/A13443.yaml

# 2. Regenerate tutors folder
./generate

# 3. Build the Tutors course
cd tutors
deno run -A jsr:@tutors/tutors

# 4. Review changes
git diff
```

### Testing changes

```bash
# Generate to test folder first
\./generate tutors-test

# Build and test
cd tutors-test
deno run -A jsr:@tutors/tutors
cd ..

# Compare with production
diff -r tutors tutors-test

# If happy, regenerate and build production
\./generate tutors
cd tutors
deno run -A jsr:@tutors/tutors
```

## Files Preserved

The script preserves these files in the output directory:
- `properties.yaml` - Course metadata
- `course.md` - Course overview
- `course.png` - Course image

Everything else is regenerated from source data.

## Common Tasks

### Add a new module

1. Add YAML files:
   - `module-catalogue/modules/yaml/A12345.yaml`
   - `module-catalogue/descriptors/yaml/A12345.yaml`
   - `module-catalogue/descriptors/pdf/A12345.pdf`

2. Add to programme schedule:
   - Edit `module-catalogue/schedules/yaml/WD_XXXXX.yaml`
   - Add module to appropriate semester

3. Regenerate and build:
   ```bash
   \./generate
   cd tutors
   deno run -A jsr:@tutors/tutors
   ```

### Update a module

1. Edit YAML:
   ```bash
   vim module-catalogue/descriptors/yaml/A13443.yaml
   ```

2. Regenerate:
   ```bash
   \./generate
   ```

### Add a new programme

1. Add YAML files:
   - `module-catalogue/programmes/yaml/WD_XXXXX.yaml`
   - `module-catalogue/schedules/yaml/WD_XXXXX.yaml`

2. Regenerate:
   ```bash
   \./generate
   ```

### Change a module's cluster

1. Edit module YAML:
   ```bash
   vim module-catalogue/modules/yaml/A13443.yaml
   ```

2. Change the `subgroup` field:
   ```yaml
   subgroup: New Cluster Name
   ```

3. Regenerate and build:
   ```bash
   \./generate
   cd tutors
   deno run -A jsr:@tutors/tutors
   ```

## Output Statistics

The generator will show:
```
============================================================
SETU Module Catalogue Generator
============================================================
Loading catalogue data...
Loaded 12 programmes, 225 modules
Found 16 clusters

Cleaning output directory...

Generating cluster view...
Generated 16 clusters with modules

Generating programme view...
Generated 12 programmes

Generating JSON exports...
JSON exports directory created

============================================================
Generation complete!
============================================================
```

## Troubleshooting

### Module not appearing

Check:
1. Module has YAML in `modules/yaml/`
2. Module has descriptor in `descriptors/yaml/`
3. Module is in a schedule in `schedules/yaml/`

### Broken links

If weburl links are broken, ensure clusters are generated before programmes (the script does this automatically).

### Missing PDFs

Ensure PDFs exist in `module-catalogue/descriptors/pdf/<CODE>.pdf`

## Customization

### Module Icons

Module icons are defined in `module-catalogue/module-icons.yaml`. See `tutors-generator/images/ICONS.md` for:
- How to choose appropriate icons from Iconify
- Icon selection guidelines
- Color palette recommendations

### Topic Images

Programme and cluster images are in `module-catalogue/images/`:
- `programmes/` - Programme topic images
- `clusters/` - Cluster topic images

See `module-catalogue/images/README.md` for:
- Image guidelines and specifications
- How to add new images
- Current coverage status

## More Information

- Full documentation: See `tutors-generator/GENERATOR_README.md`
- Test results: See `TEST_RESULTS.md`
- Icon documentation: See `tutors-generator/images/ICONS.md`
- Image guidelines: See `module-catalogue/images/README.md`
- Source code: See `tutors-generator/generate-catalogue.py`
