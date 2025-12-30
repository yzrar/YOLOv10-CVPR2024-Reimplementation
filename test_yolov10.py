from ultralytics import YOLOv10

# 加载官方预训练权重
model = YOLOv10('yolov10s.pt')

# 对示例图片推理
results = model.predict('ultralytics/assets/bus.jpg', save=True, imgsz=640, conf=0.25)

# 打印推理结果（验证是否检测到物体）
print("检测到的类别：", [result.names[result.boxes.cls[i].item()] for result in results for i in range(len(result.boxes.cls))])
print("推理结果保存路径：", results[0].save_dir)