# O-Net


This README file will guide you through the overall process of O-Net Segmentation and Classification.

## 1. Download pre-trained swin transformer model (Swin-T)
* [Get pre-trained model in this link] (https://drive.google.com/drive/folders/1UC3XOoezeum0uck4KBVGa8osahs6rKUY?usp=sharing): Put pretrained Swin-T into folder "pretrained_ckpt/" 


## 2. Prepare data

- The datasets that we used are the Synapse dataset, which is provided by TransUNet's authors, and the ISIC 2017 dataset. You can download the ISIC 2017 dataset here:
  - 2017: https://challenge.isic-archive.com/data/#2017
- Once downloaded, directories are provided for you. Please consult the README file located in the '[datasets](datasets)' folder for more details.

Once these files are set, please do the following steps:
- **In "train.sh":**
  - (LINE 6) The number of epochs we used was 75. Feel free to adjust this amount according to your preference. If you do adjust this amount, make sure to also effect the adjustment in the "train_class_after_segmentation.py" file (LINE 116)


- **In "train_class_after_segmentation.py":**
  - (LINE 89-90) Change the imgs_train_path, labels_train_path, imgs_val_path, labels_val_path, imgs_test_path, labels_test_path to their corresponding paths located in your 'datasets' folder.
  - (LINE 34) The number of epochs used for reproduction purposes is 25. Feel free to change this number depending on your needs.
  - (LINE 29) The batch size used for reproduction purposes is 8. If you do not have enough GPU memory, the batch size can be reduced to 4 to save memory.\
  - (LINE 191-192) Change the test_imgs_dir & test_csv file to their corresponding paths located in your 'datasets' folder.
  - (LINE 116) If you changed the number of epochs, make sure to change the number as well (e.g. if you used 75 epochs, the output is .../epoch74.pth). Make sure this number matches with your "swin_multi_scale_dir"

## 3. Prepare Environment

- Please prepare an environment with python=3.8, and then use the command "pip install -r requirements-full.txt" for the dependencies. It is important that the python version is 3.8, otherwise you will encounter errors. 

## 4. Run train.sh file

- Run the train script on synapse dataset. 
- The output will be saved as a ".pth" file in the directory "model_out". This will serve as the initial parameters to run the second segmentation network.

## 5. Run train_classification.sh file

- Run the script related to the ISIC dataset. The output will be metrics for both segmentation and classification.
- The result will be saved in a folder named 'classificationlr0.0001bs8' under the 'checkpoint' folder. This folder will be created once the 'train_classification.sh' file is run.

Scripts are provided below:

```bash
sh train.sh 
```
- Test 

```bash
sh train_classification.sh
```

## Paper
https://doi.org/10.3389/fnins.2022.876065

## References
* [TransUnet](https://github.com/Beckschen/TransUNet)
* [SwinTransformer](https://github.com/microsoft/Swin-Transformer)
* [Swin-Unet](https://github.com/HuCaoFighting/Swin-Unet.)

## Citation
@article{wangnet,
  title={O-Net: A novel framework with deep fusion of CNN and Transformer for Simultaneous Segmentation and Classification},
  author={Wang, Tao and Lan, Junlin and Han, Zixin and Hu, Ziwei and Huang, Yuxiu and Deng, Yanglin and Zhang, Hejun and Wang, Jianchao and Chen, Musheng and Jiang, Haiyan and others},
  journal={Frontiers in Neuroscience},
  pages={772},
  publisher={Frontiers}
}




