
import supervision as sv
from ultralytics import YOLO

video_path = "../../data/videos/79865-570708317_small.mp4"
model = YOLO("../../data/models/yolov8s.pt")
video_info = sv.VideoInfo.from_video_path(video_path)
frames_generator = sv.get_video_frames_generator(source_path=video_path)

box_annotator = sv.BoxAnnotator(thickness=2)

# Create a set to store the names of all detected object types
detected_objects = set()

with sv.VideoSink("../../data/output/output.mp4", video_info) as sink:
    for frame in frames_generator:
        result = model(frame)[0]
        detections = sv.Detections.from_ultralytics(result)
        
        # Add the names of all detected object types to the set
        for class_id in detections.class_id:
            detected_objects.add(model.model.names[class_id])

        annotated_frame = box_annotator.annotate(
            scene=frame.copy(), 
            detections=detections
        )
        sink.write_frame(annotated_frame)

# Print the different types of detected objects
print("Detected object types:")
for obj_type in detected_objects:
    print(f"- {obj_type}")
