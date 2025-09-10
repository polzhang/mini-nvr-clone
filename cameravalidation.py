import cv2
import os
import json

#load config.json from the same folder
config_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_path) as f:
    config = json.load(f)
tovalidate = config["cameras"]


cameras = []
for cam in tovalidate:
    if not cam.get("enabled", True):
        continue
    rtsp_url = cam.get("rtsp_url")
    name = cam.get("id", "unknown")
    if not rtsp_url:
        continue

    #check if rtsp url is valid by grabbing one frame
    cap = cv2.VideoCapture(rtsp_url)
    ret, _ = cap.read()
    cap.release()
    if not ret:
        print(f"Skipping camera '{cam.get('id', 'unknown')}' — unable to read from RTSP stream.")
        continue
    cameras.append([name,rtsp_url])

if not cameras:
    print("No enabled cameras with valid RTSP URL found.")
    exit()
else:
    print(f"Found {len(cameras)} enabled cameras with valid RTSP URL.")


