# Mini NVR Clone with YOLOv11n

A **shitty clone of Frigate NVR**. Reads RTSP streams (IP camera etc) and uses **YOLOv11n** for **person/object detection**. Displays live feeds on a dashboard at `http://localhost:5000` - meant to emulate a plug-and-play surveillance solution

## Features

* Multi-camera **RTSP stream capture**
* **Person/object** detection using **YOLOv11n**
* Live feed dashboard (localhost only)
* *Planned:* recording, alert dashboard, motion-triggered recording, remote access

## Setup and Usage

1. **Clone repository:**
```bash
git clone https://github.com/polzhang/mini-nvr-clone
cd mini-nvr-clone
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure cameras in `config.json`:**
```json
{
  "cameras": [
    {
      "id": "sample_camera",
      "rtsp_url": "sample_rtsp_url",
      "enabled": true,
      "recording": {
        "save": true,
        "path": "recordings/livingroom/",
        "max_file_size_mb": 500
      }
    }
  ]
}
```

4. **Run the application:**
```bash
python main.py
```

5. **Open your browser and go to:**
```
http://localhost:5000
```

## Requirements

- Python 3.11+
- OpenCV
- Ultralytics (YOLOv11)
- Flask
- RTSP-enabled cameras

## Configuration

Edit `config.json` to add your RTSP camera streams. Each camera entry should include:
- `id`: Unique identifier for the camera
- `rtsp_url`: Full RTSP stream URL (e.g., `rtsp://username:password@camera_ip:554/stream`)
- `enabled`: Boolean to enable/disable the camera
- `recording`: Recording settings (path, file size limits, etc.) (currently useless)

