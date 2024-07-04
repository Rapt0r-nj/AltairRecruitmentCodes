from ultralytics import YOLOv10
import cv2
import supervision as sv

model = YOLOv10('./weights.pt')

def detect_swan(image_path, output_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image")
        return

    results = model(image)[0]

    detections = sv.Detections.from_ultralytics(results)

    bounding_box_annotator = sv.BoundingBoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

    cv2.imwrite(output_path, annotated_image)

image_path = './sample.jpg'
output_path = './output.jpg'
detect_swan(image_path, output_path)
