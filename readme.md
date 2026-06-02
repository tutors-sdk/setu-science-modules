# SETU Module Catalogues

This repository contains module catalogues for various subject areas at SETU, structured for the [Tutors](https://tutors.dev) publishing system.

## Computing

The computing catalogue contains **225 modules** across **12 programmes** organized into **16 subject clusters**.

See [computing/readme.md](computing/readme.md) for full documentation.

### Quick Start

```bash
cd computing

# Install dependencies
pip install -r tutors-generator/requirements.txt

# Generate the catalogue
./generate

# Build and preview with Tutors
cd tutors-catalogue/tutors
deno run -A jsr:@tutors/tutors
```

See [computing/QUICKSTART.md](computing/QUICKSTART.md) for detailed quick start guide.

## Repository Structure

```
setu-comp-sci-modules/
└── computing/
    ├── module-catalogue/      # Source data (YAML, PDFs, images)
    ├── tutors-generator/      # Python generation engine
    ├── tutors-catalogue/      # Generated Tutors output
    ├── generate               # Generation script
    └── readme.md              # Computing catalogue documentation
```

## About

This system transforms structured YAML module data into Tutors-compatible course structures with:
- **Programme view** - Browse modules by programme and semester
- **Cluster view** - Browse modules by subject area
- Detailed module descriptors with learning outcomes, assessments, and content
- PDF archives of official module documents

## Prerequisites

- **Python 3.x** - For catalogue generation
- **Deno** - For Tutors course building ([install from deno.land](https://deno.land/))
