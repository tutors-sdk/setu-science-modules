# Alternative Illustration Libraries Research

## Recommendation: illlustrations.co

After researching alternatives to Flowbite and unDraw, **illlustrations.co** emerges as an excellent third option.

### Overview

- **Website:** [illlustrations.co](https://illlustrations.co/)
- **GitHub:** [realvjy/illlustrations](https://github.com/realvjy/illlustrations)
- **Creator:** Vijay Verma
- **Collection:** 120+ open-source illustrations
- **License:** Free for commercial and personal use, no attribution required

## Key Features

### ✅ Programmatic Access
- **GitHub Releases:** Direct download of entire collection
- **Format:** SVG, PNG, AI, EPS, Figma
- **Easy automation:** Can script downloads from GitHub

### ✅ Superior Licensing
- **No attribution required** (better than Storyset)
- **Commercial use allowed**
- **Modify freely**
- **Redistribute allowed**
- **Can even sell** (most permissive license)

### ✅ Multiple Download Methods
1. GitHub releases (bulk download)
2. Gumroad (all formats)
3. Individual SVG/PNG downloads
4. Figma plugin
5. Dropbox (EPS files)

### ✅ Good Variety
- 120+ illustrations
- Multiple styles and themes
- Tech, office, people, seasonal
- COVID/WFH specific illustrations
- Education relevant content

## Comparison with Current Solutions

### vs. Flowbite (Current)
| Feature | Flowbite | illlustrations.co |
|---------|----------|-------------------|
| License | MIT | Even more permissive |
| Style | 3D characters | Flat, colorful |
| Count | 54 illustrations | 120+ illustrations |
| Automation | GitHub clone | GitHub releases + direct URLs |
| Attribution | Optional | Not required |
| Customization | None | Color customizable online |

**Verdict:** illlustrations.co has better variety and easier bulk download

### vs. unDraw
| Feature | unDraw | illlustrations.co |
|---------|--------|-------------------|
| License | CC0 | Free commercial use |
| Style | Flat, customizable color | Flat, colorful |
| Count | 500+ illustrations | 120+ illustrations |
| Automation | ❌ No API | ✅ GitHub releases |
| Attribution | Not required | Not required |
| Download | Manual only | Programmatic ✅ |

**Verdict:** illlustrations.co wins on automation, unDraw wins on variety

### vs. Storyset
| Feature | Storyset | illlustrations.co |
|---------|----------|-------------------|
| License | Freemium (attribution) | Completely free |
| Style | Multiple styles | Single consistent style |
| Count | Thousands | 120+ |
| Automation | ❌ Limited | ✅ GitHub releases |
| Attribution | Required (free tier) | Not required |
| Customization | Extensive online | Basic color changes |

**Verdict:** illlustrations.co better for open-source projects (no attribution), Storyset better for variety

### vs. OpenDoodles
| Feature | OpenDoodles | illlustrations.co |
|---------|-------------|-------------------|
| License | CC0 | Free commercial use |
| Style | Sketchy/hand-drawn | Flat, polished |
| Count | Limited | 120+ |
| Automation | ✅ Dropbox | ✅ GitHub releases |
| Attribution | Not required | Not required |
| Professional | Casual/friendly | More professional |

**Verdict:** illlustrations.co more professional, OpenDoodles more casual

## Why Choose illlustrations.co?

### 1. **Best Automation**
Unlike unDraw and Storyset, illlustrations.co offers:
- Direct GitHub releases
- Bulk downloads
- Easy scripting

### 2. **Most Permissive License**
- No attribution needed
- Free commercial use
- Can redistribute
- Can modify
- Can even sell

### 3. **Professional Quality**
- Consistent flat design style
- Modern, colorful aesthetic
- Professional enough for academic use
- Friendly enough for students

### 4. **Easy Integration**
- SVG format (scalable)
- Direct URLs for each illustration
- GitHub-hosted (reliable)
- No API rate limits

## Implementation Options

### Option A: GitHub Releases Download
```bash
# Download entire collection
wget https://github.com/realvjy/illlustrations/releases/download/v1.0.3/illlustrations-1.0.3.zip

# Extract
unzip illlustrations-1.0.3.zip -d /tmp/illlustrations

# Copy selected images
python3 copy-illlustrations.py
```

### Option B: Direct URL Download
Each illustration has a direct URL pattern:
```
https://illlustrations.co/static/[name].svg
```

### Option C: Gumroad Bulk Download
Download all formats at once via Gumroad (free):
```
https://s.vjy.me/illlustrations
```

## Available Categories

Relevant for module catalogue:

- **Technology** - Computer, coding, tech devices
- **Office/Work** - Business, collaboration, meetings  
- **Education** - Learning, teaching, studying
- **People** - Various characters and poses
- **Abstract** - Concepts, ideas, processes
- **Seasonal** - Various themed illustrations

## Sample Illustrations

### Suitable for Clusters:
- **Software Development:** Developer at computer, coding illustrations
- **Business:** Office work, meetings, presentations
- **Database:** Data organization, analytics
- **Security:** Privacy, protection concepts
- **Game Development:** Entertainment, gaming
- **Graphic Design:** Creative work, design tools
- **Networks:** Connectivity, communication
- **Professional Skills:** Collaboration, teamwork

## Implementation Script

Create `tutors-generator/images/download-illlustrations.py`:

```python
#!/usr/bin/env python3
"""
Download illlustrations.co SVGs from GitHub releases
"""

import urllib.request
import zipfile
import os
from pathlib import Path

RELEASE_URL = "https://github.com/realvjy/illlustrations/releases/download/v1.0.3/illlustrations-1.0.3.zip"
TEMP_DIR = "/tmp/illlustrations"

# Mapping clusters to illlustrations
cluster_mappings = {
    "Automotive_Automation_and_IoT": "car-service.svg",
    "Business": "business-meeting.svg",
    "Database_and_Analytics": "data-analysis.svg",
    # ... etc
}

def download_release():
    """Download and extract release"""
    zip_path = f"{TEMP_DIR}.zip"
    urllib.request.urlretrieve(RELEASE_URL, zip_path)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(TEMP_DIR)

def copy_illustrations():
    """Copy mapped illustrations"""
    # Implementation here
    pass

if __name__ == "__main__":
    download_release()
    copy_illustrations()
```

## Recommended Approach

**For this project:** Use illlustrations.co as a **third option** alongside Flowbite:

1. **Primary:** Flowbite (current, working well)
2. **Alternative:** illlustrations.co (better automation, more variety)
3. **Fallback:** unDraw (manual download, largest collection)

### Why Keep Flowbite?
- Already implemented
- Good 3D style
- MIT licensed
- Works well

### Why Add illlustrations.co?
- More variety (120 vs 54)
- Easier bulk download
- Better licensing (no attribution)
- Alternative style option

## Next Steps

### To Implement illlustrations.co:

1. **Create download script:**
   ```bash
   # Create new script
   vim tutors-generator/images/download-illlustrations.py
   ```

2. **Map illustrations to clusters/programmes:**
   - Browse illlustrations.co
   - Identify suitable illustrations
   - Update mapping dictionary

3. **Download and copy:**
   ```bash
   python3 tutors-generator/images/download-illlustrations.py
   ```

4. **Regenerate catalogue:**
   ```bash
   ./generate
   ```

## Licensing Summary

### illlustrations.co
- ✅ Free for commercial use
- ✅ Free for personal use
- ✅ No attribution required
- ✅ Can modify
- ✅ Can redistribute
- ✅ Can sell

This is **more permissive** than:
- Flowbite (MIT - requires license notice)
- Storyset (requires attribution on free tier)
- Comparable to: unDraw (CC0), OpenDoodles (CC0)

## Resources

### Official Sites
- [illlustrations.co](https://illlustrations.co/) - Main website
- [GitHub Repository](https://github.com/realvjy/illlustrations) - Source code and releases
- [Gumroad Download](https://s.vjy.me/illlustrations) - Bulk download
- [Figma Community](https://www.figma.com/@realvjy) - Figma plugin

### Documentation
- [License Information](https://illlustrations.co/license)
- [GitHub Releases](https://github.com/realvjy/illlustrations/releases)

### Other Resources Researched
- [Storyset](https://storyset.com/) - Freemium, requires attribution
- [Blush](https://blush.design/) - Freemium, PNG/SVG
- [OpenDoodles](https://www.opendoodles.com/) - CC0, sketchy style
- [LukaszAdam](https://lukaszadam.com/illustrations) - CC0, limited collection

## Conclusion

**illlustrations.co** is an excellent alternative that combines:
- ✅ Easy programmatic access (better than unDraw, Storyset)
- ✅ Permissive licensing (no attribution needed)
- ✅ Good variety (120+ illustrations)
- ✅ Professional quality
- ✅ Reliable hosting (GitHub)
- ✅ Multiple download options

**Recommendation:** Implement as an alternative option alongside Flowbite to give more illustration variety and style choices.

---

*Research completed: June 1, 2026*
*illlustrations.co recommended as third option after Flowbite and unDraw*

## Sources
- [illlustrations.co Official Site](https://illlustrations.co/)
- [Storyset](https://storyset.com/)
- [Storyset Education](https://storyset.com/education)
- [Storyset Technology](https://storyset.com/technology)
- [Blush Illustrations](https://blush.design/)
- [OpenDoodles](https://www.opendoodles.com/)
- [IconScout Computer Science](https://iconscout.com/illustrations/computer-science)
- [Free Illustration Sites 2026](https://getillustrations.com/blog/top-100-websites-for-free-high-quality-vector-illustrations-2025-ultimate-edition/)
- [GitHub awesome-illustrations](https://github.com/MrPeker/awesome-illustrations)
- [Best Open Source Illustration Libraries](https://www.toools.design/free-open-source-illustrations)
