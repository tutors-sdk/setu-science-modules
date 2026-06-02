#!/usr/bin/env python3
"""
Download and copy illlustrations.co SVGs for clusters and programmes
"""

import urllib.request
import shutil
from pathlib import Path

# Base URL for direct SVG downloads from illlustrations.co
BASE_URL = "https://illlustrations.co/static/"

# Mapping clusters to illlustrations
# Based on available illustrations from the collection
cluster_mappings = {
    "Automotive_Automation_and_IoT": "day14-forklift.svg",
    "Business": "105-freelancer.svg",
    "Database_and_Analytics": "day44-hard-disk.svg",
    "Electronics": "114-retro-tv.svg",
    "Engineering": "day46-experiment-lab.svg",
    "Forensics_and_Security": "day5-vault.svg",
    "Game_Development": "day2-gaming-console.svg",
    "Graphic_Design_and_Animation": "day70-designer-tool-wacom.svg",
    "Humanities": "106-italy.svg",
    "Information_Systems_and_Modelling": "113-workstation.svg",
    "Mathematics_and_Physics": "day37-calculator.svg",
    "Media_Production": "day4-polaroid.svg",
    "Networks_and_Cloud": "109-map-location.svg",
    "Professional_Skills": "day92-freelancing.svg",
    "Software_and_Web_Development": "111-coding.svg",
    "Sports_Technology": "101-gym-guy.svg",
}

# Mapping programmes to illlustrations
programme_mappings = {
    "WD_KINFT_D": "119-working.svg",  # BSc in Information Technology
    "WD_KINTE_B": "day95-app-development.svg",  # BSc (Hons) in Information Technology
    "WD_KCRCO_B": "day94-ui-ux.svg",  # BSc (Hons) in Creative Computing
    "WD_KCOMC_D": "day93-programing.svg",  # HDip in Science in Computer Science
    "WD_KDEVP_B": "112-installing.svg",  # BSc in Software Systems Development
    "WD_KCOFO_B": "day6-open-vault.svg",  # BSc (Hons) in Computer Forensics & Security
    "WD_KCMSC_B": "day11-blackboard.svg",  # MSc in Computer Science
    "WD_KBUSY_G": "day13-it-girl.svg",  # HDip in Science in Business Systems Analysis
    "WD_KCOSC_G": "day42-imac.svg",  # BSc (Hons) in Computer Science
    "WD_KDAAN_G": "day44-hard-disk.svg",  # HDip in Science in Data Analytics (reuse)
    "WD_KCESS_R": "121-work-from-home-video-chat.svg",  # MSc in Computer Science (Enterprise)
    "WD_KISYP_R": "122-work-from-home-chat.svg",  # MSc in Computing (Info Systems)
}

def download_svg(illustration_name, output_path):
    """Download SVG from illlustrations.co"""
    url = f"{BASE_URL}{illustration_name}"
    try:
        urllib.request.urlretrieve(url, output_path)
        print(f"✓ Downloaded: {output_path.name}")
        return True
    except Exception as e:
        print(f"✗ Failed {output_path.name}: {e}")
        return False

def main():
    """Download all mapped illustrations"""

    # Create directories
    cluster_dir = Path("module-catalogue/images/clusters")
    programme_dir = Path("module-catalogue/images/programmes")

    cluster_dir.mkdir(parents=True, exist_ok=True)
    programme_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Downloading illlustrations.co")
    print("=" * 60)
    print("Source: illlustrations.co")
    print("License: Free for commercial/personal use, no attribution")
    print()

    # Download cluster images
    print("\n📁 Downloading Cluster Images...")
    print("-" * 60)
    success_count = 0

    for cluster_name, illustration in cluster_mappings.items():
        dest_path = cluster_dir / f"{cluster_name}.svg"
        if download_svg(illustration, dest_path):
            success_count += 1

    print(f"\nCluster images: {success_count}/{len(cluster_mappings)} downloaded")

    # Download programme images
    print("\n🎓 Downloading Programme Images...")
    print("-" * 60)
    success_count = 0

    for prog_code, illustration in programme_mappings.items():
        dest_path = programme_dir / f"{prog_code}.svg"
        if download_svg(illustration, dest_path):
            success_count += 1

    print(f"\nProgramme images: {success_count}/{len(programme_mappings)} downloaded")

    print("\n" + "=" * 60)
    print("✓ Download complete!")
    print("=" * 60)
    print("\nLicense: illlustrations.co")
    print("Free for commercial and personal use")
    print("No attribution required")
    print("\nNext steps:")
    print("1. Review the downloaded SVG files")
    print("2. Run: ./generate")
    print("3. Run: cd tutors-catalogue/tutors && deno run -A jsr:@tutors/tutors")

if __name__ == "__main__":
    main()
