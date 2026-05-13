import os
import re
import shutil

# Source folder containing all frames
SOURCE_DIR = "week1/frames2"

# Destination test folder
TEST_DIR = "dataset/images/test"

os.makedirs(TEST_DIR, exist_ok=True)

# Frame numbers already used in train/val
used_frames = {
    1,2,3,4,5,6,7,8,
    13,21,
    80,81,
    129,130,
    345,346,
    737,738,
    851,852,
    905,913,
    963,
    1131,1132,
    1215,1223,
    1337,1338,
    1643,1651,
    1882,1883,
    1997,2005,
    2087,2095,
    2291,2299,
    2358,2359,
    2375,2383,
    2923,2931,
    3078,3080,
    3523,3531,
    3583,3584
}

# Regex pattern to extract frame number
pattern = re.compile(r"frame_(\d+)\.jpg")

# Iterate through all images
for filename in os.listdir(SOURCE_DIR):

    match = pattern.match(filename)

    if match:
        frame_number = int(match.group(1))

        # If frame not in used train/val images
        if frame_number not in used_frames:

            src_path = os.path.join(SOURCE_DIR, filename)
            dst_path = os.path.join(TEST_DIR, filename)

            shutil.copy(src_path, dst_path)

print("Remaining images copied to test folder successfully.")