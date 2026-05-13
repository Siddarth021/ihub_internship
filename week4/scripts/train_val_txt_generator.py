import os

# Train file
train_dir = "dataset/images/train"

with open("dataset/train.txt", "w") as f:
    for img in os.listdir(train_dir):
        f.write(f"{train_dir}/{img}\n")

# Val file
val_dir = "dataset/images/val"

with open("dataset/val.txt", "w") as f:
    for img in os.listdir(val_dir):
        f.write(f"{val_dir}/{img}\n")

print("train.txt and val.txt created")