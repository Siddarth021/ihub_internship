from ultralytics import YOLO
import os
import cv2

# Load pretrained YOLO model
model = YOLO("yolo11n.pt")

input_folder = "../week1/frames_30fps2"
output_folder = "detected_frames"

os.makedirs(output_folder, exist_ok=True)

# Process all images
for filename in sorted(os.listdir(input_folder)):
    if filename.endswith(".jpg"):

        image_path = os.path.join(input_folder, filename)

        # Run detection
        results = model(image_path)

        # Annotated image
        annotated_frame = results[0].plot()

        # Save output
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, annotated_frame)

        print(f"Processed: {filename}")

print("All frames processed!")