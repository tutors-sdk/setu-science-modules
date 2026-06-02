SETU Module Catalogue

This is a system for the generation of a module catalogue for SETU Computing department.

## Source of Truth

The "source of truth" is in the `module-catalogue` directory:

- `module-catalogue/descriptors/` - Detailed module descriptors (YAML + PDF)
- `module-catalogue/modules/` - Module metadata and cluster assignments
- `module-catalogue/programmes/` - Programme definitions
- `module-catalogue/schedules/` - Semester schedules for each programme

## Generation

The catalogue is generated using the `generate` script:

```bash
# Install dependencies
pip install -r tutors-generator/requirements.txt

# Generate the catalogue structure
./generate

# Build the Tutors course
cd tutors-catalogue/tutors
deno run -A jsr:@tutors/tutors
```

See `QUICKSTART.md` for quick start guide or `tutors-generator/GENERATOR_README.md` for full documentation.

## Output

The publication of the catalogue via the Tutors generation system is documented here:

- https://tutors-reference-manual.netlify.app/llms/tutors-reference-manual-complete-llms.txt

The generated output is in the `tutors-catalogue/tutors` directory:

- `tutors-catalogue/tutors/unit-1-programmes/` - Browse modules by programme and semester
- `tutors-catalogue/tutors/unit-2-clusters/` - Browse modules by subject cluster

**Note:** The `tutors-catalogue/tutors-reference/` directory contains the reference implementation for comparison.

## Statistics

- 12 Programmes
- 225 Modules
- 16 Subject Clusters

## Complete Workflow

```bash
# 1. Edit source data
vim module-catalogue/descriptors/yaml/A13443.yaml

# 2. Generate catalogue structure
./generate

# 3. Build Tutors course
cd tutors-catalogue/tutors
deno run -A jsr:@tutors/tutors

# 4. Preview/deploy the generated site
```

## Prerequisites

- Python 3.x with PyYAML and python-dotenv
- Deno ([install from deno.land](https://deno.land/))

## Configuration

The generator uses a `.env` file for configuration. Copy the example file and adjust as needed:

```bash
cp .env.example .env
```

Configuration options:
- `TUTORS_COURSE_ID` - The course identifier used in weburl paths (default: `setu-comp-sci-modules-md`)


