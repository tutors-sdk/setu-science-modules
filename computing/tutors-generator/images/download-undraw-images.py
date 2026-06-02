#!/usr/bin/env python3
"""
Download unDraw illustrations for clusters and programmes
"""

import urllib.request
import os
from pathlib import Path

# SETU brand color (you can customize this)
BRAND_COLOR = "014771"  # SETU blue - change as needed

def download_svg(url, output_path):
    """Download SVG file from unDraw"""
    try:
        urllib.request.urlretrieve(url, output_path)
        print(f"✓ Downloaded: {output_path}")
        return True
    except Exception as e:
        print(f"✗ Failed to download {output_path}: {e}")
        return False

# Cluster illustrations mapping
# Format: cluster_name -> (undraw_illustration_name, output_filename)
cluster_images = {
    "Automotive, Automation and IoT": ("connected-world", "Automotive_Automation_and_IoT.svg"),
    "Business": ("business-plan", "Business.svg"),
    "Database and Analytics": ("data-processing", "Database_and_Analytics.svg"),
    "Electronics": ("circuit-board", "Electronics.svg"),
    "Engineering": ("engineering-team", "Engineering.svg"),
    "Forensics and Security": ("security-on", "Forensics_and_Security.svg"),
    "Game Development": ("gaming", "Game_Development.svg"),
    "Graphic Design and Animation": ("design-thinking", "Graphic_Design_and_Animation.svg"),
    "Humanities": ("professor", "Humanities.svg"),
    "Information Systems and Modelling": ("organize-data", "Information_Systems_and_Modelling.svg"),
    "Mathematics and Physics": ("calculator", "Mathematics_and_Physics.svg"),
    "Media Production": ("video-files", "Media_Production.svg"),
    "Networks and Cloud": ("cloud-sync", "Networks_and_Cloud.svg"),
    "Professional Skills": ("interview", "Professional_Skills.svg"),
    "Software and Web Development": ("programming", "Software_and_Web_Development.svg"),
    "Sports Technology": ("fitness-tracker", "Sports_Technology.svg"),
}

# Programme illustrations mapping
# Format: programme_code -> (undraw_illustration_name, output_filename)
programme_images = {
    "WD_KINFT_D": ("developer-activity", "WD_KINFT_D.svg"),  # BSc in Information Technology
    "WD_KINTE_B": ("code-review", "WD_KINTE_B.svg"),  # BSc (Hons) in Information Technology
    "WD_KCRCO_B": ("creative-thinking", "WD_KCRCO_B.svg"),  # BSc (Hons) in Creative Computing
    "WD_KCOMC_D": ("programming", "WD_KCOMC_D.svg"),  # HDip in Science in Computer Science
    "WD_KDEVP_B": ("software-engineer", "WD_KDEVP_B.svg"),  # BSc in Software Systems Development
    "WD_KCOFO_B": ("security", "WD_KCOFO_B.svg"),  # BSc (Hons) in Computer Forensics & Security
    "WD_KCMSC_B": ("graduation", "WD_KCMSC_B.svg"),  # MSc in Computer Science
    "WD_KBUSY_G": ("business-analytics", "WD_KBUSY_G.svg"),  # HDip in Science in Business Systems Analysis
    "WD_KCOSC_G": ("server-cluster", "WD_KCOSC_G.svg"),  # BSc (Hons) in Computer Science
    "WD_KDAAN_G": ("predictive-analytics", "WD_KDAAN_G.svg"),  # HDip in Science in Data Analytics
    "WD_KCESS_R": ("cloud-hosting", "WD_KCESS_R.svg"),  # MSc in Computer Science (Enterprise Software)
    "WD_KISYP_R": ("process", "WD_KISYP_R.svg"),  # MSc in Computing (Information Systems Processes)
}

def main():
    """Download all illustrations"""

    # Create directories if they don't exist
    cluster_dir = Path("module-catalogue/images/clusters")
    programme_dir = Path("module-catalogue/images/programmes")

    cluster_dir.mkdir(parents=True, exist_ok=True)
    programme_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Downloading unDraw Illustrations")
    print("=" * 60)
    print(f"Brand color: #{BRAND_COLOR}")
    print()

    # Download cluster images
    print("\n📁 Downloading Cluster Images...")
    print("-" * 60)
    success_count = 0
    for cluster_name, (illustration, filename) in cluster_images.items():
        url = f"https://undraw.co/api/illustrations/{illustration}?color={BRAND_COLOR}&format=svg"
        output_path = cluster_dir / filename
        if download_svg(url, output_path):
            success_count += 1

    print(f"\nCluster images: {success_count}/{len(cluster_images)} downloaded")

    # Download programme images
    print("\n🎓 Downloading Programme Images...")
    print("-" * 60)
    success_count = 0
    for prog_code, (illustration, filename) in programme_images.items():
        url = f"https://undraw.co/api/illustrations/{illustration}?color={BRAND_COLOR}&format=svg"
        output_path = programme_dir / filename
        if download_svg(url, output_path):
            success_count += 1

    print(f"\nProgramme images: {success_count}/{len(programme_images)} downloaded")

    print("\n" + "=" * 60)
    print("✓ Download complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review the downloaded SVG files")
    print("2. Adjust BRAND_COLOR if needed and re-run")
    print("3. Run: python3 generate-catalogue.py")
    print("4. Run: cd tutors && deno run -A jsr:@tutors/tutors")

if __name__ == "__main__":
    main()
