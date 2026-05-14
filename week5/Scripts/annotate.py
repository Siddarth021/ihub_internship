import os
import shutil
import re

# =========================
# FOLDERS
# =========================

# Folder containing annotated exported images
ANNOTATED_FOLDER = "New folder"

# Existing dataset folders
TRAIN_FOLDER = "dataset/images/train"
VAL_FOLDER = "dataset/images/val"

# =========================
# FUNCTION TO EXTRACT FRAME NUMBER
# Example:
# abc-frame_0123.jpg -> 0123
# =========================

def get_frame_number(filename):
    match = re.search(r'frame_(\d+)', filename)
    if match:
        return match.group(1)
    return None

# =========================
# BUILD LOOKUP FOR ANNOTATED IMAGES
# =========================

annotated_lookup = {}

for file in os.listdir(ANNOTATED_FOLDER):

    if file.lower().endswith((".jpg", ".jpeg", ".png")):

        frame_num = get_frame_number(file)

        if frame_num:
            annotated_lookup[frame_num] = file

# =========================
# REPLACE TRAIN IMAGES
# =========================

train_replaced = 0

for file in os.listdir(TRAIN_FOLDER):

    frame_num = get_frame_number(file)

    if frame_num in annotated_lookup:

        annotated_file = annotated_lookup[frame_num]

        src = os.path.join(ANNOTATED_FOLDER, annotated_file)
        dst = os.path.join(TRAIN_FOLDER, annotated_file)

        # remove old image
        os.remove(os.path.join(TRAIN_FOLDER, file))

        # copy annotated image
        shutil.copy(src, dst)

        train_replaced += 1

# =========================
# REPLACE VAL IMAGES
# =========================

val_replaced = 0

for file in os.listdir(VAL_FOLDER):

    frame_num = get_frame_number(file)

    if frame_num in annotated_lookup:

        annotated_file = annotated_lookup[frame_num]

        src = os.path.join(ANNOTATED_FOLDER, annotated_file)
        dst = os.path.join(VAL_FOLDER, annotated_file)

        # remove old image
        os.remove(os.path.join(VAL_FOLDER, file))

        # copy annotated image
        shutil.copy(src, dst)

        val_replaced += 1

# =========================
# SUMMARY
# =========================

print(f"Train images replaced: {train_replaced}")
print(f"Validation images replaced: {val_replaced}")
print("Done.")