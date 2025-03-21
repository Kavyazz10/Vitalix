import cv2
import cvzone
import math
import time

# Define configuration parameters
camWidth = 640
camHeight = 480
confidence = 0.5  # Example confidence threshold
offsetPercentageW = 10  # Example offset percentage
offsetPercentageH = 10  # Example offset percentage
blurThreshold = 100  # Example blur threshold
classID = 0  # Example class ID
debug = False  # Set to True for debugging
save = True  # Set to True to save images and labels
outputFolderPath = "output"  # Directory to save outputs
floatingPoint = 6

# Placeholder for FaceDetector class; replace with actual implementation
class FaceDetector:
    def findFaces(self, img, draw=True):
        # Placeholder implementation
        # Return a tuple of (img, bboxs) where bboxs is a list of bounding box dictionaries
        return img, []

# Initialize video capture and FaceDetector
cap = cv2.VideoCapture(0)
cap.set(3, camWidth)
cap.set(4, camHeight)

detector = FaceDetector()  # Initialize the FaceDetector

while True:
    success, img = cap.read()
    if not success:
        break  # Exit loop if no frame is captured

    imgOut = img.copy()
    img, bboxs = detector.findFaces(img, draw=False)  # Ensure `detector.findFaces` works as expected

    listBlur = []  # List indicating if faces are blurred
    listInfo = []  # List for normalized values and class names

    if bboxs:
        for bbox in bboxs:
            x, y, w, h = bbox["bbox"]
            score = bbox["score"][0]
            print(x, y, w, h)

            # Check the score
            if score > confidence:
                # Add offset to the face detected
                offsetW = (offsetPercentageW / 100) * w
                x = int(x - offsetW)
                w = int(w + offsetW * 2)
                offsetH = (offsetPercentageH / 100) * h
                y = int(y - offsetH * 3)
                h = int(h + offsetH * 3.5)

                # Avoid values below 0
                x = max(x, 0)
                y = max(y, 0)
                w = max(w, 0)
                h = max(h, 0)

                # Find blurriness
                imgFace = img[y:y + h, x:x + w]
                cv2.imshow("Face", imgFace)
                blurValue = int(cv2.Laplacian(imgFace, cv2.CV_64F).var())
                listBlur.append(blurValue > blurThreshold)

                # Normalize values
                ih, iw, _ = img.shape
                xc, yc = x + w / 2, y + h / 2
                xcn, ycn = round(xc / iw, floatingPoint), round(yc / ih, floatingPoint)
                wn, hn = round(w / iw, floatingPoint), round(h / ih, floatingPoint)

                # Avoid values above 1
                xcn = min(xcn, 1)
                ycn = min(ycn, 1)
                wn = min(wn, 1)
                hn = min(hn, 1)

                listInfo.append(f"{classID} {xcn} {ycn} {wn} {hn}\n")

                # Drawing
                cv2.rectangle(imgOut, (x, y, w, h), (255, 0, 0), 3)
                cvzone.putTextRect(imgOut, f'Score: {int(score * 100)}% Blur: {blurValue}', (x, y - 20),
                                   scale=2, thickness=3)
                if debug:
                    cv2.rectangle(img, (x, y, w, h), (255, 0, 0), 3)
                    cvzone.putTextRect(img, f'Score: {int(score * 100)}% Blur: {blurValue}', (x, y - 20),
                                       scale=2, thickness=3)

        # Save image and label file
        if save and all(listBlur):
            timeNow = str(int(time.time()))
            cv2.imwrite(f"{outputFolderPath}/{timeNow}.jpg", img)
            with open(f"{outputFolderPath}/{timeNow}.txt", 'w') as f:
                f.writelines(listInfo)

    cv2.imshow("Image", imgOut)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
