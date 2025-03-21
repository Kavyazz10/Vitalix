from ultralytics import YOLO

model = YOLO('yolov8n.pt')

def main():
    model.train(data='Dataset/splitData/dataoffline.yaml',epochs=3)



