# SETU Module Catalogue Generator

This script generates the `tutors` folder structure from the `module-catalogue` source data.

## Overview

The generator transforms structured YAML data into a Tutors-compatible course structure with:

1. **Programme-based view** (`unit-1-programmes/`) - Modules organized by academic programme and semester
2. **Cluster-based view** (`unit-2-clusters/`) - Modules organized by subject area clusters

## Source Data Structure

The `module-catalogue/` directory contains:

```
module-catalogue/
├── descriptors/
│   ├── yaml/          # Detailed module descriptors (aims, outcomes, assessments)
│   └── pdf/           # Official PDF module documents
├── modules/
│   └── yaml/          # Module metadata (author, cluster, programmes)
├── programmes/
│   └── yaml/          # Programme definitions (name, leader, structure)
├── schedules/
│   └── yaml/          # Semester schedules for each programme
├── images/
│   ├── programmes/    # Topic images for programmes
│   └── clusters/      # Topic images for clusters
├── module-icons.yaml  # Icon mappings for all modules
└── \.catalogue-order.yaml  # Display order for programmes and clusters
```

## Output Structure

The `tutors-catalogue/tutors/` directory is generated with:

```
tutors-catalogue/tutors/
├── properties.yaml              # Course-level properties (preserved)
├── course.md                    # Course overview (preserved)
├── course.png                   # Course image (preserved)
├── unit-1-programmes/           # Generated: Programme view
│   ├── topic.md
│   └── topic-XX-<PROG_CODE>/
│       ├── topic.md            # Programme overview
│       └── unit-N/             # Semester N
│           ├── topic.md        # Semester overview
│           └── web-XX-web-XX-<MODULE>/
│               ├── link.md     # Module link with icon
│               └── weburl      # Link to cluster-based note
└── unit-2-clusters/             # Generated: Cluster view
    ├── topic.md
    └── topic-XX-<CLUSTER>/
        ├── topic.md            # Cluster overview
        └── note-XX-note-XX-<MODULE>/
            ├── note.md         # Full module documentation
            └── archives/
                └── <CODE>.pdf  # Module PDF descriptor
```

## How the Transformation Works

### 1. Programmes → unit-1-programmes

For each programme in `programmes/yaml/`:
- Creates a topic folder: `topic-XX-<PROG_CODE>/`
- Reads corresponding schedule from `schedules/yaml/<PROG_CODE>.yaml`
- For each semester (1 to num_stages * 2):
  - Creates `unit-N/` folder
  - For each mandatory module in that semester:
    - Creates `web-XX-web-XX-<MODULE_NAME>/` folder
    - Generates `link.md` with module title and icon
    - Generates `weburl` pointing to the corresponding cluster note

### 2. Clusters → unit-2-clusters

Clusters are derived from the `subgroup` field in `modules/yaml/`:
- Groups modules by their subgroup/cluster
- For each cluster:
  - Creates `topic-XX-<CLUSTER_NAME>/` folder
  - For each module in the cluster:
    - Creates `note-XX-note-XX-<MODULE_NAME>/` folder
    - Generates comprehensive `note.md` from descriptor data:
      - Module information table
      - Aims and learning outcomes
      - Indicative content
      - Teaching methods and contact hours
      - Assessment methods and criteria
      - Prerequisites and reading materials
      - Programme associations
    - Copies PDF from `descriptors/pdf/` to `archives/`

### 3. Module Markdown Generation

Each module note contains sections generated from descriptor YAML:
- **Module Information**: Code, title, credits, level, department, author, cluster
- **Module Aim**: Overall purpose and context
- **Learning Outcomes**: What students will be able to do
- **Indicative Content**: Topics covered
- **Learning and Teaching Methods**: Delivery approach + contact hours table
- **Assessment Methods**: Types, learning outcomes covered, weightings
- **Assessment Criteria**: Grade boundaries and expectations
- **Pre-requisites and Co-requisites**: Dependencies
- **Recommended Reading**: Supplementary materials
- **Programme Information**: Which programmes use this module
- **Resources Required**: Special requirements (e.g., computer labs)

