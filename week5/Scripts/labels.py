import os
import shutil

# =========================
# FOLDERS
# =========================

# Exported YOLO labels folder
SOURCE_LABELS = "New folder (2)"

# Image folders
TRAIN_IMAGES = "dataset/images/train"
VAL_IMAGES = "dataset/images/val"

# Label destination folders
TRAIN_LABELS = "dataset/labels/train"
VAL_LABELS = "dataset/labels/val"

# Create folders if not exist
os.makedirs(TRAIN_LABELS, exist_ok=True)
os.makedirs(VAL_LABELS, exist_ok=True)

# =========================
# GET TRAIN IMAGE FILENAMES
# =========================

train_files = set()

for img in os.listdir(TRAIN_IMAGES):

    name = os.path.splitext(img)[0]
    train_files.add(name)

# =========================
# GET VAL IMAGE FILENAMES
# =========================

val_files = set()

for img in os.listdir(VAL_IMAGES):

    name = os.path.splitext(img)[0]
    val_files.add(name)

# =========================
# SPLIT LABELS
# =========================

train_count = 0
val_count = 0

for label_file in os.listdir(SOURCE_LABELS):

    if label_file.endswith(".txt"):

        label_name = os.path.splitext(label_file)[0]

        src = os.path.join(SOURCE_LABELS, label_file)

        # TRAIN
        if label_name in train_files:

            shutil.copy(src,
                        os.path.join(TRAIN_LABELS, label_file))

            train_count += 1

        # VAL
        elif label_name in val_files:

            shutil.copy(src,
                        os.path.join(VAL_LABELS, label_file))

            val_count += 1

# =========================
# SUMMARY
# =========================

print(f"Train labels copied: {train_count}")
print(f"Validation labels copied: {val_count}")
print("Done.")