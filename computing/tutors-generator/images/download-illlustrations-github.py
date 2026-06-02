#!/usr/bin/env python3
"""
Download illlustrations from GitHub releases and copy selected files
"""

import urllib.request
import zipfile
import shutil
from pathlib import Path
import os

# GitHub release URL
RELEASE_URL = "https://github.com/realvjy/illlustrations/archive/refs/heads/main.zip"
TEMP_ZIP = "/tmp/illlustrations.zip"
TEMP_DIR = "/tmp/illlustrations-main"

# Mapping clusters to illlustrations (using actual filenames from repo)
cluster_mappings = {
    "Automotive_Automation_and_IoT": "Day 14 - Forklift.svg",
    "Business": "105 - Freelancer.svg",
    "Database_and_Analytics": "Day 44 - Hard Disk.svg",
    "Electronics": "114 - Retro TV.svg",
    "Engineering": "Day 46 - Experiment Lab.svg",
    "Forensics_and_Security": "Day 5 - Vault.svg",
    "Game_Development": "Day 2 - Gaming Console.svg",
    "Graphic_Design_and_Animation": "Day 70 - Designer Tool Wacom.svg",
    "Humanities": "106 - Italy.svg",
    "Information_Systems_and_Modelling": "113 - Workstation.svg",
    "Mathematics_and_Physics": "Day 37 - Calculator.svg",
    "Media_Production": "Day 4 - Polaroid.svg",
    "Networks_and_Cloud": "109 - Map Location.svg",
    "Professional_Skills": "Day 92 - Freelancing.svg",
    "Software_and_Web_Development": "111 - Coding.svg",
    "Sports_Technology": "101 - Gym Guy.svg",
}

# Mapping programmes to illlustrations
programme_mappings = {
    "WD_KINFT_D": "119 - Working.svg",
    "WD_KINTE_B": "Day 95 - App Development.svg",
    "WD_KCRCO_B": "Day 94 - UI UX.svg",
    "WD_KCOMC_D": "Day 93 - Programing.svg",
    "WD_KDEVP_B": "112 - Installing.svg",
    "WD_KCOFO_B": "Day 6 - Open Vault.svg",
    "WD_KCMSC_B": "Day 11 - Blackboard.svg",
    "WD_KBUSY_G": "Day 13 - IT Girl.svg",
    "WD_KCOSC_G": "Day 42 - iMac.svg",
    "WD_KDAAN_G": "Day 43 - RAM.svg",
    "WD_KCESS_R": "121 - Work From Home - Video Chat.svg",
    "WD_KISYP_R": "122 - Work From Home - Chat.svg",
}

def download_release():
    """Download and extract GitHub release"""
    print("Downloading illlustrations from GitHub...")
    try:
        urllib.request.urlretrieve(RELEASE_URL, TEMP_ZIP)
        print("✓ Downloaded release archive")

        print("Extracting archive...")
        with zipfile.ZipFile(TEMP_ZIP, 'r') as zip_ref:
            zip_ref.extractall("/tmp")
        print("✓ Extracted archive")
        return True
    except Exception as e:
        print(f"✗ Failed to download/extract: {e}")
        return False

def find_svg_file(temp_dir, filename):
    """Find SVG file in extracted directory"""
    # Look in common subdirectories
    search_paths = [
        temp_dir / "svg",
        temp_dir / "SVG",
        temp_dir / "illustrations",
        temp_dir,
    ]

    for search_path in search_paths:
        if search_path.exists():
            svg_file = search_path / filename
            if svg_file.exists():
                return svg_file
            # Try recursive search
            for file in search_path.rglob(filename):
                return file
    return None

def copy_illustrations():
    """Copy mapped illustrations to destination"""
    temp_dir = Path(TEMP_DIR)

    if not temp_dir.exists():
        print(f"✗ Temp directory not found: {temp_dir}")
        return

    # Create destination directories
    cluster_dir = Path("module-catalogue/images/clusters")
    programme_dir = Path("module-catalogue/images/programmes")

    cluster_dir.mkdir(parents=True, exist_ok=True)
    programme_dir.mkdir(parents=True, exist_ok=True)

    # Copy cluster images
    print("\n📁 Copying Cluster Images...")
    print("-" * 60)
    success_count = 0

    for cluster_name, source_file in cluster_mappings.items():
        svg_path = find_svg_file(temp_dir, source_file)
        if svg_path:
            dest_path = cluster_dir / f"{cluster_name}.svg"
            shutil.copy(svg_path, dest_path)
            print(f"✓ Copied: {cluster_name}.svg")
            success_count += 1
        else:
            print(f"✗ Not found: {source_file}")

    print(f"\nCluster images: {success_count}/{len(cluster_mappings)} copied")

    # Copy programme images
    print("\n🎓 Copying Programme Images...")
    print("-" * 60)
    success_count = 0

    for prog_code, source_file in programme_mappings.items():
        svg_path = find_svg_file(temp_dir, source_file)
        if svg_path:
            dest_path = programme_dir / f"{prog_code}.svg"
            shutil.copy(svg_path, dest_path)
            print(f"✓ Copied: {prog_code}.svg")
            success_count += 1
        else:
            print(f"✗ Not found: {source_file}")

    print(f"\nProgramme images: {success_count}/{len(programme_mappings)} copied")

def main():
    """Main execution"""
    print("=" * 60)
    print("illlustrations.co Download from GitHub")
    print("=" * 60)
    print("Repository: github.com/realvjy/illlustrations")
    print("License: Free for commercial/personal, no attribution")
    print()

    if download_release():
        copy_illustrations()

        print("\n" + "=" * 60)
        print("✓ Complete!")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Review: ls module-catalogue/images/clusters/")
        print("2. Run: ./generate")
        print("3. Build: cd tutors-catalogue/tutors && deno run -A jsr:@tutors/tutors")

        # Cleanup
        print("\nCleaning up temporary files...")
        if os.path.exists(TEMP_ZIP):
            os.remove(TEMP_ZIP)
        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)
        print("✓ Cleanup complete")

if __name__ == "__main__":
    main()
