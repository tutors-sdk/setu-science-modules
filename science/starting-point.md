  Analysis: Science Module Catalogue Folder

  The science folder contains a partial implementation of the module catalogue system - it has source data but lacks the generation infrastructure.

  Current State

  What EXISTS ✓
  - module-catalogue/descriptors/ directory with 636 modules (YAML + PDF)
    - 636 YAML descriptors
    - 636 PDF documents

  What's MISSING ✗
  - No tutors-generator/ directory
  - No generator script (generate)
  - No modules/ directory (module metadata)
  - No programmes/ directory (programme definitions)
  - No schedules/ directory (semester schedules)
  - No images/ directory (topic images)
  - No module-icons.yaml (icon mappings)
  - No .catalogue-order.yaml (ordering configuration)
  - No tutors-catalogue/ output directory

  Data Structure Differences

  Science YAML schema (different from computing):
  reference: A00914          # (vs 'code' in computing)
  full_title: ...            # (vs 'full title' with space)
  short_title: ...           # (vs 'short title' with space)
  author: KGRENNAN          # (staff code, not full name)
  school: Science and Computing
  department: Science
  cluster: Mathematics and Physics
  programmes:               # Embedded in descriptor
    - timetable: STAT-0052
      code: WD_SANSC_G
      name: "..."
      stage: 1
      semester: 0
      status: E
  prerequisites: []         # (vs 'pre-requisites')
  corequisites: []         # (vs 'co-requisites')
  learning_outcomes: []    # (vs 'learning outcomes')
  assessment_methods: []   # (vs 'assessment methods')
  mlo_to_po: ''           # Module LO to Programme Outcome mapping
  track_changes: true
  history_comment: ''

  Key differences:
  - Underscore naming (learning_outcomes vs learning outcomes)
  - Single-file model: Programmes embedded in descriptors, not separate files
  - No separate module metadata files (modules/yaml/ doesn't exist)
  - Additional fields: school, history_comment, mlo_to_po, track_changes
  - Different field names: reference vs code, prerequisites vs pre-requisites

  Coverage & Scope

  Modules: 636 (vs 225 in computing)
  Programmes: ~130 unique programme codes (vs 12 in computing)
  Clusters: 37 (vs 16 in computing)

  Schools:
  - Science and Computing
  - Engineering
  - Humanities

  Departments: 13 different departments including:
  - Science
  - Computing and Mathematics (overlap with computing!)
  - Engineering Technology
  - Land Sciences
  - Sport and Exercise Science
  - Adult Continuing Education
  - Management and Organisation
  - Law and Criminal Justice Studies
  - etc.

  Levels:
  - Introductory
  - Intermediate
  - Advanced
  - Postgraduate

  Module Overlap

  223 modules appear in BOTH datasets (99% of computing modules)

  This means:
  - Computing's 225 modules are a subset of Science's 636
  - The same modules exist with different YAML schemas
  - Science represents the institutional master database
  - Computing is a focused view for the Computing department

  Sample Clusters (Science-specific)

  Science has 21 additional clusters not in computing:
  - Agriculture, AgriFoodICT
  - Analytical Science
  - Biology, Chemistry
  - Environmental Science, Forestry, Horticulture
  - Food Science
  - Pharmaceutical Science
  - Quality, Regulatory and Compliance
  - Placement and Projects
  - English Language
  - Science and Mathematics
  - etc.

  What This Means

  The science folder is:

  1. Institutional-level data - All SETU modules across all faculties
  2. Different source format - Uses underscored field names, single-file design
  3. Incomplete for generation - Has descriptors but lacks:
    - Generator script
    - Programme/schedule structure files
    - Metadata separation (cluster assignments in descriptors)
    - Images and icons
    - Output structure

  Migration Challenge

  To generate a Tutors catalogue from the science data would require:

  1. Schema transformation:
    - Convert underscore fields to space/hyphenated (learning_outcomes → learning outcomes)
    - Map reference → code
    - Extract embedded programme info
  2. Data extraction:
    - Extract unique programmes from embedded data
    - Build separate programme definition files
    - Build semester schedule files
    - Extract cluster assignments into separate module metadata
  3. Generator adaptation:
    - Modify generate-catalogue.py to handle science schema
    - Or transform science YAML to computing schema first
  4. Enrichment:
    - Add icon mappings for 636 modules
    - Add topic images for 37 clusters + 130 programmes
    - Define catalogue ordering

  Summary

  The science folder contains raw institutional data (636 modules, 130 programmes, 37 clusters) in a different YAML schema than computing, but lacks the
  full infrastructure (generator, metadata files, images, icons) needed to produce a Tutors catalogue. It represents the master dataset with
  computing's modules being a curated subset adapted to the generation system.