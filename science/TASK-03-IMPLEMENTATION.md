# Task-03-Programmes Implementation Summary

## Overview

Successfully implemented task-3-programmes, adding a complete programmes view with semester organization and web links to cluster notes.

## What Was Built

### Structure Created

```
tutors-modules-master/
└── topic-03-programmes/
    ├── topic.md ("Programmes" - with school icon)
    └── topic-XX-{PROG_CODE}/
        ├── topic.md (Programme name with education icon)
        └── unit-{semester}/
            ├── topic.md (Semester N)
            └── web-XXX-{module}/
                ├── link.md (icon + title + summary)
                └── weburl (→ cluster note)
```

### Statistics

- **111 programmes** generated
- **443 semester units** across all programmes
- **2,132 web objects** (module links)
- Average: 4.0 semesters and 19.2 modules per programme

## Technical Implementation

### 1. Data Extraction (`extract_programmes` method)

Extracts programme information from embedded data in module descriptors:

```python
def extract_programmes(self):
    # For each module descriptor:
    #   - Extract programme code, name
    #   - Extract semester assignments
    #   - Build programme → semester → modules mapping
    #   - Filter out programmes with no semester data
```

**Data extracted:**
- Programme code (e.g., `WD_KCRCO_B`)
- Programme name
- Semester numbers
- Module assignments per semester
- Module status (M=Mandatory, E=Elective)

**Result:** 111 programmes with semester data (out of 130 total programmes in descriptors)

### 2. Programme Generation (`generate_programmes` method)

**Process:**
1. Create `topic-03-programmes/` container with school icon
2. Sort programmes alphabetically by name
3. For each programme:
   - Create programme topic directory
   - Add `topic.md` with programme name and education icon
   - For each semester with modules:
     - Create `unit-{N}/` directory
     - Add semester `topic.md`
     - Generate web objects for all modules

**Web Object Creation:**
- Same pattern as `topic-01-all-modules`
- `link.md`: icon frontmatter + title + first sentence of aim
- `weburl`: path to cluster note
- Icons: module-specific > cluster > default

### 3. Icon Strategy

**Programmes topic:**
```yaml
icon:
  type: mdi:school
  color: 2E7D32  # green
```

**Each programme:**
```yaml
icon:
  type: mdi:book-education
  color: 455A64  # grey (default)
```

**Module web objects:**
- Inherit from module-specific icons (225)
- Or inherit from cluster icons (rest)
- Same 3-tier priority as all-modules view

## Sample Programme: BSc Creative Computing

**Code:** `WD_KCRCO_B`

**Structure:**
```
topic-05-WD_KCRCO_B/
├── topic.md
├── unit-1/ (6 modules)
├── unit-2/ (6 modules)
├── unit-3/ (6 modules)
├── unit-4/ (6 modules)
├── unit-5/ (1 module + electives)
├── unit-6/ (6 modules)
├── unit-7/ (4 mandatory + 1 elective)
└── unit-8/ (2 mandatory + 3 electives)
```

**Sample web object:**
```
unit-1/web-01-web-01-Introduction_to_Creative_Media/
├── link.md
└── weburl
```

**WebURL:**
```
/note/setu-sci-modules/topic-02-clusters/topic-28-Media_Production/note-10-Introduction_to_Creative_Media
```

## Code Changes

### Modified Files

**`tutors-generator/generate-master.py`:**

1. **Added to `__init__`:**
   ```python
   self.programmes = {}  # Maps programme code to info/modules
   ```

2. **Added to `load_data`:**
   ```python
   self.extract_programmes()
   ```

3. **New method: `extract_programmes()`**
   - Extracts programmes from descriptors
   - Builds programme → semester → modules mapping
   - Filters programmes with no semester data

4. **New method: `generate_programmes()`**
   - Creates topic-03-programmes structure
   - Generates programme topics
   - Creates semester units
   - Generates web objects with icons

5. **Updated `generate()` method:**
   ```python
   self.generate_programmes()  # Added after all-modules
   ```

## Programmes Generated

Sample programmes (alphabetically):
1. BSc (Hons) in Creative Computing - 8 semesters
2. BSc (Hons) in Food Science and Innovation - multiple semesters
3. Master of Science in Analytical Science - multiple semesters
4. Postgraduate diplomas and certificates
5. Bachelor programmes across all faculties

**Total:** 111 programmes with structured semester data

## Comparison with Computing

| Aspect | Computing | Science |
|--------|-----------|---------|
| Programmes | 12 | 111 |
| Data Source | Separate files | Embedded in descriptors |
| Programme files | Yes (yaml) | No (extracted) |
| Schedule files | Yes (yaml) | No (extracted) |
| Semester units | Present | Present |
| Web objects | Links to clusters | Links to clusters |
| Icons | Custom per programme | Default (customizable) |

## Missing Elements (TODO)

The following are marked as TODO in programme topic.md files:

- **Programme leader names** - not available in descriptors
- **Programme-level images** - no SVG/PNG files
- **Custom programme icons** - using defaults (can be added later)

These can be added later if the data becomes available.

## Navigation Flow

Users can now browse modules three ways:

1. **Alphabetical** → topic-01-all-modules → web object → cluster note
2. **By Cluster** → topic-02-clusters → cluster topic → module note
3. **By Programme** → topic-03-programmes → programme → semester → web object → cluster note

All paths lead to the same master notes in `topic-02-clusters`.

## Benefits

✅ **No duplication** - Single master copy of each note  
✅ **Three views** - Alphabetical, clustered, and by programme  
✅ **Contextual organization** - See modules in programme/semester context  
✅ **Consistent linking** - All use same weburl to cluster notes  
✅ **Icon consistency** - Same icons across all views  
✅ **Scalable** - Extracted from existing data, no manual entry  
✅ **Clean structure** - Follows computing pattern  

## Future Enhancements

Potential improvements:

- [ ] Add programme leader names (if data source identified)
- [ ] Create custom icons for each programme
- [ ] Add programme images/banners
- [ ] Extract more programme metadata (levels, awards, etc.)
- [ ] Add filtering/ordering options
- [ ] Generate programme statistics per semester

## Verification

✅ All 111 programmes have topic.md  
✅ All 443 semesters have topic.md  
✅ All 2,132 web objects have link.md + weburl  
✅ Icons applied to programmes topic  
✅ Icons applied to each programme  
✅ Module icons inherited correctly  
✅ WebURLs point to correct cluster notes  
✅ TUTORS_COURSE_ID used from .env  

## Usage

**Regenerate:**
```bash
cd science
./generate-master
```

**Build with Tutors:**
```bash
cd tutors-modules-master
deno run -A jsr:@tutors/tutors
```

## Implementation Date

2026-06-02

## Status

✅ **COMPLETE** - Task-03-programmes fully implemented and tested

All 111 programmes with 443 semesters and 2,132 web objects successfully generated!
