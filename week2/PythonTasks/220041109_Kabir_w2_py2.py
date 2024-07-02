import os
import cv2
import numpy as np

def apply_filters(image_path):
    image_name, ext = os.path.splitext(image_path)
    base_name = os.path.basename(image_name)
    
    image = cv2.imread(image_path)

    # 1. Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"{base_name}-grayscale{ext}", gray_image)

    # 2. Blur
    blurred_image = cv2.GaussianBlur(image, (51, 51), 0)
    cv2.imwrite(f"{base_name}-blur{ext}", blurred_image)

    # 3. Hue Rotation 
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue_shift = 60
    hsv_image[..., 0] = (hsv_image[..., 0] + hue_shift) % 180
    hue_rotated_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    cv2.imwrite(f"{base_name}-hue_rot{ext}", hue_rotated_image)

    # 4. Brightness
    bright_factor = 50
    bright_image = cv2.convertScaleAbs(image, alpha=1, beta=bright_factor)
    cv2.imwrite(f"{base_name}-bright{ext}", bright_image)

    # 5. Inversion
    inverted_image = cv2.bitwise_not(image)
    cv2.imwrite(f"{base_name}-invert{ext}", inverted_image)

    # 6_Bonus. Noise
    noise = np.random.normal(0, 32, image.shape)
    noisy_image = np.clip(np.array(image) + noise, 0, 255).astype(np.uint8)
    cv2.imwrite(f"{base_name}-noise{ext}", noisy_image)

    
if __name__ == "__main__":
    image_path = "./sample1.jpg" 
    apply_filters(image_path)

