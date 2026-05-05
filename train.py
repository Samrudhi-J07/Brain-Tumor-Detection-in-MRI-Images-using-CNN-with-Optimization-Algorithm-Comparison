from ultralytics import YOLO

# -------- TRAIN WITH ADAM --------
print("🚀 Starting training with Adam...")

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=10,          # keep low for your laptop
    imgsz=256,         # smaller image size
    batch=2,           # small batch
    workers=0,         # avoid CPU overload
    device="cpu",
    optimizer="Adam",
    verbose=True,
    name="adam_run"
)

print(" Adam training completed!")


# -------- TRAIN WITH SGD --------
print(" Starting training with SGD...")

model = YOLO("yolov8n.pt")   # reload fresh model

model.train(
    data="data.yaml",
    epochs=10,
    imgsz=256,
    batch=2,
    workers=0,
    device="cpu",
    optimizer="SGD",
    verbose=True,
    name="sgd_run"
)

print("✅ SGD training completed!")