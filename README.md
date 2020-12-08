# cropper
Script for cropping remote clasess screenshots I wrote for my sister. It can use predefined sizes or detect borders of a slide. For this feature to work properly interesting part of image should:
- be positioned near the middle of screen height,
- have similar colour near the border (inside),
- have different color of sorrounding pixels,
- have rectangular shape.
After specifing directory and running script from command line it cropps all images from the dir, places them in subdir(CROPPED) while preserving raw versions in other subdir(RAW). 
