# SETU Science Module Catalogue

This system generates a Tutors-based module catalogue from SETU's institutional science module database.

## Overview

The science catalogue contains **636 modules** across **37 subject clusters**, covering all SETU programmes including:
- Agriculture, Forestry, Horticulture
- Analytical Science, Chemistry, Biology
- Food Science, Pharmaceutical Science
- Engineering, Electronics, Electrical Engineering
- Computing, IT, Data Communications
- Business, Professional Skills
- And more...

## Source Data

The `module-catalogue/` directory contains:

```
module-catalogue/
├── descriptors/
│   ├── yaml/    # 636 module descriptors (YAML)
│   └── pdf/     # 636 module PDFs
```

## Generated Output: tutors-modules-master

A dual-view Tutors course with:
- **All Modules view** - 636 modules alphabetically with web links
- **Clusters view** - 37 subject clusters with 636 module notes
- **636 PDF archives** attached to each module
- **Icon support** - Reuses 225 icons from computing + 37 cluster icons

## Generation

### Prerequisites

```bash
pip install pyyaml
```

### Generate the catalogue

```bash
./generate-master
```

This creates `tutors-modules-master/` with the complete cluster-based module catalogue.

### Build with Tutors

```bash
cd tutors-modules-master
deno run -A jsr:@tutors/tutors
```

## Data Schema

Science modules use a different YAML schema than computing:

```yaml
reference: A00914              # Module code
full_title: "..."              # Full module name
short_title: "..."             # Short name
credits: 10
level: Postgraduate            # Introductory/Intermediate/Advanced/Postgraduate
author: KGRENNAN              # Staff code
school: Science and Computing
department: Science
cluster: Mathematics and Physics
aim: "..."
programmes:                    # Embedded programme info
  - code: WD_SANSC_G
    name: "..."
    stage: 1
    semester: 0
    status: E                  # M=Mandatory, E=Elective
learning_outcomes: [...]       # Underscore naming
assessment_methods: [...]
learning_and_teaching_methods: [...]
learning_modes: [...]
indicative_content: [...]
assessment_criteria: [...]
prerequisites: []
corequisites: []
essential_material: [...]
supplementary_material: [...]
requested_resources: [...]
```

## Output Structure

```
tutors-modules-master/
├── properties.yaml               # Course metadata
├── course.md                     # Course overview
├── topic.md                      # Root topic
├── topic-01-all-modules/         # All modules alphabetically
│   ├── topic.md
│   └── web-XXX-web-XXX-{module}/ # 636 web objects
│       ├── link.md               # Title + icon + summary
│       └── weburl                # → cluster note
└── topic-02-clusters/            # Modules by cluster
    ├── topic.md
    └── topic-XX-{cluster}/       # 37 clusters
        ├── topic.md
        └── note-XX-note-XX-{module}/
            ├── note.md           # Full descriptor (master)
            └── archives/
                └── {code}.pdf    # Module PDF
```

## Statistics

- **Modules**: 636
- **Clusters**: 37
- **Programmes**: ~130
- **Schools**: 3 (Science and Computing, Engineering, Humanities)
- **Departments**: 13

## Icons

### Module Icons

Icons are applied using a 3-tier priority system:

1. **Module-specific icons** - From computing catalogue (225 modules)
2. **Cluster icons** - Inherited from cluster (411 modules)
3. **Default icon** - `carbon:sys-provision` fallback

### Cluster Icons

All 37 clusters have custom icons defined in `tutors-generator/cluster-icons.yaml`:

```yaml
Biology:
  type: mdi:dna
  color: '00897B'
  description: Biological sciences

"Food Science":
  type: mdi:food-apple-outline
  color: 'EF5350'
  description: Food technology and nutrition
```

See `tutors-generator/CLUSTER_ICONS.md` for complete icon documentation.

## Cluster Coverage

<details>
<summary>Full list of 37 clusters</summary>

1. AgriFoodICT
2. Agriculture
3. Analytical Science
4. Automotive, Automation and IoT
5. Biology
6. Business
7. Chemistry
8. Creativity and Innovation
9. Data Communications
10. Database and Analytics
11. Discipline Specific Technologies
12. Electrical Engineering
13. Electronics
14. Engineering
15. Engineering Practise
16. English Language
17. Environmental Science
18. Food Science
19. Forensics and Security
20. Forestry
21. Game Development
22. Graphic Design and Animation
23. Horticulture
24. Humanities
25. IT
26. Information Systems and Modelling
27. Mathematics and Physics
28. Media Production
29. Networks and Cloud
30. Pharmaceutical Science
31. Placement and Projects
32. Professional Skills
33. Quality, Regulatory and Compliance
34. Science and Mathematics
35. Software and Information Systems
36. Software and Web Development
37. Sports Technology

</details>

## Comparison with Computing Catalogue

| Aspect | Computing | Science |
|--------|-----------|---------|
| Modules | 225 | 636 |
| Clusters | 16 | 37 |
| Programmes | 12 | ~130 |
| Views | 2 (programmes + clusters) | 1 (clusters only) |
| YAML Schema | Space/hyphen naming | Underscore naming |
| Icon Coverage | 100% custom | 35% reused + defaults |

**Overlap**: 223 modules (99% of computing) appear in both catalogues.

## Implementation Notes

The generator (`tutors-generator/generate-master.py`) adapts the computing catalogue generator to:
- Handle underscore field naming (`learning_outcomes` vs `learning outcomes`)
- Extract cluster assignments from descriptor files (no separate module metadata)
- Reuse computing icons for overlapping modules
- Support the science-specific schema extensions (school, department, etc.)
- Generate cluster-only view (no programme/schedule structure needed)

## Related

See `../computing/` for the Computing department's dual-view catalogue (programmes + clusters) generated from a curated subset of modules.
