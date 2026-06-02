#!/usr/bin/env python3
"""
SETU Module Catalogue Generator

This script generates the tutors folder structure from the module-catalogue source data.
It creates:
1. Programme-based view (unit-1-programmes)
2. Cluster-based view (unit-2-clusters)
"""

import os
import yaml
import shutil
from pathlib import Path
from typing import Dict, List, Any
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class CatalogueGenerator:
    def __init__(self, source_dir: str = "module-catalogue", output_dir: str = "tutors-catalogue/tutors"):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)

        # Load Tutors course ID from environment
        self.tutors_course_id = os.getenv('TUTORS_COURSE_ID', 'setu-comp-sci-modules-md')

        # Data stores
        self.programmes = {}
        self.modules = {}
        self.descriptors = {}
        self.schedules = {}
        self.clusters = {}
        self.module_to_cluster_path = {}  # Maps module code to cluster note path

        # Load ordering configuration
        self.programme_order = []
        self.cluster_order = []
        self.load_ordering()

        # Load icon mappings
        self.module_icons = {}
        self.load_icons()

    def load_ordering(self):
        """Load ordering configuration from module-catalogue/.catalogue-order.yaml"""
        order_file = self.source_dir / ".catalogue-order.yaml"
        if order_file.exists():
            with open(order_file) as f:
                order_data = yaml.safe_load(f)
                self.programme_order = order_data.get('programmes', [])
                self.cluster_order = order_data.get('clusters', [])
        else:
            print("Warning: .catalogue-order.yaml not found, using alphabetical order")

    def load_icons(self):
        """Load icon mappings from module-icons.yaml"""
        icon_file = self.source_dir / "module-icons.yaml"
        if icon_file.exists():
            with open(icon_file) as f:
                self.module_icons = yaml.safe_load(f) or {}
            print(f"Loaded {len(self.module_icons)} module icon mappings")
        else:
            print("Warning: module-icons.yaml not found, using default icons")

    def load_data(self):
        """Load all YAML data from source directory"""
        print("Loading catalogue data...")

        # Load programmes
        for prog_file in (self.source_dir / "programmes" / "yaml").glob("*.yaml"):
            with open(prog_file) as f:
                data = yaml.safe_load(f)
                self.programmes[data['code']] = data

        # Load modules
        for mod_file in (self.source_dir / "modules" / "yaml").glob("*.yaml"):
            with open(mod_file) as f:
                data = yaml.safe_load(f)
                self.modules[data['code']] = data

        # Load descriptors
        for desc_file in (self.source_dir / "descriptors" / "yaml").glob("*.yaml"):
            with open(desc_file) as f:
                data = yaml.safe_load(f)
                self.descriptors[data['code']] = data

        # Load schedules
        for sched_file in (self.source_dir / "schedules" / "yaml").glob("*.yaml"):
            with open(sched_file) as f:
                data = yaml.safe_load(f)
                self.schedules[data['code']] = data

        # Build cluster index from modules
        for code, module in self.modules.items():
            subgroup = module.get('subgroup', 'Uncategorized')
            if subgroup not in self.clusters:
                self.clusters[subgroup] = []
            self.clusters[subgroup].append(code)

        print(f"Loaded {len(self.programmes)} programmes, {len(self.modules)} modules")
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

    def copy_course_files(self):
        """Copy or create required course files"""
        print("\nSetting up course files...")

        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Try to copy from tutors-reference/ if it exists, otherwise create defaults
        tutors_dir = Path("tutors-catalogue/tutors-reference")

        # Copy or create course.md
        course_md_source = tutors_dir / "course.md"
        course_md_dest = self.output_dir / "course.md"
        if course_md_source.exists() and not course_md_dest.exists():
            shutil.copy(course_md_source, course_md_dest)
            print("  Copied course.md from tutors-reference/")
        elif not course_md_dest.exists():
            # Create default
            with open(course_md_dest, 'w') as f:
                f.write("# SETU Computing Module Catalogue\n\n")
                f.write("This site contains a complete catalogue of approved modules across all of SETU's computing programmes")
            print("  Created default course.md")
        else:
            print("  course.md already exists")

        # Copy or create properties.yaml
        props_source = tutors_dir / "properties.yaml"
        props_dest = self.output_dir / "properties.yaml"
        if props_source.exists() and not props_dest.exists():
            shutil.copy(props_source, props_dest)
            print("  Copied properties.yaml from tutors-reference/")
        elif not props_dest.exists():
            # Create default
            with open(props_dest, 'w') as f:
                f.write("credits: Peter Windle, Kieran Murphy, Eamonn De Leastar\n")
                f.write("parent: #\n")
                f.write("pdfOrientation : portrait\n")
                f.write("llm: 2\n")
                f.write("github: https://github.com/tutors-sdk/setu-compsci-catalogue/blob/main/tutors-md/\n")
            print("  Created default properties.yaml")
        else:
            print("  properties.yaml already exists")

        # Copy course.png if it exists
        png_source = tutors_dir / "course.png"
        png_dest = self.output_dir / "course.png"
        if png_source.exists() and not png_dest.exists():
            shutil.copy(png_source, png_dest)
            print("  Copied course.png from tutors-reference/")
        elif not png_dest.exists():
            print("  course.png not found (optional)")
        else:
            print("  course.png already exists")

    def sanitize_filename(self, text: str) -> str:
        """Convert text to safe filename"""
        # Replace spaces with underscores
        text = text.replace(' ', '_')
        # Remove special characters except dash and underscore (no commas)
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
        """Generate markdown content for a module"""
        module = self.modules.get(module_code)
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
        md.append(f"# {descriptor.get('short title', descriptor.get('full title', module_code))}")
        md.append("")

        # Aim - extract first sentence only for the summary
        if 'aim' in descriptor:
            aim_text = descriptor['aim']
            # Extract first sentence
            # Look for period followed by space or capital letter, but not in abbreviations
            import re
            # Match period followed by space and capital, or period followed by capital (no space)
            # But avoid splitting on common patterns like "B1.1", "v1.0" etc
            # Pattern: period not preceded by single letter/digit, followed by space/capital
            match = re.search(r'(?<![A-Z]\d)\.(?:\s+[A-Z]|[A-Z](?=[a-z]))', aim_text)
            if match:
                first_sentence = aim_text[:match.start() + 1].strip()
            else:
                # No clear sentence boundary found, use whole text
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
        md.append(f"| **Module Title** | {descriptor.get('full title', 'N/A')} |")
        md.append(f"| **Short Title** | {descriptor.get('short title', 'N/A')} |")
        md.append(f"| **Credits** | {descriptor.get('credits', 'N/A')} ECTS |")
        md.append(f"| **Level** | {descriptor.get('level', 'N/A')} (Level 8) |")
        md.append(f"| **Department** | {descriptor.get('department', 'N/A')} |")

        if module:
            md.append(f"| **Module Author** | {module.get('author', 'N/A')} |")
            md.append(f"| **Cluster** | {module.get('subgroup', 'N/A')} |")

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
        if 'learning outcomes' in descriptor:
            md.append("## Learning Outcomes")
            md.append("")
            md.append("On successful completion of this module, learners will be able to:")
            md.append("")
            for i, outcome in enumerate(descriptor['learning outcomes'], 1):
                md.append(f"{i}. {self.convert_latex_to_markdown(outcome)}")
            md.append("")
            md.append("---")
            md.append("")

        # Indicative content
        if 'indicative content' in descriptor:
            md.append("## Indicative Content")
            md.append("")
            md.append("The module covers the following topics:")
            md.append("")
            for topic in descriptor['indicative content']:
                md.append(f"- {self.convert_latex_to_markdown(topic)}")
            md.append("")
            md.append("---")
            md.append("")

        # Learning and teaching methods
        if 'learning and teaching methods' in descriptor:
            md.append("## Learning and Teaching Methods")
            md.append("")
            for method in descriptor['learning and teaching methods']:
                md.append(self.convert_latex_to_markdown(method))
                md.append("")

            # Contact hours table
            if 'learning modes' in descriptor:
                md.append("### Contact Hours")
                md.append("")
                md.append("| **Activity** | **Full Time Hours** | **Part Time Hours** |")
                md.append("|--------------|---------------------|---------------------|")

                total_ft = 0
                total_pt = 0
                for mode in descriptor['learning modes']:
                    ft = mode.get('full time', 0)
                    pt = mode.get('part time', 0)
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
        if 'assessment methods' in descriptor:
            md.append("## Assessment Methods")
            md.append("")
            md.append("| **Assessment Type** | **Learning Outcomes** | **Weighting** |")
            md.append("|---------------------|----------------------|---------------|")

            main_assessments = [a for a in descriptor['assessment methods'] if a.get('main', False)]
            sub_assessments = [a for a in descriptor['assessment methods'] if not a.get('main', False)]

            for assessment in main_assessments:
                los = assessment.get('learning outcomes', 'All')
                weight = assessment.get('weighting', 0)
                md.append(f"| **{assessment['name']}** | {los} | **{weight}%** |")

            for assessment in sub_assessments:
                los = assessment.get('learning outcomes', '')
                weight = assessment.get('weighting', 0)
                md.append(f"| - {assessment['name']} | {los} | {weight}% |")

            md.append("")
            md.append("---")
            md.append("")

        # Assessment criteria
        if 'assessment criteria' in descriptor:
            md.append("## Assessment Criteria")
            md.append("")

            criteria_map = {
                '<40%': ('Fail', '<40%'),
                '40%-49%': ('Pass', '40%-49%'),
                '50%-59%': ('Credit', '50%-59%'),
                '60%-69%': ('Distinction', '60%-69%'),
                '70%-100%': ('High Distinction', '70%-100%')
            }

            for criterion in descriptor['assessment criteria']:
                for key, (title, range_text) in criteria_map.items():
                    if criterion.startswith(key):
                        md.append(f"### {title} ({range_text})")
                        md.append(self.convert_latex_to_markdown(criterion))
                        md.append("")
                        break

            md.append("---")
            md.append("")

        # Pre-requisites and co-requisites
        prereqs = descriptor.get('pre-requisites', [])
        coreqs = descriptor.get('co-requisites', [])

        md.append("## Pre-requisites and Co-requisites")
        md.append("")
        md.append(f"- **Pre-requisites:** {', '.join(prereqs) if prereqs else 'None'}")
        md.append(f"- **Co-requisites:** {', '.join(coreqs) if coreqs else 'None'}")
        md.append("")
        md.append("---")
        md.append("")

        # Recommended reading
        if 'supplementary material' in descriptor:
            md.append("## Recommended Reading")
            md.append("")
            md.append("### Supplementary Material")
            md.append("")
            for material in descriptor['supplementary material']:
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
                    prog_code = prog_info.get('programme', '')
                    prog_title = prog_info.get('title', '')
                    stage = prog_info.get('stage', '')
                    semester = prog_info.get('semester', '')
                    status = 'Mandatory' if prog_info.get('status') == 'M' else 'Elective'
                    md.append(f"| {prog_code} | {prog_title} | {stage} | {semester} | {status} |")

            md.append("")
            md.append("---")
            md.append("")

        # Resources required
        if 'requested resources' in descriptor:
            md.append("## Resources Required")
            md.append("")
            for resource in descriptor['requested resources']:
                md.append(f"- {self.convert_latex_to_markdown(resource)}")
            md.append("")
            md.append("---")
            md.append("")

        # Footer
        timetable = module.get('timetable', 'N/A') if module else 'N/A'
        md.append(f"*Module Code: {module_code} | Timetable Code: {timetable}*")

        return '\n'.join(md)

    def copy_topic_image(self, source_name: str, dest_dir: Path, image_type: str = "programme"):
        """Copy topic image from image library to destination"""
        # Determine source directory
        if image_type == "programme":
            source_dir = self.source_dir / "images" / "programmes"
        else:  # cluster
            source_dir = self.source_dir / "images" / "clusters"

        # Check for image with various extensions
        # For clusters, prefer PNG (ChatGPT images), for programmes prefer SVG
        if image_type == "cluster":
            extensions = ['png', 'svg', 'jpg', 'jpeg']
        else:  # programme
            extensions = ['svg', 'png', 'jpg', 'jpeg']

        for ext in extensions:
            source_file = source_dir / f"{source_name}.{ext}"
            if source_file.exists():
                dest_file = dest_dir / f"topic.{ext}"
                shutil.copy(source_file, dest_file)
                return True
        return False

    def generate_programmes(self):
        """Generate programme-based folder structure"""
        print("\nGenerating programme view...")

        unit_dir = self.output_dir / "unit-1-programmes"
        unit_dir.mkdir(parents=True, exist_ok=True)

        # Create unit topic.md
        with open(unit_dir / "topic.md", 'w') as f:
            f.write("# Programmes\n\nBrowse modules organized by programme and semester.\n")

        # Sort programmes using defined order
        if self.programme_order:
            # Use the defined order
            sorted_programmes = []
            for prog_code in self.programme_order:
                if prog_code in self.programmes:
                    sorted_programmes.append((prog_code, self.programmes[prog_code]))
            # Add any programmes not in the order list at the end
            for prog_code, prog_data in sorted(self.programmes.items()):
                if prog_code not in self.programme_order:
                    sorted_programmes.append((prog_code, prog_data))
        else:
            # Fallback to alphabetical
            sorted_programmes = sorted(self.programmes.items(), key=lambda x: x[0])

        for idx, (prog_code, programme) in enumerate(sorted_programmes):
            prog_name = self.sanitize_filename(programme.get('name', prog_code))
            prog_dir = unit_dir / f"topic-{idx:02d}-{prog_code}"
            prog_dir.mkdir(exist_ok=True)

            # Copy programme topic image
            self.copy_topic_image(prog_code, prog_dir, "programme")

            # Create programme topic.md
            leader = programme.get('leader', 'N/A')
            with open(prog_dir / "topic.md", 'w') as f:
                f.write(f"# {programme.get('name', prog_code)}\n\n")
                f.write(f"Programme leader: {leader}\n")

            # Get schedule for this programme
            schedule = self.schedules.get(prog_code)
            if not schedule:
                continue

            # Get actual semester numbers from the schedule
            semester_nums = sorted(schedule.get('semesters', {}).keys())

            # Create semester units
            for semester_num in semester_nums:
                semester_dir = prog_dir / f"unit-{semester_num}"
                semester_dir.mkdir(exist_ok=True)

                # Create semester topic.md
                with open(semester_dir / "topic.md", 'w') as f:
                    f.write(f"# Semester {semester_num}\n\nTODO (semester)\n")

                # Get modules for this semester
                semester_data = schedule.get('semesters', {}).get(semester_num)
                if not semester_data:
                    continue

                # Combine mandatory and elective modules
                mandatory_modules = semester_data.get('mandatory', [])
                elective_modules = semester_data.get('elective', [])
                all_modules = mandatory_modules + elective_modules

                # Create web links for each module
                for mod_idx, module_info in enumerate(all_modules, 1):
                    module_code = module_info.get('code')
                    module_name = self.sanitize_filename(module_info.get('name', module_code))

                    web_dir = semester_dir / f"web-{mod_idx:02d}-web-{mod_idx:02d}-{module_name}"
                    web_dir.mkdir(exist_ok=True)

                    # Get cluster path from mapping (will be populated after clusters are generated)
                    cluster_path = self.module_to_cluster_path.get(module_code, "#")

                    # Get icon for this module
                    icon_info = self.module_icons.get(module_code)
                    if icon_info:
                        icon_type = icon_info.get('type', 'lucide:presentation')
                        icon_color = icon_info.get('color', '394B53')
                    else:
                        # Default icon
                        icon_type = 'lucide:presentation'
                        icon_color = '394B53'

                    # Get short title and first sentence of aim from descriptor if available
                    descriptor = self.descriptors.get(module_code)
                    if descriptor:
                        module_title = descriptor.get('short title', module_info.get('name', module_code))

                        # Extract first sentence of aim
                        aim_text = descriptor.get('aim', '')
                        if aim_text:
                            # Match period followed by space and capital, or period followed by capital (no space)
                            match = re.search(r'(?<![A-Z]\d)\.(?:\s+[A-Z]|[A-Z](?=[a-z]))', aim_text)
                            if match:
                                first_sentence = aim_text[:match.start() + 1].strip()
                            else:
                                first_sentence = aim_text.strip()
                                if not first_sentence.endswith('.'):
                                    first_sentence += '.'
                            # Convert LaTeX to markdown
                            first_sentence = self.convert_latex_to_markdown(first_sentence)
                        else:
                            first_sentence = ''
                    else:
                        module_title = module_info.get('name', module_code)
                        first_sentence = ''

                    # Create link.md
                    with open(web_dir / "link.md", 'w') as f:
                        f.write("---\n")
                        f.write("icon:\n")
                        f.write(f"  type: {icon_type}\n")
                        f.write(f"  color: {icon_color}\n")
                        f.write("---\n\n")
                        f.write(module_title)
                        if first_sentence:
                            f.write("\n\n")
                            f.write(first_sentence)

                    # Create weburl
                    with open(web_dir / "weburl", 'w') as f:
                        f.write(cluster_path)

        print(f"Generated {len(sorted_programmes)} programmes")

    def generate_clusters(self):
        """Generate cluster-based folder structure"""
        print("\nGenerating cluster view...")

        unit_dir = self.output_dir / "unit-2-clusters"
        unit_dir.mkdir(parents=True, exist_ok=True)

        # Create unit topic.md
        with open(unit_dir / "topic.md", 'w') as f:
            f.write("# Clusters\n\nBrowse modules organized by subject cluster.\n")

        # Sort clusters using defined order
        if self.cluster_order:
            # Use the defined order
            sorted_clusters = []
            for cluster_name in self.cluster_order:
                if cluster_name in self.clusters:
                    sorted_clusters.append((cluster_name, self.clusters[cluster_name]))
            # Add any clusters not in the order list at the end
            for cluster_name, module_codes in sorted(self.clusters.items()):
                if cluster_name not in self.cluster_order:
                    sorted_clusters.append((cluster_name, module_codes))
        else:
            # Fallback to alphabetical
            sorted_clusters = sorted(self.clusters.items(), key=lambda x: x[0])

        for idx, (cluster_name, module_codes) in enumerate(sorted_clusters, 1):
            cluster_dir_name = self.sanitize_filename(cluster_name)
            cluster_dir = unit_dir / f"topic-{idx:02d}-{cluster_dir_name}"
            cluster_dir.mkdir(exist_ok=True)

            # Copy cluster topic image
            self.copy_topic_image(cluster_dir_name, cluster_dir, "cluster")

            # Create cluster topic.md
            with open(cluster_dir / "topic.md", 'w') as f:
                f.write(f"# {cluster_name}\n\n\n")

            # Sort modules in cluster alphabetically by module name
            # Get module names for sorting
            module_with_names = []
            for module_code in module_codes:
                descriptor = self.descriptors.get(module_code)
                if descriptor:
                    name = descriptor.get('full title', module_code)
                    module_with_names.append((module_code, name))

            # Sort by name
            sorted_modules = [code for code, name in sorted(module_with_names, key=lambda x: x[1])]

            for mod_idx, module_code in enumerate(sorted_modules, 1):
                module = self.modules.get(module_code)
                descriptor = self.descriptors.get(module_code)

                if not descriptor:
                    continue

                module_name = self.sanitize_filename(descriptor.get('full title', module_code))
                note_dir_name = f"note-{mod_idx:02d}-note-{mod_idx:02d}-{module_name}"
                note_dir = cluster_dir / note_dir_name
                note_dir.mkdir(exist_ok=True)

                # Store the path mapping for weburl generation
                relative_path = f"/note/{self.tutors_course_id}/unit-2-clusters/topic-{idx:02d}-{cluster_dir_name}/{note_dir_name}"
                self.module_to_cluster_path[module_code] = relative_path

                # Create archives directory
                archives_dir = note_dir / "archives"
                archives_dir.mkdir(exist_ok=True)

                # Copy PDF if exists
                pdf_source = self.source_dir / "descriptors" / "pdf" / f"{module_code}.pdf"
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
        print("SETU Module Catalogue Generator")
        print("=" * 60)

        # Load all data
        self.load_data()

        # Copy or create required course files first
        self.copy_course_files()

        # Clean output (preserve certain files)
        print("\nCleaning output directory...")
        self.clean_output()

        # Generate structures (clusters first to build path mapping)
        self.generate_clusters()
        self.generate_programmes()

        print("\n" + "=" * 60)
        print("Generation complete!")
        print("=" * 60)
        print(f"\nOutput directory: {self.output_dir}")
        print(f"- Programmes: unit-1-programmes")
        print(f"- Clusters: unit-2-clusters")


if __name__ == "__main__":
    import sys
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "tutors-catalogue/tutors"
    generator = CatalogueGenerator(output_dir=output_dir)
    generator.generate()
