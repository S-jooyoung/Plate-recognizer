# License plate recognition and detection.

![Python](https://img.shields.io/badge/python-v3.9.4+-blue.svg)
![Cv2](https://img.shields.io/badge/cv2-4.5.4+-yellow)

## Basic Overview

This repository is a solution that recognizes and detects license plates.

---

## Getting Start

- Clone Plate-recognizer to your hard drive with `https://github.com/S-jooyoung/Plate-recognizer.git`
- Download the pretrained model from:https://drive.google.com/file/d/1VTFpw9T8VhgaSbCWLS_cqfA4TtnMzfsI/view?usp=sharing

- install tesseractOCR:
  `https://github.com/tesseract-ocr/tesseract`
- Put a license plate video that you want to detect.

```python
#car_detection.py

cap = cv2.VideoCapture("sample.mp4")

net = cv2.dnn.readNetFromDarknet('cfg/yolov4-ANPR.cfg', 'yolov4-ANPR.weights')
```

- run `python car_detection.py`

---

## Example

<img src="sample.JPG" width=500 height=300>

---

## Learn

- If you want to know the license plate recognition principle, refer to it `main.ipynb`

---

## References

- Paper
  - [You Only Look Once : Unified, Real-Time Object Detection](https://pjreddie.com/media/files/papers/yolo_1.pdf)
  - [YOLO9000 : Better, Faster, Stronger](https://pjreddie.com/media/files/papers/YOLO9000.pdf)
  - [YOLOv3 : An Incremental Improvement](https://pjreddie.com/media/files/papers/YOLOv3.pdf)
  - [YOLOv4：Optimal Speed and Accuracy of Object Detection](https://arxiv.org/pdf/2004.10934.pdf)
- Keras-yolov3
  - weights to h5 : https://github.com/qqwweee/keras-yolo3/blob/master/convert.py
  - weights to mlmodel : https://gist.github.com/TakaoNarikawa/aef13571eec97d78603688eef05b5389
  - Mish : https://qiita.com/TakaoNarikawa/items/e4521fd8c7a522e9d4fd
- Core ML
  - https://gist.github.com/TakaoNarikawa
  - https://github.com/Ma-Dan/YOLOv3-CoreML

---

## Contributing

Let's connect 👨‍💻 and forge the future together.😁✌

**Check the Repositories and don't forget to give a star.** 👇

:star: From [S-jooyoung](https://github.com/S-jooyoung)
