# unDraw Image Download Guide

Since unDraw doesn't offer a public API for automated downloads, here's a manual guide to download the appropriate illustrations for your clusters and programmes.

## Download Instructions

1. Visit [undraw.co/illustrations](https://undraw.co/illustrations)
2. Set the color picker to your brand color: `#014771` (SETU blue)
3. Search for each illustration name below and download the SVG
4. Save to the specified directory with the exact filename

## Cluster Illustrations

Download these to: `module-catalogue/images/clusters/`

| Cluster Name | Search Term | Filename |
|--------------|-------------|----------|
| Automotive, Automation and IoT | "connected world" or "IoT" | `Automotive_Automation_and_IoT.svg` |
| Business | "business plan" or "business" | `Business.svg` |
| Database and Analytics | "data processing" or "analytics" | `Database_and_Analytics.svg` |
| Electronics | "circuit board" or "electronics" | `Electronics.svg` |
| Engineering | "engineering team" or "engineering" | `Engineering.svg` |
| Forensics and Security | "security on" or "security" | `Forensics_and_Security.svg` |
| Game Development | "gaming" or "game" | `Game_Development.svg` |
| Graphic Design and Animation | "design thinking" or "designer" | `Graphic_Design_and_Animation.svg` |
| Humanities | "professor" or "teaching" | `Humanities.svg` |
| Information Systems and Modelling | "organize data" or "workflow" | `Information_Systems_and_Modelling.svg` |
| Mathematics and Physics | "calculator" or "mathematics" | `Mathematics_and_Physics.svg` |
| Media Production | "video files" or "media" | `Media_Production.svg` |
| Networks and Cloud | "cloud sync" or "cloud" | `Networks_and_Cloud.svg` |
| Professional Skills | "interview" or "presentation" | `Professional_Skills.svg` |
| Software and Web Development | "programming" or "code" | `Software_and_Web_Development.svg` |
| Sports Technology | "fitness tracker" or "fitness" | `Sports_Technology.svg` |

## Programme Illustrations

Download these to: `module-catalogue/images/programmes/`

| Programme Code | Programme Name | Search Term | Filename |
|----------------|----------------|-------------|----------|
| WD_KINFT_D | BSc in Information Technology | "developer activity" | `WD_KINFT_D.svg` |
| WD_KINTE_B | BSc (Hons) in Information Technology | "code review" | `WD_KINTE_B.svg` |
| WD_KCRCO_B | BSc (Hons) in Creative Computing | "creative thinking" | `WD_KCRCO_B.svg` |
| WD_KCOMC_D | HDip in Science in Computer Science | "programming" | `WD_KCOMC_D.svg` |
| WD_KDEVP_B | BSc in Software Systems Development | "software engineer" | `WD_KDEVP_B.svg` |
| WD_KCOFO_B | BSc (Hons) in Computer Forensics & Security | "security" | `WD_KCOFO_B.svg` |
| WD_KCMSC_B | MSc in Computer Science | "graduation" | `WD_KCMSC_B.svg` |
| WD_KBUSY_G | HDip in Science in Business Systems Analysis | "business analytics" | `WD_KBUSY_G.svg` |
| WD_KCOSC_G | BSc (Hons) in Computer Science | "server cluster" | `WD_KCOSC_G.svg` |
| WD_KDAAN_G | HDip in Science in Data Analytics | "predictive analytics" | `WD_KDAAN_G.svg` |
| WD_KCESS_R | MSc in Computer Science (Enterprise Software) | "cloud hosting" | `WD_KCESS_R.svg` |
| WD_KISYP_R | MSc in Computing (Information Systems Processes) | "process" | `WD_KISYP_R.svg` |

## Tips

- **Customize Color**: Always set the color picker to `#014771` before downloading
- **SVG Format**: Make sure to download as SVG (not PNG) for scalability
- **Exact Filenames**: Use the exact filenames listed above
- **Alternative Search**: If the exact search term doesn't match, browse similar illustrations
- **Batch Download**: You can open multiple tabs to speed up the process

## After Downloading

Once all images are downloaded:

```bash
# Regenerate the catalogue
python3 generate-catalogue.py

# Build tutors
cd tutors
deno run -A jsr:@tutors/tutors
```

## Alternative: Use Browser Extension

Consider using a browser extension like "DownThemAll!" to batch download if you find a pattern in the unDraw URLs.
