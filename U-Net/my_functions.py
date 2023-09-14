# Source: https://github.com/jiyangzhao/pyehd
import numpy as np
import scipy.ndimage as ndi
import cv2
from skimage.color import rgb2gray
from skimage.feature import hog
from skimage.feature import local_binary_pattern
from scipy import stats

# Local Binary Patterns (LBP)
# Source : https://apmonitor.com/pds/index.php/Main/TextureClassification#:~:text=Local%20Binary%20Pattern,-A%20Local%20Binary&text=LBP%20is%20an%20effective%20feature,to%20create%2036%20unique%20patterns
def extract_lbp_features(image):
    gray_image = rgb2gray(image)
    # Convert image to integer dtype
    image_int = (gray_image * 255).astype(np.uint8)

    # LBP function params
    radius = 3
    n_points = 8 * radius
    n_bins = n_points + 2
    lbp = local_binary_pattern(image_int, n_points, radius, 'uniform')
    lbp = lbp.ravel()
    # feature_len = int(lbp.max() + 1)
    feature = np.zeros(n_bins)
    for i in lbp:
        feature[int(i)] += 1
    feature /= np.linalg.norm(feature, ord=1)
    return feature


# Edge Histogram Descriptor
# function to convert RBG image to grayscale image
def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


# function to get EHD vector
def findehd(img):
    r, c, m = np.shape(img)  # get the shape of image
    if m == 3:
        img = rgb2gray(img)  # convert RGB img to grayscale img
    M = 4 * np.ceil(r / 4)
    N = 4 * np.ceil(c / 4)
    img = np.reshape(img, (int(M), int(N)))  # Making image dim. divisible completely by 4
    AllBins = np.zeros((17, 5))  # initializing Bins
    p = 1
    L = 0
    for _ in range(4):
        K = 0
        for _ in range(4):
            block = img[K:K + int(M / 4), L:L + int(N / 4)]  # Extracting (M/4,N/4) block
            AllBins[p, :] = getbins(np.double(block))
            K = K + int(M / 4)
            p = p + 1
        L = L + int(N / 4)
    GlobalBin = np.mean(AllBins)  # getting global Bin
    AllBins[16, :] = np.round(GlobalBin)
    ehd = np.reshape(np.transpose(AllBins), [1, 85])
    ehd = ehd[0, -5:]
    return ehd


# function for getting Bin values for each block
def getbins(imgb):
    M, N = imgb.shape
    M = 2 * np.ceil(M / 2)
    N = 2 * np.ceil(N / 2)
    # print(M)
    # print(N)
    imgb = np.reshape(imgb, (int(M), int(N)))  # Making block dimension divisible by 2
    bins = np.zeros((1, 5))  # initialize Bin
    """Operations, define constant"""
    V = np.array([[1, -1], [1, -1]])  # vertical edge operator
    H = np.array([[1, 1], [-1, -1]])  # horizontal edge operator
    D45 = np.array([[1.414, 0], [0, -1.414]])  # diagonal 45 edge operator
    D135 = np.array([[0, 1.414], [-1.414, 0]])  # diagonal 135 edge operator
    Isot = np.array([[2, -2], [-2, 2]])  # isotropic edge operator
    T = 50  # threshold

    nobr = int(M / 2)  # loop limits
    nobc = int(N / 2)  # loop limits
    L = 0

    """loops of operating"""
    for _ in range(nobc):
        K = 0
        for _ in range(nobr):
            block = imgb[K:K + 2, L:L + 2]  # Extracting 2x2 block
            pv = np.abs(np.sum(np.sum(block * V)))  # apply operators
            ph = np.abs(np.sum(np.sum(block * H)))
            pd45 = np.abs(np.sum(np.sum(block * D45)))
            pd135 = np.abs(np.sum(np.sum(block * D135)))
            pisot = np.abs(np.sum(np.sum(block * Isot)))
            parray = [pv, ph, pd45, pd135, pisot]
            index = np.argmax(parray)  # get the index of max value
            value = parray[index]  # get the max value
            # print('value: '+str(value))
            if value >= T:
                bins[0, index] = bins[0, index] + 1  # update bins values
            K = K + 2
        L = L + 2

    # print('bins is:')
    # print(bins)
    return bins


