# Brain-Tumor-Detection-in-MRI-Images-using-CNN-with-Optimization-Algorithm-Comparison
Brain Tumor Detection using YOLOv8 with optimizer comparison

# 🧠 Brain Tumor Detection using YOLOv8 with Optimizer Comparison (Adam vs SGD)

## 📌 Overview

This project focuses on detecting brain tumors from MRI images using the YOLOv8 object detection model. It also includes a comparative analysis of two optimization algorithms — Adam and SGD — to evaluate their impact on model performance.

The system identifies different types of brain tumors and highlights them with bounding boxes along with confidence scores.

---

## 🚀 Features

* Detection of multiple tumor types:

  * NO_tumor
  * glioma
  * meningioma
  * pituitary
* Real-time object detection using YOLOv8
* Bounding box visualization with confidence scores
* Comparison of Adam and SGD optimizers
* Custom dataset training and evaluation

---

## 🛠️ Tech Stack

* Python
* YOLOv8 (Ultralytics)
* PyTorch
* OpenCV
* NumPy
* Matplotlib

---

## 📂 Project Structure

```
Brain-Tumor-Detection-YOLOv8/
│
├── train.py              # Model training script
├── predict.py            # Prediction script
├── data.yaml             # Dataset configuration
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── results/              # Output images
```

---

## ⚙️ Installation

1. Clone or download the repository
2. Install dependencies:

```
pip install -r requirements.txt
```

---

## 🧠 Model Training

```
python train.py
```

* Trains YOLOv8 model on custom MRI dataset
* Supports both Adam and SGD optimizers

---

## 🔍 Prediction

```
python predict.py
```

* Runs detection on test images
* Saves output images with bounding boxes

---

## 📊 Results

* The model successfully detects brain tumors with bounding boxes
* Performance varies based on optimizer used
* SGD showed more stable learning in this setup

---

## 📸 Sample Results

### 🧠 Tumor Detection Outputs

![Result 1](results/img1.png)
![Result 2](results/img2.png)
![Result 3](results/img3.png)

![Result 4](results/img4.png)
![Result 5](results/img5.png)
![Result 6](results/img6.png)

![Result 7](results/img7.png)


## ⚠️ Challenges Faced

* Incorrect dataset labeling (NO_tumor mixed with tumor classes)
* Model bias toward NO_tumor class
* Limited hardware (CPU training) leading to slow training

---

## 💡 Key Learnings

* Object detection using YOLOv8
* Importance of correct data labeling
* Model training and evaluation techniques
* Impact of optimizers on deep learning models
* Debugging model prediction issues

---

## 🔮 Future Improvements

* Increase dataset size for better accuracy
* Use GPU for faster training
* Improve class balance
* Deploy as a web application using Streamlit

---

## 👩‍💻 Author

**Samrudhi Jadhav**

---

## ⭐ Acknowledgement

This project is developed as part of learning and exploring deep learning techniques for medical image analysis.
