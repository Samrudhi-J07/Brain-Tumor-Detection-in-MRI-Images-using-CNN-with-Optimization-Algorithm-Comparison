from ultralytics import YOLO

model = YOLO("runs/detect/sgd_run/weights/best.pt")

results = model.predict(
    source="test_images",
    save=True,
    conf=0.2,
)

for r in results:
    print(r.boxes.cls)   # class ids
    print(r.boxes.conf)  # confidence scores