## Usage

### Prerequisites

**Python 3.x** - For running the catalogue generator

Install Python dependencies:

```bash
pip install -r requirements.txt
```

**Deno** - For building the Tutors course

Install from [deno.land](https://deno.land/)

### Configuration

The generator uses environment variables from a `.env` file:

```bash
# Copy the example configuration
cp .env.example .env
```

Configuration variables:
- `TUTORS_COURSE_ID` - The course identifier used in weburl paths (default: `setu-comp-sci-modules-md`)

This ID appears in the paths generated for module links in programmes:
```
/note/{TUTORS_COURSE_ID}/unit-2-clusters/topic-XX-{cluster}/{note}
```

### Running the Generator

From the project root:

```bash
python3 generate-catalogue.py
```

Or:

```bash
./generate-catalogue.py
```

### Building the Tutors Course

After generating the catalogue structure:

```bash
cd tutors-catalogue/tutors
deno run -A jsr:@tutors/tutors
```

This builds the static Tutors site from the markdown structure.

### What Gets Preserved

The script preserves these files in the output directory:
- `properties.yaml` - Course metadata (copied from `tutors-catalogue/tutors-reference/` if available)
- `course.md` - Course overview text (copied from `tutors-catalogue/tutors-reference/` if available)
- `course.png` - Course banner image (copied from `tutors-catalogue/tutors-reference/` if available)

If these files don't exist in `tutors-catalogue/tutors-reference/`, defaults are created.

All other content is regenerated from the source data.

**Note:** The `tutors-catalogue/tutors-reference/` directory contains the original reference implementation used for extracting icons, images, and default course files.

## Customization

### Adding New Clusters

Clusters are automatically discovered from the `subgroup` field in module YAML files. To add a new cluster, simply assign modules to it in `modules/yaml/*.yaml`:

```yaml
subgroup: Your New Cluster Name
```

### Module Icons

Icons in module notes use Carbon icons. To change:
Edit the icon section in `generate_module_markdown()`:

```python
md.append("icon:")
md.append("  type: carbon:sys-provision")  # Change icon type here
md.append("  color: 014771")               # Change color here
```

### Module Link Icons

Icons in programme web links use Lucide icons. To change:
Edit in `generate_programmes()`:

```python
f.write("icon:\n")
f.write("  type: lucide:presentation\n")  # Change icon type
f.write("  color: 394B53\n")              # Change color
```

## Data Flow

```
module-catalogue/
    programmes/yaml/ ─────┐
    schedules/yaml/  ─────┤
    modules/yaml/    ─────┼──→ CatalogueGenerator ──→ tutors-catalogue/tutors/
    descriptors/yaml/─────┤                             ├── unit-1-programmes/
    descriptors/pdf/ ─────┘                             └── unit-2-clusters/
```

## Troubleshooting

### Missing modules in output

Check that:
1. Module has a YAML file in `modules/yaml/`
2. Module has a descriptor in `descriptors/yaml/`
3. Module is referenced in a schedule in `schedules/yaml/`

### Broken web links in programmes

The script generates `weburl` paths pointing to cluster notes. If clusters are reorganized, the path generation logic in `generate_programmes()` needs updating.

### PDF not appearing

Ensure the PDF exists in `module-catalogue/descriptors/pdf/<CODE>.pdf` with the correct module code.

## Development

### Key Classes and Methods

- `CatalogueGenerator`: Main orchestrator
  - `load_data()`: Loads all YAML files into memory
  - `generate_programmes()`: Creates programme-based view
  - `generate_clusters()`: Creates cluster-based view
  - `generate_module_markdown()`: Converts descriptor to markdown
  - `sanitize_filename()`: Makes safe filesystem names

### Adding New Features

To add new output formats:
1. Add a new method like `generate_xyz()`
2. Call it from `generate()` main method
3. Use `self.programmes`, `self.modules`, `self.descriptors`, `self.schedules` data

## License

Part of the SETU Computing Module Catalogue system.
