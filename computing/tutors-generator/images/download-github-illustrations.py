#!/usr/bin/env python3
"""
Download open-source illustrations from GitHub repositories
Using Flowbite Illustrations (MIT License)
"""

import urllib.request
import json
import os
from pathlib import Path

# Flowbite Illustrations - MIT License
# GitHub: https://github.com/themesberg/flowbite-illustrations
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/themesberg/flowbite-illustrations/main"

# Mapping of clusters to Flowbite illustration filenames
# Based on browsing https://flowbite.com/illustrations/
cluster_mappings = {
    "Automotive_Automation_and_IoT": "computers/car-wash.svg",
    "Business": "business/business-deal.svg",
    "Database_and_Analytics": "computers/data-report.svg",
    "Electronics": "computers/circuit.svg",
    "Engineering": "computers/engineer.svg",
    "Forensics_and_Security": "computers/security.svg",
    "Game_Development": "computers/gaming.svg",
    "Graphic_Design_and_Animation": "computers/design-thinking.svg",
    "Humanities": "education/teacher.svg",
    "Information_Systems_and_Modelling": "computers/workflow.svg",
    "Mathematics_and_Physics": "education/mathematics.svg",
    "Media_Production": "computers/video-streaming.svg",
    "Networks_and_Cloud": "computers/cloud-server.svg",
    "Professional_Skills": "business/meeting.svg",
    "Software_and_Web_Development": "computers/coding.svg",
    "Sports_Technology": "health/fitness.svg",
}

# Mapping of programmes to Flowbite illustration filenames
programme_mappings = {
    "WD_KINFT_D": "computers/developer.svg",
    "WD_KINTE_B": "computers/programmer.svg",
    "WD_KCRCO_B": "computers/creative-design.svg",
    "WD_KCOMC_D": "computers/programming.svg",
    "WD_KDEVP_B": "computers/software-development.svg",
    "WD_KCOFO_B": "computers/cyber-security.svg",
    "WD_KCMSC_B": "education/graduation.svg",
    "WD_KBUSY_G": "business/analytics.svg",
    "WD_KCOSC_G": "computers/server.svg",
    "WD_KDAAN_G": "computers/data-analysis.svg",
    "WD_KCESS_R": "computers/cloud-computing.svg",
    "WD_KISYP_R": "business/process.svg",
}

def download_svg(github_path, output_path):
    """Download SVG file from GitHub"""
    url = f"{GITHUB_RAW_BASE}/{github_path}"
    try:
        urllib.request.urlretrieve(url, output_path)
        print(f"✓ Downloaded: {output_path.name}")
        return True
    except Exception as e:
        print(f"✗ Failed {output_path.name}: {e}")
        # Try alternative path (sometimes files are in different subdirectories)
        return False

def try_alternative_illustrations(search_term, output_path, category="computers"):
    """Try to find alternative illustrations based on search term"""
    alternatives = {
        "Automotive_Automation_and_IoT": ["computers/connected-world.svg", "computers/iot.svg", "business/logistics.svg"],
        "Database_and_Analytics": ["computers/database.svg", "computers/analytics.svg", "business/data-report.svg"],
        "Electronics": ["computers/technology.svg", "computers/devices.svg"],
        "Engineering": ["business/team-work.svg", "computers/engineering-team.svg"],
        "Game_Development": ["computers/game.svg", "computers/entertainment.svg"],
        "Mathematics_and_Physics": ["education/science.svg", "education/learning.svg"],
        "Media_Production": ["computers/media.svg", "computers/content-creation.svg"],
    }

    for alt_path in alternatives.get(search_term, []):
        url = f"{GITHUB_RAW_BASE}/{alt_path}"
        try:
            urllib.request.urlretrieve(url, output_path)
            print(f"✓ Downloaded alternative: {output_path.name} from {alt_path}")
            return True
        except:
            continue
    return False

def main():
    """Download all illustrations from GitHub"""

    # Create directories
    cluster_dir = Path("module-catalogue/images/clusters")
    programme_dir = Path("module-catalogue/images/programmes")

    cluster_dir.mkdir(parents=True, exist_ok=True)
    programme_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Downloading Flowbite Illustrations from GitHub")
    print("=" * 60)
    print("Repository: github.com/themesberg/flowbite-illustrations")
    print("License: MIT")
    print()

    # Download cluster images
    print("\n📁 Downloading Cluster Images...")
    print("-" * 60)
    success_count = 0
    failed = []

    for cluster_name, github_path in cluster_mappings.items():
        output_path = cluster_dir / f"{cluster_name}.svg"
        if download_svg(github_path, output_path):
            success_count += 1
        elif try_alternative_illustrations(cluster_name, output_path):
            success_count += 1
        else:
            failed.append(cluster_name)

    print(f"\nCluster images: {success_count}/{len(cluster_mappings)} downloaded")
    if failed:
        print(f"Failed: {', '.join(failed)}")

    # Download programme images
    print("\n🎓 Downloading Programme Images...")
    print("-" * 60)
    success_count = 0
    failed = []

    for prog_code, github_path in programme_mappings.items():
        output_path = programme_dir / f"{prog_code}.svg"
        if download_svg(github_path, output_path):
            success_count += 1
        else:
            failed.append(prog_code)

    print(f"\nProgramme images: {success_count}/{len(programme_mappings)} downloaded")
    if failed:
        print(f"Failed: {', '.join(failed)}")

    print("\n" + "=" * 60)
    print("Download complete!")
    print("=" * 60)
    print("\nNote: Some illustrations may not exist in the repository.")
    print("You can browse available illustrations at:")
    print("https://flowbite.com/illustrations/")
    print("\nOr clone the full repository:")
    print("git clone https://github.com/themesberg/flowbite-illustrations.git")
    print("\nNext steps:")
    print("1. Review downloaded SVG files")
    print("2. Manually download any missing illustrations from flowbite.com")
    print("3. Run: python3 generate-catalogue.py")
    print("4. Run: cd tutors && deno run -A jsr:@tutors/tutors")

if __name__ == "__main__":
    main()
