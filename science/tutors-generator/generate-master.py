#!/usr/bin/env python3
"""
SETU Science Module Catalogue Generator - Master
This script generates the tutors-modules-master course from science/module-catalogue data.
It creates a cluster-based view similar to computing's unit-2-clusters.
"""

import os
import yaml
import shutil
from pathlib import Path
from typing import Dict, List, Any
import re


class MasterCatalogueGenerator:
    def __init__(self, source_dir: str = "module-catalogue", output_dir: str = "tutors-modules-master"):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)

        # Data stores
        self.descriptors = {}
        self.clusters = {}

        # Load icon mappings from computing if available
        self.module_icons = {}
        self.load_computing_icons()

    def load_computing_icons(self):
        """Load icon mappings from computing catalogue for overlapping modules"""
        computing_icons = Path("../computing/module-catalogue/module-icons.yaml")
        if computing_icons.exists():
            with open(computing_icons) as f:
                self.module_icons = yaml.safe_load(f) or {}
            print(f"Loaded {len(self.module_icons)} icon mappings from computing catalogue")
        else:
            print("Computing icon mappings not found, will use defaults")

    def load_data(self):
        """Load all YAML descriptors from source directory"""
        print("Loading catalogue data...")

        # Load descriptors
        for desc_file in (self.source_dir / "descriptors" / "yaml").glob("*.yaml"):
            with open(desc_file) as f:
                data = yaml.safe_load(f)
                # Extract module code from reference field
                module_code = data.get('reference', desc_file.stem.split('_')[0])
                self.descriptors[module_code] = data

        # Build cluster index from descriptors
        for code, descriptor in self.descriptors.items():
            cluster = descriptor.get('cluster', 'Uncategorized')
            if cluster not in self.clusters:
                self.clusters[cluster] = []
            self.clusters[cluster].append(code)

        print(f"Loaded {len(self.descriptors)} modules")
        print(f"Found {len(self.clusters)} clusters")

    def clean_output(self):
        """Clean the output directory"""
        if self.output_dir.exists():
            # Keep these files
            keep_files = ['properties.yaml', 'course.md', 'course.png']

            for item in self.output_dir.iterdir():
                if item.name not in keep_files:
                    if item.is_dir():
                        shutil.rmtree(item)
                    else:
                        item.unlink()

    def create_course_files(self):
        """Create required course files"""
        print("\nSetting up course files...")

        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Create course.md
        course_md = self.output_dir / "course.md"
        if not course_md.exists():
            with open(course_md, 'w') as f:
                f.write("# SETU Science Module Catalogue\n\n")
                f.write("This site contains a complete catalogue of approved modules across all of SETU's science programmes.\n\n")
                f.write(f"**{len(self.descriptors)} modules** organized into **{len(self.clusters)} subject clusters**.\n")
            print("  Created course.md")
        else:
            print("  course.md already exists")

        # Create properties.yaml
        props = self.output_dir / "properties.yaml"
        if not props.exists():
            with open(props, 'w') as f:
                f.write("credits: SETU Faculty\n")
                f.write("parent: #\n")
                f.write("pdfOrientation: portrait\n")
                f.write("llm: 2\n")
            print("  Created properties.yaml")
        else:
            print("  properties.yaml already exists")

    def sanitize_filename(self, text: str) -> str:
        """Convert text to safe filename"""
        # Replace spaces with underscores
        text = text.replace(' ', '_')
        # Remove special characters except dash and underscore
        text = re.sub(r'[^\w\-]', '', text)
        return text

    def convert_latex_to_markdown(self, text: str) -> str:
        """Convert LaTeX formatting to markdown"""
        if not text:
            return text

        # Replace \emph{...} with *...*
        text = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', text)

        return text

    def generate_module_markdown(self, module_code: str) -> str:
        """Generate markdown content for a module from science schema"""
        descriptor = self.descriptors.get(module_code)

        if not descriptor:
            return f"# {module_code}\n\nModule data not available."

        md = []

        # Icon and title - use custom icon if available
        icon_info = self.module_icons.get(module_code)
        if icon_info:
            icon_type = icon_info.get('type', 'carbon:sys-provision')
            icon_color = icon_info.get('color', '014771')
        else:
            # Default icon
            icon_type = 'carbon:sys-provision'
            icon_color = '014771'

        md.append("---")
        md.append("icon:")
        md.append(f"  type: {icon_type}")
        md.append(f"  color: {icon_color}")
        md.append("---")
        md.append("")
        md.append(f"# {descriptor.get('short_title', descriptor.get('full_title', module_code))}")
        md.append("")

        # Aim - extract first sentence only for the summary
        if 'aim' in descriptor:
            aim_text = descriptor['aim']
            # Extract first sentence
            match = re.search(r'(?<![A-Z]\d)\.(?:\s+[A-Z]|[A-Z](?=[a-z]))', aim_text)
            if match:
                first_sentence = aim_text[:match.start() + 1].strip()
            else:
                first_sentence = aim_text.strip()
                if not first_sentence.endswith('.'):
                    first_sentence += '.'
            md.append(first_sentence)
        md.append("")
        md.append(f'<p><a href="./archives/{module_code}.pdf" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; text-decoration: none;"><img src="https://upload.wikimedia.org/wikipedia/commons/6/60/Adobe_Acrobat_Reader_icon_%282020%29.svg" width="20" height="20" style="margin-right: 4px;" alt="Adobe Acrobat Icon"><span>Module Descriptor (PDF)</span></a></p>')
        md.append("")

        # Module information table
        md.append("## Module Information")
        md.append("")
        md.append("| **Field** | **Details** |")
        md.append("|-----------|-------------|")
        md.append(f"| **Module Code** | {module_code} |")
        md.append(f"| **Module Title** | {descriptor.get('full_title', 'N/A')} |")
        md.append(f"| **Short Title** | {descriptor.get('short_title', 'N/A')} |")
        md.append(f"| **Credits** | {descriptor.get('credits', 'N/A')} ECTS |")
        md.append(f"| **Level** | {descriptor.get('level', 'N/A')} |")
        md.append(f"| **School** | {descriptor.get('school', 'N/A')} |")
        md.append(f"| **Department** | {descriptor.get('department', 'N/A')} |")
        md.append(f"| **Module Author** | {descriptor.get('author', 'N/A')} |")
        md.append(f"| **Cluster** | {descriptor.get('cluster', 'N/A')} |")
        md.append("")
        md.append("---")
        md.append("")

        # Module aim
        if 'aim' in descriptor:
            md.append("## Module Aim")
            md.append("")
            md.append(self.convert_latex_to_markdown(descriptor['aim']))
            md.append("")
            md.append("---")
            md.append("")

        # Learning outcomes
        if 'learning_outcomes' in descriptor:
            md.append("## Learning Outcomes")
            md.append("")
            md.append("On successful completion of this module, learners will be able to:")
            md.append("")
            for i, outcome in enumerate(descriptor['learning_outcomes'], 1):
                md.append(f"{i}. {self.convert_latex_to_markdown(outcome)}")
            md.append("")
            md.append("---")
            md.append("")

        # Indicative content
        if 'indicative_content' in descriptor:
            md.append("## Indicative Content")
            md.append("")
            md.append("The module covers the following topics:")
            md.append("")
            for topic in descriptor['indicative_content']:
                md.append(f"- {self.convert_latex_to_markdown(topic)}")
            md.append("")
            md.append("---")
            md.append("")

        # Learning and teaching methods
        if 'learning_and_teaching_methods' in descriptor:
            md.append("## Learning and Teaching Methods")
            md.append("")
            for method in descriptor['learning_and_teaching_methods']:
                md.append(self.convert_latex_to_markdown(method))
                md.append("")

            # Contact hours table
            if 'learning_modes' in descriptor:
                md.append("### Contact Hours")
                md.append("")
                md.append("| **Activity** | **Full Time Hours** | **Part Time Hours** |")
                md.append("|--------------|---------------------|---------------------|")

                total_ft = 0
                total_pt = 0
                for mode in descriptor['learning_modes']:
                    ft = mode.get('full_time', 0)
                    pt = mode.get('part_time', 0)
                    # Handle cases where values might be strings or missing
                    try:
                        ft_val = int(ft) if ft else 0
                    except (ValueError, TypeError):
                        ft_val = 0
                    try:
                        pt_val = int(pt) if pt else 0
                    except (ValueError, TypeError):
                        pt_val = 0
                    total_ft += ft_val
                    total_pt += pt_val
                    md.append(f"| {mode['name']} | {ft_val} | {pt_val} |")

                md.append(f"| **Total** | **{total_ft}** | **{total_pt}** |")
                md.append("")

            md.append("---")
            md.append("")

        # Assessment methods
        if 'assessment_methods' in descriptor:
            md.append("## Assessment Methods")
            md.append("")
            md.append("| **Assessment Type** | **Learning Outcomes** | **Weighting** |")
            md.append("|---------------------|----------------------|---------------|")

            main_assessments = [a for a in descriptor['assessment_methods'] if a.get('main', False)]
            sub_assessments = [a for a in descriptor['assessment_methods'] if not a.get('main', False)]

            for assessment in main_assessments:
                los = assessment.get('learning_outcomes', 'All')
                weight = assessment.get('weighting', 0)
                md.append(f"| **{assessment['name']}** | {los} | **{weight}%** |")

            for assessment in sub_assessments:
                los = assessment.get('learning_outcomes', '')
                weight = assessment.get('weighting', 0)
                md.append(f"| - {assessment['name']} | {los} | {weight}% |")

            md.append("")
            md.append("---")
            md.append("")

        # Assessment criteria
        if 'assessment_criteria' in descriptor:
            md.append("## Assessment Criteria")
            md.append("")

            for criterion in descriptor['assessment_criteria']:
                criterion_text = self.convert_latex_to_markdown(criterion)
                md.append(criterion_text)
                md.append("")

            md.append("---")
            md.append("")

        # Pre-requisites and co-requisites
        prereqs = descriptor.get('prerequisites', [])
        coreqs = descriptor.get('corequisites', [])

        md.append("## Pre-requisites and Co-requisites")
        md.append("")
        md.append(f"- **Pre-requisites:** {', '.join(prereqs) if prereqs else 'None'}")
        md.append(f"- **Co-requisites:** {', '.join(coreqs) if coreqs else 'None'}")
        md.append("")
        md.append("---")
        md.append("")

        # Recommended reading
        if 'supplementary_material' in descriptor:
            md.append("## Recommended Reading")
            md.append("")
            md.append("### Supplementary Material")
            md.append("")
            for material in descriptor['supplementary_material']:
                md.append(f"- {self.convert_latex_to_markdown(material)}")
            md.append("")
            md.append("---")
            md.append("")

        if 'essential_material' in descriptor:
            if 'supplementary_material' not in descriptor:
                md.append("## Recommended Reading")
                md.append("")
            md.append("### Essential Material")
            md.append("")
            for material in descriptor['essential_material']:
                md.append(f"- {self.convert_latex_to_markdown(material)}")
            md.append("")
            md.append("---")
            md.append("")

        # Programme information
        if 'programmes' in descriptor and descriptor['programmes']:
            md.append("## Programme Information")
            md.append("")
            md.append("This module is available on the following programmes:")
            md.append("")
            md.append("| **Programme Code** | **Programme Title** | **Stage** | **Semester** | **Status** |")
            md.append("|-------------------|---------------------|-----------|--------------|------------|")

            for prog_info in descriptor['programmes']:
                if prog_info:  # Skip None entries
                    prog_code = prog_info.get('code', '')
                    prog_title = prog_info.get('name', '')
                    stage = prog_info.get('stage', '')
                    semester = prog_info.get('semester', '')
                    status = 'Mandatory' if prog_info.get('status') == 'M' else 'Elective'
                    md.append(f"| {prog_code} | {prog_title} | {stage} | {semester} | {status} |")

            md.append("")
            md.append("---")
            md.append("")

        # Resources required
        if 'requested_resources' in descriptor:
            md.append("## Resources Required")
            md.append("")
            for resource in descriptor['requested_resources']:
                md.append(f"- {self.convert_latex_to_markdown(resource)}")
            md.append("")
            md.append("---")
            md.append("")

        # Footer
        timetable_code = 'N/A'
        if 'programmes' in descriptor and descriptor['programmes']:
            for prog in descriptor['programmes']:
                if prog and prog.get('timetable'):
                    timetable_code = prog['timetable']
                    break

        md.append(f"*Module Code: {module_code} | Timetable Code: {timetable_code}*")

        return '\n'.join(md)

    def generate_clusters(self):
        """Generate cluster-based folder structure"""
        print("\nGenerating cluster view...")

        # Create root topic.md
        with open(self.output_dir / "topic.md", 'w') as f:
            f.write("# SETU Science Modules\n\n")
            f.write("Browse modules organized by subject cluster.\n")

        # Sort clusters alphabetically
        sorted_clusters = sorted(self.clusters.items(), key=lambda x: x[0])

        for idx, (cluster_name, module_codes) in enumerate(sorted_clusters, 1):
            cluster_dir_name = self.sanitize_filename(cluster_name)
            cluster_dir = self.output_dir / f"topic-{idx:02d}-{cluster_dir_name}"
            cluster_dir.mkdir(exist_ok=True)

            # Create cluster topic.md
            with open(cluster_dir / "topic.md", 'w') as f:
                f.write(f"# {cluster_name}\n\n\n")

            # Sort modules in cluster alphabetically by module name
            module_with_names = []
            for module_code in module_codes:
                descriptor = self.descriptors.get(module_code)
                if descriptor:
                    name = descriptor.get('full_title', module_code)
                    module_with_names.append((module_code, name))

            # Sort by name
            sorted_modules = [code for code, name in sorted(module_with_names, key=lambda x: x[1])]

            for mod_idx, module_code in enumerate(sorted_modules, 1):
                descriptor = self.descriptors.get(module_code)

                if not descriptor:
                    continue

                module_name = self.sanitize_filename(descriptor.get('full_title', module_code))
                note_dir_name = f"note-{mod_idx:02d}-note-{mod_idx:02d}-{module_name}"
                note_dir = cluster_dir / note_dir_name
                note_dir.mkdir(exist_ok=True)

                # Create archives directory
                archives_dir = note_dir / "archives"
                archives_dir.mkdir(exist_ok=True)

                # Copy PDF if exists
                pdf_source = self.source_dir / "descriptors" / "pdf" / f"{descriptor.get('reference', module_code)}.pdf"
                # Try alternate naming pattern
                if not pdf_source.exists():
                    # Try with full filename from directory
                    yaml_file = self.source_dir / "descriptors" / "yaml" / f"{descriptor.get('reference', module_code)}.yaml"
                    pdf_name = yaml_file.stem.replace('.yaml', '.pdf')
                    for pdf_file in (self.source_dir / "descriptors" / "pdf").glob(f"{module_code}*.pdf"):
                        pdf_source = pdf_file
                        break

                if pdf_source.exists():
                    shutil.copy(pdf_source, archives_dir / f"{module_code}.pdf")

                # Generate note.md
                markdown = self.generate_module_markdown(module_code)
                with open(note_dir / "note.md", 'w') as f:
                    f.write(markdown)

        print(f"Generated {len(sorted_clusters)} clusters with modules")

    def generate(self):
        """Main generation process"""
        print("=" * 60)
        print("SETU Science Module Catalogue Generator - Master")
        print("=" * 60)

        # Load all data
        self.load_data()

        # Create course files first
        self.create_course_files()

        # Clean output (preserve certain files)
        print("\nCleaning output directory...")
        self.clean_output()

        # Generate cluster structure
        self.generate_clusters()

        print("\n" + "=" * 60)
        print("Generation complete!")
        print("=" * 60)
        print(f"\nOutput directory: {self.output_dir}")
        print(f"- Clusters: {len(self.clusters)}")
        print(f"- Modules: {len(self.descriptors)}")


if __name__ == "__main__":
    import sys
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "tutors-modules-master"
    generator = MasterCatalogueGenerator(output_dir=output_dir)
    generator.generate()
