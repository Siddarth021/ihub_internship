from ultralytics import YOLO
import os
import cv2

model = YOLO("yolo11n-seg.pt")

input_folder = "../week1/frames_30fps2"
output_folder = "segmented_frames"

os.makedirs(output_folder, exist_ok=True)

for filename in sorted(os.listdir(input_folder)):

    if filename.endswith(".jpg"):

        image_path = os.path.join(input_folder, filename)

        results = model(image_path)

        segmented_image = results[0].plot()

        output_path = os.path.join(output_folder, filename)

        cv2.imwrite(output_path, segmented_image)

        print(f"Processed: {filename}")

print("Segmentation completed!")