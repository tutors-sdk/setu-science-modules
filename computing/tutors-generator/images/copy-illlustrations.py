#!/usr/bin/env python3
"""
Copy illlustrations from cloned repository to module catalogue
"""

import shutil
from pathlib import Path

# Base path to cloned repository
SOURCE_BASE = Path("/tmp/illlustrations/content/illlustrations")

# Mapping clusters to illlustrations (folder / filename)
cluster_mappings = {
    "Automotive_Automation_and_IoT": "day-14/day14-forklift.svg",
    "Business": "105/105-freelancer.svg",
    "Database_and_Analytics": "day-44/day44-hdd.svg",
    "Electronics": "114/114-retro-tv.svg",
    "Engineering": "day-46/day46-experiment-lab.svg",
    "Forensics_and_Security": "day-5/day5-vault.svg",
    "Game_Development": "day-2/day2-gaming-console.svg",
    "Graphic_Design_and_Animation": "day-70/day70-designer-fav-tool-wacom.svg",
    "Humanities": "106/106-italy.svg",
    "Information_Systems_and_Modelling": "113/113-workstation.svg",
    "Mathematics_and_Physics": "day-37/day37-calculator.svg",
    "Media_Production": "day-4/day4-polariod.svg",
    "Networks_and_Cloud": "109/109-map-location.svg",
    "Professional_Skills": "day-92/day92-freelancing.svg",
    "Software_and_Web_Development": "111/111-coding.svg",
    "Sports_Technology": "101/101-gym-guy.svg",
}

# Mapping programmes to illlustrations
programme_mappings = {
    "WD_KINFT_D": "119/119-working.svg",
    "WD_KINTE_B": "day-95/day95-app-development.svg",
    "WD_KCRCO_B": "day-94/day94-ui-ux.svg",
    "WD_KCOMC_D": "day-93/day93-programing.svg",
    "WD_KDEVP_B": "112/112-installing.svg",
    "WD_KCOFO_B": "day-6/day6-open-vault.svg",
    "WD_KCMSC_B": "day-11/day11-blackboard.svg",
    "WD_KBUSY_G": "day-13/day13-it-girl.svg",
    "WD_KCOSC_G": "day-42/day42-imac.svg",
    "WD_KDAAN_G": "day-43/day43-ram.svg",
    "WD_KCESS_R": "121/121-work-from-home-1.svg",
    "WD_KISYP_R": "122/122-work-from-home-2.svg",
}

def copy_illustration(source_path, dest_path):
    """Copy illustration file"""
    source_file = SOURCE_BASE / source_path
    try:
        if source_file.exists():
            shutil.copy(source_file, dest_path)
            print(f"✓ Copied: {dest_path.name}")
            return True
        else:
            print(f"✗ Source not found: {source_path}")
            return False
    except Exception as e:
        print(f"✗ Failed to copy {dest_path.name}: {e}")
        return False

def main():
    """Copy all mapped illustrations"""

    # Check if repository exists
    if not SOURCE_BASE.exists():
        print("Error: illlustrations repository not found at /tmp/illlustrations")
        print("Please run: cd /tmp && git clone https://github.com/realvjy/illlustrations.git")
        return

    # Create directories
    cluster_dir = Path("module-catalogue/images/clusters")
    programme_dir = Path("module-catalogue/images/programmes")

    cluster_dir.mkdir(parents=True, exist_ok=True)
    programme_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Copying illlustrations.co Illustrations")
    print("=" * 60)
    print("Repository: github.com/realvjy/illlustrations")
    print("License: Free for commercial/personal, no attribution required")
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
    print("\nLicense: illlustrations.co")
    print("Free for commercial and personal use")
    print("No attribution required")
    print("\nNext steps:")
    print("1. Review: ls module-catalogue/images/clusters/")
    print("2. Run: ./generate")
    print("3. Build: cd tutors-catalogue/tutors && deno run -A jsr:@tutors/tutors")

if __name__ == "__main__":
    main()
