import cv2
import time
from cameravalidation import cameras
from ultralytics import YOLO
from flask import Flask, Response
import threading

app = Flask(__name__)
model = YOLO("yolov8n.pt")  # nano - lightest

interval = 0.1 # time between frames - vary according to available compute
latest_frames = {}  # store frames for each camera

def capture_loop(name, url):
    cap = cv2.VideoCapture(url)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    last_time = time.time()
    
    while True:
        cap.grab()
        now = time.time()
        if now - last_time >= interval:
            last_time = now
            ret, frame = cap.retrieve()
            if ret:
                small_frame = cv2.resize(frame, (220, 160))
                results = model(small_frame, verbose=False, classes=[0], conf=0.6)
                annotated_frame = results[0].plot()
                latest_frames[name] = annotated_frame.copy()

def generate_frames(camera_name):
    while True:
        if camera_name in latest_frames:
            _, buffer = cv2.imencode('.jpg', latest_frames[camera_name])
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        time.sleep(0.1)

@app.route('/video_feed/<camera_name>')
def video_feed(camera_name):
    return Response(generate_frames(camera_name),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    camera_feeds = ""
    for name, url in cameras:
        camera_feeds += f'''
        <div style="display: inline-block; margin: 10px; text-align: center;">
            <h3>{name}</h3>
            <img src="/video_feed/{name}" width="440" height="320" style="border: 1px solid #ccc;">
        </div>
        '''
    
    return f'''
    <html>
        <head>
            <title>Multi-Camera Detection Dashboard</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; }}
                .camera-grid {{ display: flex; flex-wrap: wrap; justify-content: center; }}
            </style>
        </head>
        <body>
            <h1>Person detection</h1>
            <div class="camera-grid">
                {camera_feeds}
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    for name, url in cameras:
        capture_thread = threading.Thread(target=capture_loop, args=(name, url), daemon=True)
        capture_thread.start()
        print(f"Started capture thread for camera: {name}")
    
    app.run(host='0.0.0.0', port=5000, debug=False)