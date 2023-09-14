IMAGE SEGMENTATION AND IMAGE CLASSIFICATION
=
This ReadMe file is a guide on how to run image segmentation, feature extraction, and image classification on the ISIC 2017 dataset using U-Net. 

__PRE-REQUISITES__

In order to ensure a successful run, the following are needed:
* Python >=3.8
* All necessary dependencies, which can be found in the "requirements.txt" file. To install, run on your terminal the following code: "pip install -r requirements.txt"


Your directory should look similar to this: 
```
.
├──extracted_features
├──ISIC Data
│   ├──test
│   ├──train
│   ├──val
├──predicted_masks
│   ├──test
│   ├──train
│   ├──val
├──segmented_images
│   ├──test
│   ├──train
│   ├──val
├──SVM



```
Once you have the structure set up, please run __"resize.py"__. This code will resize your images and masks to the standard size (128x128x3 for images ; 128x128x1 for masks). This is needed to run the U-Net structure. Also, modify all directories to reflect the correct file paths for train, test, and validation.

__CODE__
Run the following in order:

* resize.py - resizing of images

* "1. UNet.ipynb" - runs your U-Net algorithm

* my_functions.py (this will serve as a baseline to run feature extraction)

* "2. Feature Extraction.ipynb" - runs feature extraction

* "3. SVM.ipynb" - runs SVM algorithm


Citations

Seeja R D and A Suresh. "Deep Learning Based Skin Lesion Segmentation and Classification of Melanoma Using Support Vector Machine (SVM)." Asian Pacific Journal of Cancer Prevention (2019). doi: 10.31557/APJCP.2019.20.5.1555.

Cassidy, Bill, Connah Kendrick, Andrzej Brodzicki, Joanna Jaworek-Korjakowska, and Moi Hoon Yap. “Analysis of the ISIC Image Datasets: Usage, Benchmarks and Recommendations.” Medical Image Analysis 75 (2022): 102305. https://doi.org/10.1016/j.media.2021.102305.

