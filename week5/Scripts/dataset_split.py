import os
import random
import shutil

# Source folder containing all frames
SOURCE_DIR = "frames"

# Destination folders
TRAIN_DIR = "dataset/images/train"
VAL_DIR = "dataset/images/val"
TEST_DIR = "dataset/images/test"

# Create folders
os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(VAL_DIR, exist_ok=True)
os.makedirs(TEST_DIR, exist_ok=True)

# Get all image files
images = [img for img in os.listdir(SOURCE_DIR)
          if img.endswith((".jpg", ".png", ".jpeg"))]

# Sort and shuffle
images.sort()
random.shuffle(images)

# Fixed split sizes
train_count = 80
val_count = 20

# Split images
train_images = images[:train_count]
val_images = images[train_count:train_count + val_count]
test_images = images[train_count + val_count:]

# Copy train images
for img in train_images:
    shutil.copy(
        os.path.join(SOURCE_DIR, img),
        os.path.join(TRAIN_DIR, img)
    )

# Copy validation images
for img in val_images:
    shutil.copy(
        os.path.join(SOURCE_DIR, img),
        os.path.join(VAL_DIR, img)
    )

# Copy test images
for img in test_images:
    shutil.copy(
        os.path.join(SOURCE_DIR, img),
        os.path.join(TEST_DIR, img)
    )

# Summary
print(f"Total images: {len(images)}")
print(f"Train images: {len(train_images)}")
print(f"Validation images: {len(val_images)}")
print(f"Test images: {len(test_images)}")