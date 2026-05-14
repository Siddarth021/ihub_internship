import os

folder = "../runs/detect/predict-2"

images = [f for f in os.listdir(folder) if f.endswith(".jpg")]

images.sort()

for i, image in enumerate(images, start=1):

    new_name = f"frame_{i:04d}.jpg"

    os.rename(
        os.path.join(folder, image),
        os.path.join(folder, new_name)
    )

print("Renaming complete.")