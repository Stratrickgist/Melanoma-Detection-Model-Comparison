import pandas as pd

# SAVE TRAINING GROUND TRUTH TO SEGMENTED IMAGES
# Path to csv file
train_csv_file_path = "C:/Users/Patrick/Desktop/Capstone/O-Net/O-Net/datasets/ISIC 2017/Training/ISIC-2017_Training_Part3_GroundTruth.csv"

# Path to the new folder where the CSV file will be saved
train_output_folder = "C:/Users/Patrick/Desktop/Capstone/O-Net/O-Net/datasets/ISIC 2017/Training"

# Read CSV file
df = pd.read_csv(train_csv_file_path)

# Create the third column based on conditions
df['label'] = 2  # Initialize with class 2 (others)
df.loc[(df['melanoma'] == 1) & (df['seborrheic_keratosis'] == 0), 'label'] = 0  # Melanoma class
df.loc[(df['melanoma'] == 0) & (df['seborrheic_keratosis'] == 1), 'label'] = 1  # Keratosis class

# Save the updated DataFrame back to a new CSV file
new_csv_file_path = train_output_folder + "/ISIC-2017_Training_Part3_GroundTruth_preprocessed.csv"
df.to_csv(new_csv_file_path, index=False)

################################################################

# SAVE VALIDATION GROUND TRUTH TO SEGMENTED IMAGES
# Path to csv file
val_csv_file_path = "C:/Users/Patrick/Desktop/Capstone/O-Net/O-Net/datasets/ISIC 2017/Validation/ISIC-2017_Validation_Part3_GroundTruth.csv"

# Path to the new folder where the CSV file will be saved
val_output_folder = "C:/Users/Patrick/Desktop/Capstone/O-Net/O-Net/datasets/ISIC 2017/Validation"

# Read CSV file
df1 = pd.read_csv(val_csv_file_path)

# Create the third column based on conditions
df1['label'] = 2  # Initialize with class 2 (others)
df1.loc[(df1['melanoma'] == 1) & (df1['seborrheic_keratosis'] == 0), 'label'] = 0  # Melanoma class
df1.loc[(df1['melanoma'] == 0) & (df1['seborrheic_keratosis'] == 1), 'label'] = 1  # Keratosis class

# Save the updated DataFrame back to a new CSV file
new_csv_file_path_val = val_output_folder + "/ISIC-2017_Validation_Part3_GroundTruth_preprocessed.csv"
df1.to_csv(new_csv_file_path_val, index=False)


################################################################



# SAVE TESTING GROUND TRUTH TO SEGMENTED IMAGES
# Path to csv file
test_csv_file_path = "C:/Users/Patrick/Desktop/Capstone/O-Net/O-Net/datasets/ISIC 2017/Test/ISIC-2017_Test_v2_Part3_GroundTruth.csv"

# Path to the new folder where the CSV file will be saved
test_output_folder = "C:/Users/Patrick/Desktop/Capstone/O-Net/O-Net/datasets/ISIC 2017/Test"

# Read CSV file
df2 = pd.read_csv(test_csv_file_path)

# Create the third column based on conditions
df2['label'] = 2  # Initialize with class 2 (others)
df2.loc[(df2['melanoma'] == 1) & (df2['seborrheic_keratosis'] == 0), 'label'] = 0  # Melanoma class
df2.loc[(df2['melanoma'] == 0) & (df2['seborrheic_keratosis'] == 1), 'label'] = 1  # Keratosis class

# Save the updated DataFrame back to a new CSV file
new_csv_file_path_test = test_output_folder + "/ISIC-2017_Test_v2_Part3_GroundTruth_preprocessed.csv"
df2.to_csv(new_csv_file_path_test, index=False)