IMAGE SEGMENTATION AND IMAGE CLASSIFICATION
=
This ReadMe file provides an overview on what data files are needed. This is based off the ISIC 2017 dataset.

* The ISIC 2017 dataset ()
  * Download the images from the ISIC repository, and drag them to their respective folders:
    * train files - "/data/ISIC Data/train"
    * test files -  "/data/ISIC Data/test"
    * validation files - "/data/ISIC Data/val"

Your directory should look similar to this: 
```
.
├──ISIC Data
│   ├──test
│   │   └── ISIC-2017_Test_v2_Data
│   │   └── ISIC-2017_Test_v2_Part1_GroundTruth
│   │   └── ISIC-2017_Test_v2_Part2_GroundTruth
│   │   └── ISIC-2017_Test_v2_Part3_GroundTruth.csv
│   ├──train
│   │   └── ISIC-2017_Training_Data
│   │   └── ISIC-2017_Training_Part1_GroundTruth
│   │   └── ISIC-2017_Training_Part2_GroundTruth
│   │   └── ISIC-2017_Training_Part3_GroundTruth.csv
│   ├──val
│   │   └── ISIC-2017_Validation_Data
│   │   └── ISIC-2017_Validation_Part1_GroundTruth
│   │   └── ISIC-2017_Validation_Part2_GroundTruth
│   │   └── ISIC-2017_Validation_Part3_GroundTruth.csv

```
Once you have the structure set up, kindly run __"resize.py"__. This code will resize your images and masks to the standard size (128x128x3 for images ; 128x128x1 for masks). This is needed to run the U-Net structure.

__CODE__
Run the following in order:

* resize.py - resizing of images

* "1. UNet.ipynb" - runs your U-Net algorithm

* my_functions.py (this will serve as a baseline to run feature extraction)

* "2. Feature Extraction.ipynb" - runs feature extraction

* "3. SVM.ipynb" - runs SVM algorithm


