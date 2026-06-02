#!/usr/bin/env python3
"""
Copy Flowbite illustrations to project directories
Using illustrations from the cloned repository
"""

import shutil
from pathlib import Path

# Base path to cloned repository
FLOWBITE_BASE = Path("/tmp/flowbite-illustrations/src/3d/light")

# Mapping clusters to available Flowbite illustrations
cluster_mappings = {
    "Automotive_Automation_and_IoT": "man-car-service-repairing.svg",
    "Business": "employees-working-charts.svg",
    "Database_and_Analytics": "woman-laptop-chart.svg",
    "Electronics": "man-adjusting-settings.svg",
    "Engineering": "man-repairing.svg",
    "Forensics_and_Security": "woman-cyber-security.svg",
    "Game_Development": "gaming-controller-ghosts.svg",
    "Graphic_Design_and_Animation": "man-drawing.svg",
    "Humanities": "woman-tutoring-classroom.svg",
    "Information_Systems_and_Modelling": "employees-working-office.svg",
    "Mathematics_and_Physics": "woman-laptop-chart.svg",  # Using analytics as substitute
    "Media_Production": "smartphone-application-features.svg",
    "Networks_and_Cloud": "woman-working-servers.svg",
    "Professional_Skills": "group-brainstorming.svg",
    "Software_and_Web_Development": "man-working-programs.svg",
    "Sports_Technology": "woman-fitness-gym.svg",
}

# Mapping programmes to available Flowbite illustrations
programme_mappings = {
    "WD_KINFT_D": "woman-laptop-sitting.svg",  # BSc in Information Technology
    "WD_KINTE_B": "woman-laptop-standing.svg",  # BSc (Hons) in Information Technology
    "WD_KCRCO_B": "man-drawing.svg",  # BSc (Hons) in Creative Computing
    "WD_KCOMC_D": "man-working-programs.svg",  # HDip in Science in Computer Science
    "WD_KDEVP_B": "employees-working-office.svg",  # BSc in Software Systems Development
    "WD_KCOFO_B": "woman-cyber-security.svg",  # BSc (Hons) in Computer Forensics & Security
    "WD_KCMSC_B": "woman-rocket-flying.svg",  # MSc in Computer Science
    "WD_KBUSY_G": "employees-working-charts.svg",  # HDip in Science in Business Systems Analysis
    "WD_KCOSC_G": "group-brainstorming.svg",  # BSc (Hons) in Computer Science
    "WD_KDAAN_G": "smartphone-charts.svg",  # HDip in Science in Data Analytics
    "WD_KCESS_R": "woman-working-servers.svg",  # MSc in Computer Science (Enterprise Software)
    "WD_KISYP_R": "people-connecting.svg",  # MSc in Computing (Information Systems Processes)
}

def copy_illustration(source_filename, dest_path):
    """Copy illustration from cloned repo to destination"""
    source_path = FLOWBITE_BASE / source_filename
    try:
        if source_path.exists():
            shutil.copy(source_path, dest_path)
            print(f"✓ Copied: {dest_path.name}")
            return True
        else:
            print(f"✗ Source not found: {source_filename}")
            return False
    except Exception as e:
        print(f"✗ Failed to copy {dest_path.name}: {e}")
        return False

def main():
    """Copy all mapped illustrations"""

    # Check if repository exists
    if not FLOWBITE_BASE.exists():
        print("Error: Flowbite repository not found at /tmp/flowbite-illustrations")
        print("Please run: git clone https://github.com/themesberg/flowbite-illustrations.git /tmp/flowbite-illustrations")
        return

    # Create directories
    cluster_dir = Path("module-catalogue/images/clusters")
    programme_dir = Path("module-catalogue/images/programmes")

    cluster_dir.mkdir(parents=True, exist_ok=True)
    programme_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Copying Flowbite Illustrations")
    print("=" * 60)
    print("Repository: github.com/themesberg/flowbite-illustrations")
    print("License: MIT")
    print()

    # Copy cluster images
    print("\n📁 Copying Cluster Images...")
    print("-" * 60)
    success_count = 0

    for cluster_name, source_file in cluster_mappings.items():
        dest_path = cluster_dir / f"{cluster_name}.svg"
        if copy_illustration(source_file, dest_path):
            success_count += 1

    print(f"\nCluster images: {success_count}/{len(cluster_mappings)} copied")

    # Copy programme images
    print("\n🎓 Copying Programme Images...")
    print("-" * 60)
    success_count = 0

    for prog_code, source_file in programme_mappings.items():
        dest_path = programme_dir / f"{prog_code}.svg"
        if copy_illustration(source_file, dest_path):
            success_count += 1

    print(f"\nProgramme images: {success_count}/{len(programme_mappings)} copied")

    print("\n" + "=" * 60)
    print("✓ Copy complete!")
    print("=" * 60)
    print("\nLicense: MIT (Free for commercial use)")
    print("Attribution: Flowbite (optional but appreciated)")
    print("\nNext steps:")
    print("1. Review the copied SVG files in:")
    print("   - module-catalogue/images/clusters/")
    print("   - module-catalogue/images/programmes/")
    print("2. Run: python3 generate-catalogue.py")
    print("3. Run: cd tutors && deno run -A jsr:@tutors/tutors")

if __name__ == "__main__":
    main()
