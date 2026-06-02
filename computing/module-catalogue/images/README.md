# Image Library

This directory contains topic images for programmes and clusters.

## Structure

```
images/
├── programmes/      # Programme topic images
│   ├── WD_KINFT_D.png
│   ├── WD_KINTE_B.jpg
│   └── ...
└── clusters/        # Cluster topic images
    ├── Automotive_Automation_and_IoT.jpeg
    ├── Database_and_Analytics.jpeg
    └── ...
```

## Naming Convention

### Programmes
Files are named using the programme code:
- Format: `{PROGRAMME_CODE}.{ext}`
- Example: `WD_KINFT_D.png`

### Clusters
Files are named using the sanitized cluster name:
- Format: `{Cluster_Name}.{ext}`
- Example: `Software_and_Web_Development.png`
- Note: Spaces replaced with underscores, special characters removed

## File Formats

Supported formats (in order of preference):
1. **PNG** (`.png`) - Preferred for graphics with transparency
2. **JPEG** (`.jpg`, `.jpeg`) - For photographic images

The generator will check for images in this order and use the first one found.

## Image Guidelines

### Resolution
- Minimum: 800x450 pixels
- Recommended: 1200x675 pixels (16:9 aspect ratio)
- Maximum: 1920x1080 pixels

### File Size
- Target: < 200 KB per image
- Maximum: 500 KB per image

### Content
- Images should visually represent the programme or cluster theme
- Use high-quality, professional images
- Ensure images are appropriate for educational context
- Consider accessibility (sufficient contrast, clear subjects)

## Current Coverage

### Programmes
✅ All 12 programmes have images:
- WD_KINFT_D (BSc in Information Technology) - PNG
- WD_KINTE_B (BSc Hons in Information Technology) - JPG
- WD_KCRCO_B (BSc Hons in Creative Computing) - JPG
- WD_KCOMC_D (BSc in Software Systems Development) - PNG
- WD_KDEVP_B (BSc Hons in Software Systems Development) - PNG
- WD_KCOFO_B (BSc Hons in Computer Forensics Security) - PNG
- WD_KCMSC_B (BSc Hons in Computer Science) - PNG
- WD_KBUSY_G (HDip in Science in Business Systems Analysis) - PNG
- WD_KCOSC_G (HDip in Science in Computer Science) - PNG
- WD_KDAAN_G (HDip in Science in Data Analytics) - PNG
- WD_KCESS_R (MSc in Computer Science Enterprise Software Systems) - JPG
- WD_KISYP_R (MSc in Computing Information Systems Processes) - PNG

### Clusters
⚠️ 15 out of 16 clusters have images:
- ✅ Automotive, Automation and IoT - JPEG
- ❌ Business - **MISSING**
- ✅ Database and Analytics - JPEG
- ✅ Electronics - JPEG
- ✅ Engineering - JPEG
- ✅ Forensics and Security - PNG
- ✅ Game Development - JPEG
- ✅ Graphic Design and Animation - JPEG
- ✅ Humanities - JPEG
- ✅ Information Systems and Modelling - PNG
- ✅ Mathematics and Physics - JPEG
- ✅ Media Production - PNG
- ✅ Networks and Cloud - JPEG
- ✅ Professional Skills - JPEG
- ✅ Software and Web Development - PNG
- ✅ Sports Technology - PNG + JPEG (both available)

## Adding New Images

### For a New Programme

1. Create the image following the guidelines above
2. Save as: `module_catalogue/images/programmes/{PROGRAMME_CODE}.{ext}`
3. Example: `module_catalogue/images/programmes/WD_KNEWP_X.png`
4. Regenerate the catalogue:
   ```bash
   python3 generate-catalogue.py
   ```

### For a New Cluster

1. Create the image following the guidelines above
2. Save as: `module_catalogue/images/clusters/{Cluster_Name}.{ext}`
   - Use underscores for spaces
   - Match the sanitized name used in the cluster order
3. Example: `module_catalogue/images/clusters/Artificial_Intelligence.png`
4. Regenerate the catalogue:
   ```bash
   python3 generate-catalogue.py
   ```

## Image Sources

Images should be:
- **Owned by SETU** or properly licensed
- **Copyright compliant** (Creative Commons, purchased, or created)
- **Documented** with source information if required

Consider sources:
- SETU photography department
- Free stock photo sites (Unsplash, Pexels) with proper attribution
- Custom graphics created for SETU
- Licensed stock photography

## Maintenance

When updating images:
1. Replace the file in the appropriate directory
2. Keep the same filename
3. Regenerate the catalogue
4. Verify the new image appears correctly in the Tutors UI

When removing a programme/cluster:
1. Delete the corresponding image file
2. Update this README
3. Regenerate the catalogue

## Technical Details

The generator (`generate-catalogue.py`) uses the `copy_topic_image()` method to:
1. Check for images in the library directory
2. Try extensions in order: png, jpg, jpeg
3. Copy the first match to the output directory as `topic.{ext}`
4. Gracefully handle missing images (no error, just skip)

Images are copied during generation, not symlinked, ensuring the output directory is self-contained.
