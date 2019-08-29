# Face Recognition Congress

This project seeks to replicate the [ACLU analysis](https://www.aclu.org/blog/privacy-technology/surveillance-technologies/amazons-face-recognition-falsely-matched-28) that used AWS Rekognition service to compare headshots of congressmen to public arrest photos.

The original analysis used a public dataset of 25k public arrest photos and found 28 mismatches based on default settings (70% confidence).

This analysis uses a public [NIST Special Database 18](https://www.nist.gov/srd/nist-special-database-18) consisting of 1,573 individuals (1495 male and 78 female) and found 10 mismatches based on 70% confidence.
