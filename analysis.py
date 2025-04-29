import cv2
import numpy as np

def analyze_brightness(image):
    """Calculate the average brightness of the image."""
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Calculate the average brightness
    average_brightness = np.mean(gray_image)
    return average_brightness

def analyze_sharpness(image):
    """Calculate the sharpness of the image using the Laplacian variance."""
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Calculate the Laplacian
    laplacian_var = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    return laplacian_var

def analyze_contrast(image):
    """Calculate the contrast of the image using the standard deviation of pixel values."""
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Calculate the standard deviation
    contrast = np.std(gray_image)
    return contrast

def analyze_saturation(image):
    """Calculate the average saturation of the image."""
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Extract the saturation channel
    saturation_channel = hsv_image[:, :, 1]
    # Calculate the average saturation
    average_saturation = np.mean(saturation_channel)
    return average_saturation 
