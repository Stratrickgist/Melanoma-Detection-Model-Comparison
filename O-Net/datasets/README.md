# Data Preparation

1. Access to the synapse multi-organ dataset:
   - Please download the pre-processed Synapse Dataset here: https://github.com/SLDGroup/MERIT (it is a Google Drive link)

2. Download the ISIC 2017 dataset (https://challenge.isic-archive.com/data/#2017) and save them in their respective directories

3. Convert the labels from binary to multi-class. Do it using the following steps:
   - Create a new column named "label" - this will contain the following values
     - 0 = Melanoma
     - 1 = Seborrheic Keratosis
     - 2 = Nevus
   - Once created, check the following:
     - If "melanoma" = 1 & "keratosis" = 0 - label as 0 in the "label" column
     - If "melanoma" = 0 & "keratosis" = 1 - label as 1 in the "label" column
     - If "melanoma" = 0 & "keratosis" = 0 - label as 2 in the "label" column

   - NOTE: Alternatively, please run this script located in the "datasets" folder that creates the above process: __"ISIC_preprocessing.py"__

4. If you run the "ISIC_preprocessing.py" script, the directory structure of the dataset folder should be as follows:

```bash
.
├── ISIC 2017
│   ├──Test
│   │       └── ISIC-2017_Test_v2_Data
│   │       └── ISIC-2017_Test_v2_Part1_GroundTruth
│   │       └── ISIC-2017_Test_v2_Part2_GroundTruth
│   │       └── ISIC-2017_Test_v2_Part3_GroundTruth.csv
│   │       └── ISIC-2017_Test_v2_Part3_GroundTruth_preprocessed.csv
│   ├──Training
│   │       └── ISIC-2017_Training_Data
│   │       └── ISIC-2017_Training_Part1_GroundTruth
│   │       └── ISIC-2017_Training_Part2_GroundTruth
│   │       └── ISIC-2017_Training_Part3_GroundTruth.xlsx
│   │       └── ISIC-2017_Training_Part3_GroundTruth_preprocessed.csv
│   ├──Validation
│   │       └── ISIC-2017_Validation_Data
│   │       └── ISIC-2017_Validation_Part1_GroundTruth
│   │       └── ISIC-2017_Validation_Part2_GroundTruth
│   │       └── ISIC-2017_Validation_Part3_GroundTruth.xlsx
│   │       └── ISIC-2017_Validation_Part3_GroundTruth_preprocessed.csv
└──Synapse
      ├── test_vol_h5
        │   ├── case0001.npy.h5
        │   └── *.npy.h5
      └── train_npz
        ├── case0005_slice000.npz
        └── *.npz
```
