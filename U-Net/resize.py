import cv2
import os


### TRAIN ###
# Set the path for the input directory
input_dir_train = 'your_train_image_directory'

# Resize images in the input directory and overwrite them with the resized versions
image_files = os.listdir(input_dir_train)
for image_file in image_files:
    image_path = os.path.join(input_dir_train, image_file)

    # Read the image
    image = cv2.imread(image_path)

    # Resize the image to 128x128 pixels
    resized_image = cv2.resize(image, (128, 128), interpolation=cv2.INTER_AREA)

    # Overwrite the original image with the resized image
    cv2.imwrite(image_path, resized_image)

### TEST ###
import cv2
import os

# Set the path for the input directory
input_dir_test = 'your_test_image_directory'

# Resize images in the input directory and overwrite them with the resized versions
image_files = os.listdir(input_dir_test)
for image_file in image_files:
    image_path = os.path.join(input_dir_train, image_file)

    # Read the image
    image = cv2.imread(image_path)

    # Resize the image to 128x128 pixels
    resized_image = cv2.resize(image, (128, 128), interpolation=cv2.INTER_AREA)

    # Overwrite the original image with the resized image
    cv2.imwrite(image_path, resized_image)

### VALIDATION ###
import cv2
import os

# Set the path for the input directory
input_dir_val = 'your_val_image_directory'

# Resize images in the input directory and overwrite them with the resized versions
image_files = os.listdir(input_dir_train)
for image_file in image_files:
    image_path = os.path.join(input_dir_train, image_file)

    # Read the image
    image = cv2.imread(image_path)

    # Resize the image to 128x128 pixels
    resized_image = cv2.resize(image, (128, 128), interpolation=cv2.INTER_AREA)

    # Overwrite the original image with the resized image
    cv2.imwrite(image_path, resized_image)


#### MASKS ####

### TRAIN ###
# Set the path for the input directory
input_dir_train_m = 'your_train_mask_directory'

# Get the list of image files in the input directory
image_files = os.listdir(input_dir_train_m)

# Process each image in the input directory
for image_file in image_files:
    image_path = os.path.join(input_dir_train_m, image_file)

    # Load the image
    image = cv2.imread(image_path)

    # Resize the image to 128x128 pixels
    resized_image = cv2.resize(image, (128, 128))

    # Convert the resized image to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Convert the grayscale image to 8-bit depth
    bit_depth_image = cv2.convertScaleAbs(gray_image)

    # Overwrite the original image with the processed image
    cv2.imwrite(image_path, bit_depth_image)


### TEST ###
# Set the path for the input directory
input_dir_test_m = 'your_test_mask_directory'

# Get the list of image files in the input directory
image_files = os.listdir(input_dir_test_m)

# Process each image in the input directory
for image_file in image_files:
    image_path = os.path.join(input_dir_train_m, image_file)

    # Load the image
    image = cv2.imread(image_path)

    # Resize the image to 128x128 pixels
    resized_image = cv2.resize(image, (128, 128))

    # Convert the resized image to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Convert the grayscale image to 8-bit depth
    bit_depth_image = cv2.convertScaleAbs(gray_image)

    # Overwrite the original image with the processed image
    cv2.imwrite(image_path, bit_depth_image)


### VALIDATION ###
# Set the path for the input directory
input_val_test_m = 'your_val_mask_directory'

# Get the list of image files in the input directory
image_files = os.listdir(input_dir_test_m)

# Process each image in the input directory
for image_file in image_files:
    image_path = os.path.join(input_dir_train_m, image_file)

    # Load the image
    image = cv2.imread(image_path)

    # Resize the image to 128x128 pixels
    resized_image = cv2.resize(image, (128, 128))

    # Convert the resized image to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Convert the grayscale image to 8-bit depth
    bit_depth_image = cv2.convertScaleAbs(gray_image)

    # Overwrite the original image with the processed image
    cv2.imwrite(image_path, bit_depth_image)