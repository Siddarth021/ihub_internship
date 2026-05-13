from ultralytics import YOLO

# Load the latest YOLO26n model (nano version for speed)
model = YOLO("yolo26n.pt")

# Run inference on an image from a URL
# results = model("https://ultralytics.com/images/bus.jpg")
# results = model("D:\iiith-internship\image.png")
results = model("D:\iiith-internship\city-traffic.webp")

# Display the results with bounding boxes
results[0].show()
results[0].save()