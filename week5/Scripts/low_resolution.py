import cv2
import os

input_dir = "../week4/dataset/images/train"
output_dir ="../week4/dataset/resized_images/train_resized"

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):

    if file.endswith(".jpg"):

        img_path = os.path.join(input_dir, file)

        img = cv2.imread(img_path)

        h, w = img.shape[:2]

        new_width = 384
        new_height = int((new_width / w) * h)

        resized = cv2.resize(img, (new_width, new_height))

        cv2.imwrite(os.path.join(output_dir, file), resized)

print("train images resized.")