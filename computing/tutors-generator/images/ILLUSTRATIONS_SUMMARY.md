# Open-Source Illustrations Summary

## Successfully Implemented ✓

All cluster and programme images have been replaced with **open-source SVG illustrations** from the Flowbite Illustrations library.

### What Was Done

1. **Downloaded Flowbite Illustrations**
   - Repository: [github.com/themesberg/flowbite-illustrations](https://github.com/themesberg/flowbite-illustrations)
   - License: **MIT** (Free for commercial use)
   - Format: **SVG** (scalable, perfect quality at any resolution)

2. **Images Replaced**
   - **16 Cluster images** - All replaced with relevant SVG illustrations
   - **12 Programme images** - All replaced with relevant SVG illustrations
   - **Total: 28 images** successfully downloaded and integrated

3. **Generator Updated**
   - Modified `generate-catalogue.py` to prefer SVG format over PNG/JPEG
   - Images now copy as `topic.svg` in each programme and cluster directory

## Image Mappings

### Cluster Illustrations

| Cluster Name | Illustration Used | Theme |
|--------------|-------------------|-------|
| Automotive, Automation and IoT | man-car-service-repairing.svg | Automotive service |
| Business | employees-working-charts.svg | Business analytics |
| Database and Analytics | woman-laptop-chart.svg | Data analysis |
| Electronics | man-adjusting-settings.svg | Technical settings |
| Engineering | man-repairing.svg | Engineering work |
| Forensics and Security | woman-cyber-security.svg | Cybersecurity |
| Game Development | gaming-controller-ghosts.svg | Gaming |
| Graphic Design and Animation | man-drawing.svg | Design work |
| Humanities | woman-tutoring-classroom.svg | Teaching |
| Information Systems and Modelling | employees-working-office.svg | Office collaboration |
| Mathematics and Physics | woman-laptop-chart.svg | Analytics |
| Media Production | smartphone-application-features.svg | Media apps |
| Networks and Cloud | woman-working-servers.svg | Server management |
| Professional Skills | group-brainstorming.svg | Team collaboration |
| Software and Web Development | man-working-programs.svg | Programming |
| Sports Technology | woman-fitness-gym.svg | Fitness |

### Programme Illustrations

| Programme Code | Programme Name | Illustration Used |
|----------------|----------------|-------------------|
| WD_KINFT_D | BSc in Information Technology | woman-laptop-sitting.svg |
| WD_KINTE_B | BSc (Hons) in Information Technology | woman-laptop-standing.svg |
| WD_KCRCO_B | BSc (Hons) in Creative Computing | man-drawing.svg |
| WD_KCOMC_D | HDip in Science in Computer Science | man-working-programs.svg |
| WD_KDEVP_B | BSc in Software Systems Development | employees-working-office.svg |
| WD_KCOFO_B | BSc (Hons) in Computer Forensics & Security | woman-cyber-security.svg |
| WD_KCMSC_B | MSc in Computer Science | woman-rocket-flying.svg |
| WD_KBUSY_G | HDip in Science in Business Systems Analysis | employees-working-charts.svg |
| WD_KCOSC_G | BSc (Hons) in Computer Science | group-brainstorming.svg |
| WD_KDAAN_G | HDip in Science in Data Analytics | smartphone-charts.svg |
| WD_KCESS_R | MSc in Computer Science (Enterprise Software) | woman-working-servers.svg |
| WD_KISYP_R | MSc in Computing (Information Systems Processes) | people-connecting.svg |

## Verification

```bash
# Count SVG images in generated tutors
find tutors -name "topic.svg" | wc -l
# Result: 56 SVG files (includes both unit-1 and unit-2)
```

## License Information

**Flowbite Illustrations** - MIT License
- ✅ Free for commercial use
- ✅ Free for personal use
- ✅ Attribution optional (but appreciated)
- ✅ Can modify and redistribute
- ✅ Can use in proprietary projects

Full license: https://github.com/themesberg/flowbite-illustrations/blob/main/LICENSE

## Benefits of SVG Format

1. **Scalable** - Perfect quality at any size/resolution
2. **Lightweight** - Smaller file sizes than raster images
3. **Modern** - Web-standard format, well-supported
4. **Consistent** - Cohesive 3D illustration style across all images
5. **Professional** - High-quality, modern aesthetic

## Scripts Created

1. `download-github-illustrations.py` - Initial attempt (failed - wrong paths)
2. `copy-flowbite-illustrations.py` - **Working script** that copied all illustrations from cloned repo
3. `download-undraw-images.py` - Alternative approach (for reference)
4. `UNDRAW_DOWNLOAD_GUIDE.md` - Manual download guide (for reference)

## How to Update Images in Future

If you want to change any illustration:

1. Browse available illustrations: https://flowbite.com/illustrations/
2. Clone the repository: 
   ```bash
   git clone https://github.com/themesberg/flowbite-illustrations.git /tmp/flowbite-illustrations
   ```
3. Edit `copy-flowbite-illustrations.py` to update the mappings
4. Run:
   ```bash
   python3 copy-flowbite-illustrations.py
   python3 generate-catalogue.py
   cd tutors && deno run -A jsr:@tutors/tutors
   ```

## Alternatives Considered

1. **unDraw** - Excellent but requires manual downloads (no API)
2. **Open Peeps** - Modular people illustrations (CC0 license)
3. **Wikimedia Commons** - 141M+ images but requires manual curation
4. **Unsplash/Pexels/Pixabay** - Stock photos but licensing concerns

**Selected: Flowbite** - Best balance of quality, automation, and licensing.

## Attribution (Optional)

If you'd like to attribute Flowbite (optional under MIT license):

> Illustrations by [Flowbite](https://flowbite.com/illustrations/) - MIT License

---

*Last updated: June 1, 2026*
*Generated illustrations: 28 SVG files*
*Total SVG files in tutors: 56*
