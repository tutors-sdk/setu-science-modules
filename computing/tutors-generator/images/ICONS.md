# Module Icons

The catalogue uses custom icons for each module, carefully selected to match the module content.

## Icon Configuration

Icons are defined in `module-catalogue/module-icons.yaml`:

```yaml
A13443:
  type: carbon:sys-provision
  color: '014771'
A06609:
  type: vscode-icons:file-type-python
  color: '317234'
```

- **type**: Icon identifier from [Iconify](https://icon-sets.iconify.design/)
- **color**: Hex color code (quoted to preserve leading zeros)

## Icon Sources

All icons are from the Iconify icon sets:
- https://icon-sets.iconify.design/

Common icon sets used:
- **fluent**: Microsoft Fluent UI icons
- **carbon**: IBM Carbon Design System
- **lucide**: Lucide icons
- **simple-icons**: Brand/technology logos
- **vscode-icons**: VS Code file type icons
- **material-symbols**: Google Material Symbols
- **tabler**: Tabler icons
- **mingcute**: MingCute icons
- **iconoir**: Iconoir icons
- **ph**: Phosphor icons
- **ri**: Remix Icon

## How Icons are Used

### 1. Cluster Notes (`unit-2-clusters`)

Each module note starts with icon frontmatter:

```markdown
---
icon:
  type: vscode-icons:file-type-python
  color: '317234'
---

# Programming Fundamentals 1

Module content here...
```

### 2. Programme Web Links (`unit-1-programmes`)

Each module link in a programme semester uses the same icon:

```markdown
---
icon:
  type: vscode-icons:file-type-python
  color: '317234'
---

Programming Fundamentals 1
```

## Extraction Process

Icons were extracted from the reference tutors course using:

```python
# Extract icons from all note.md files
for note_file in tutors/unit-2-clusters/*/note-*/note.md:
    # Parse frontmatter
    # Extract module code from content
    # Map code -> {type, color}
```

The extraction script preserves:
- Leading zeros in hex colors (e.g., `'014771'` not `14771`)
- Exact icon type strings
- Original color casing

## Statistics

- **Total modules**: 225
- **Total icons mapped**: 225
- **Coverage**: 100%

## Adding Icons for New Modules

When adding a new module:

1. Choose an appropriate icon from [Iconify](https://icon-sets.iconify.design/)
2. Select a color that fits the module theme
3. Add to `module-catalogue/module-icons.yaml`:

```yaml
A99999:
  type: chosen-icon-type
  color: 'HEXCOLOR'
```

4. Regenerate the catalogue:

```bash
python3 generate-catalogue.py
```

## Icon Selection Guidelines

Choose icons that represent:

- **Technology/Language**: Use brand icons for specific technologies
  - Python modules: `vscode-icons:file-type-python`
  - Java modules: `vscode-icons:file-type-java`
  - JavaScript/Web: `vscode-icons:file-type-js`

- **Subject Area**: Use conceptual icons
  - Database: `carbon:data-base`, `fluent:database-24-regular`
  - Security: `solar:lock-bold`, `fluent:shield-24-regular`
  - Networks: `fluent:network-24-regular`, `carbon:network-3`

- **Activity Type**: Use action icons
  - Projects: `fluent:clipboard-task-24-regular`
  - Research: `lucide:star`, `material-symbols:science`
  - Design: `carbon:model-builder`, `simple-icons:uml`

- **Professional Skills**: Use specific icons
  - Communication: `ri:translate`, `iconoir:sound-high`
  - Mathematics: `tabler:math`, `tabler:sum`
  - Business: `carbon:business-processes`

## Color Palette

Colors are chosen to:
- Differentiate module types
- Group related modules
- Provide visual distinction in the UI

Common color ranges:
- **Blue tones** (`014771`, `1975BE`): Technical/Computing
- **Green tones** (`317234`, `52BD56`): Development/Programming  
- **Purple tones** (`9024A3`, `CB32E5`): Analytics/Data
- **Orange/Red tones** (`FF5722`, `BD342A`): Systems/Hardware
- **Brown tones** (`725043`, `A27260`): Humanities/Soft skills

## Maintenance

The icon mapping should be:
- **Version controlled**: Changes tracked in git
- **Documented**: Significant changes noted in commit messages
- **Validated**: Icons tested in Tutors UI before deployment

## Troubleshooting

### Icon not displaying

1. Check icon type is valid on Iconify
2. Verify YAML syntax (quotes around color)
3. Ensure module code matches exactly

### Color appears wrong

1. Check hex color has quotes: `color: '014771'` not `color: 014771`
2. Leading zeros must be preserved
3. Colors are case-insensitive but uppercase is preferred

### Missing icon for module

If a module has no icon defined, the generator uses default:
- **Type**: `carbon:sys-provision`
- **Color**: `'014771'`

Add the module to `module-icons.yaml` to customize.