# Histogram of Oriented Gradients (HOG)
# Source : https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_hog.html
# Source : https://www.kaggle.com/code/samanemami/caltech101-feature-extraction-hog
def extract_hog_features(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    fd, hog_features = hog(gray_image, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True)
    return fd


# Gabor filters
# source : https://subscription.packtpub.com/book/data/9781789537147/7/ch07lvl1sec52/classifying-textures-with-gabor-filter-banks
# source : https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial75-Extracting_features_using_Gabor_Filter.py
def extract_gabor_features(image, kernels):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    feats = np.zeros((len(kernels), 2), dtype=np.double)
    for k, kernel in enumerate(kernels):
        filtered = ndi.convolve(image, kernel, mode='wrap')
        feats[k, 0] = filtered.mean()
        feats[k, 1] = filtered.var()
    return feats


# Color features
def extract_color_features(image):
    # Separate R, G, B components of the ROI
    r, g, b = cv2.split(image)

    def remove_zeros_and_normalize(matrix):
        nonzero_matrix = matrix[matrix != 0]
        if len(nonzero_matrix) == 0:
            # Handle blacked out images by returning NaN values
            return np.array([0, 0], dtype=np.uint8)
        std = np.std(nonzero_matrix)
        if std == 0:
            # Handle the case of zero standard deviation (when all values are the same)
            return np.array([0, 0], dtype=np.uint8)
        else:
            normalized_matrix = (nonzero_matrix - np.mean(nonzero_matrix)) / np.std(nonzero_matrix)
            return normalized_matrix


    def calculate_stats(matrix):
        mean = np.mean(matrix)
        minimum = np.min(matrix)
        std_dev = np.std(matrix)
        skewness = stats.skew(matrix)
        kurtosis = stats.kurtosis(matrix)
        return mean, minimum, std_dev, skewness, kurtosis

    # Normalize and calculate statistics for R, G, B components
    r_normalized = remove_zeros_and_normalize(r)
    g_normalized = remove_zeros_and_normalize(g)
    b_normalized = remove_zeros_and_normalize(b)

    r_mean, r_min, r_std, r_skew, r_kurt = calculate_stats(r_normalized)
    g_mean, g_min, g_std, g_skew, g_kurt = calculate_stats(g_normalized)
    b_mean, b_min, b_std, b_skew, b_kurt = calculate_stats(b_normalized)

    # Convert ROI to LUV color space
    luv_image = cv2.cvtColor(image, cv2.COLOR_RGB2LUV)
    l, u, v = cv2.split(luv_image)

    # Normalize and calculate statistics for L, U, V components
    l_normalized = remove_zeros_and_normalize(l)
    u_normalized = remove_zeros_and_normalize(u)
    v_normalized = remove_zeros_and_normalize(v)

    l_mean, l_min, l_std, l_skew, l_kurt = calculate_stats(l_normalized)
    u_mean, u_min, u_std, u_skew, u_kurt = calculate_stats(u_normalized)
    v_mean, v_min, v_std, v_skew, v_kurt = calculate_stats(v_normalized)

    # Check if any statistics are NaN and assign default value of 0
    statistics = [r_mean, r_min, r_std, r_skew, r_kurt,
                  g_mean, g_min, g_std, g_skew, g_kurt,
                  b_mean, b_min, b_std, b_skew, b_kurt,
                  l_mean, l_min, l_std, l_skew, l_kurt,
                  u_mean, u_min, u_std, u_skew, u_kurt,
                  v_mean, v_min, v_std, v_skew, v_kurt]

    default_value = 0

    for i in range(len(statistics)):
        if np.isnan(statistics[i]):
            statistics[i] = default_value

    # Assign the updated values back to the original variables
    r_mean, r_min, r_std, r_skew, r_kurt, \
        g_mean, g_min, g_std, g_skew, g_kurt, \
        b_mean, b_min, b_std, b_skew, b_kurt, \
        l_mean, l_min, l_std, l_skew, l_kurt, \
        u_mean, u_min, u_std, u_skew, u_kurt, \
        v_mean, v_min, v_std, v_skew, v_kurt = statistics

    # Create separate NumPy arrays for each statistic
    mean_features = np.array([r_mean, g_mean, b_mean, l_mean, u_mean, v_mean])
    min_features = np.array([r_min, g_min, b_min, l_min, u_min, v_min])
    std_features = np.array([r_std, g_std, b_std, l_std, u_std, v_std])
    skewness_features = np.array([r_skew, g_skew, b_skew, l_skew, u_skew, v_skew])
    kurtosis_features = np.array([r_kurt, g_kurt, b_kurt, l_kurt, u_kurt, v_kurt])

    return mean_features, min_features, std_features, skewness_features, kurtosis_features
