<<<<<<< HEAD
from ultralytics import YOLOv10

model = YOLOv10('yolov10n.yaml')
model.model.model[-1].export = True
model.model.model[-1].format = 'onnx'
del model.model.model[-1].cv2
del model.model.model[-1].cv3
=======
from ultralytics import YOLOv10

model = YOLOv10('yolov10n.yaml')
model.model.model[-1].export = True
model.model.model[-1].format = 'onnx'
del model.model.model[-1].cv2
del model.model.model[-1].cv3
>>>>>>> 9a9dd0c18f58afe7450dacd418695b8e7788d146
model.fuse()