# 🧠 Vitalix — AI-Powered Anti-Spoofing Face Detection System

> **Vitalix** brings *intelligence, speed, and reliability* together to stop spoofing attacks before they happen.
> It’s a next-gen **liveness detection** and **anti-spoofing** system built using **Python, YOLOv8, and Deep Learning** — crafted to secure face-based authentication systems in real-time.

---

## 🌍 Overview

In today’s digital-first world, **face authentication** has become mainstream — but so have **spoofing attacks** using printed photos, deepfakes, or 3D masks.
**Vitalix** tackles this head-on with a **real-time liveness detection system** that can tell the difference between a *real human face* and a *spoofed attempt*.

This project is designed for:

* AI-based identity verification systems
* Government or banking KYC workflows
* Access control and surveillance systems
* Any platform that relies on face-based authentication

---

## ⚙️ Key Features

✅ **YOLOv8 Integration** – Lightning-fast face detection and localization
✅ **Liveness Detection** – Distinguishes between live and fake faces using micro-expressions & texture analysis
✅ **Anti-Spoofing Model** – Trained to resist print, replay, and mask-based attacks
✅ **Real-Time Performance** – Optimized for low-latency detection using GPU acceleration
✅ **Customizable Architecture** – Easy to extend or retrain on your own dataset

---



## 🗂️ Project Structure

```
Vitalix/
│
├── datacollection.py       # Collect and preprocess face datasets  
├── splitData.py            # Split data into train/test sets  
├── train.py                # Model training pipeline using YOLOv8  
├── yolo Test.py            # Testing script for inference  
├── main.py                 # Project entry point  
├── yolov8n.pt              # Pretrained YOLO model weights  
└── README.md               # Project documentation
```

---

## 💻 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Kavyazz10/Vitalix.git
cd Vitalix
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt` file yet, create one including:
> `torch`, `ultralytics`, `opencv-python`, `numpy`, `matplotlib`, `pandas`

### 3️⃣ Run the Application

```bash
python "yolo Test.py" --weights yolov8n.pt --source 0
```

This will activate your webcam and start real-time liveness detection.

---

## 📊 Model Training

You can train your own dataset using:

```bash
python train.py --data path/to/your_dataset.yaml --epochs 100 --img 640
```

* Adjust epochs, batch size, and learning rate for better accuracy.
* Dataset should contain both *real* and *spoofed* face samples.

---

## 🧠 Research Highlights

* Based on the latest **YOLOv8** detection backbone
* Integrates **texture and temporal analysis** for detecting spoofing attempts
* Can be improved with:

  * Depth map analysis
  * Blink/motion detection
  * Transformer-based attention modules

---

## 💬 Author

👩‍💻 **Kavya** — B.Tech Artificial Intelligence & Data Science
📍 Focus: Deep Learning | Face Recognition | AI Systems
🌐 GitHub: [Kavyazz10](https://github.com/Kavyazz10)

> “AI isn’t about replacing humans — it’s about amplifying how secure, fast, and smart our systems can become.”

---

## ⭐ Support the Project

If you found this project helpful, please ⭐ star this repository — it helps others discover **Vitalix** and motivates continued development.

---

**Vitalix** — Because *authenticity* deserves *intelligence*.
