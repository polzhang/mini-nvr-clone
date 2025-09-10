# Mini NVR Clone with YOLOv8n

A **shitty clone of Frigate NVR**. Reads RTSP streams (IP camera etc) and uses **YOLOv8n** for **person/object detection**. Displays live feeds on a dashboard at `http://localhost:5000`. Meant to be a plug-and-play surveillance solution.

## Features

* Multi-camera **RTSP stream capture**
* **Computer vision** detections using **YOLOv8n**
* Live feed dashboard (localhost only)
* *Planned:* recording, alert dashboard, motion-triggered recording, remote access

## Setup and usage

1. Clone repository:

```bash
git clone <your-repo-url>
cd mini-nvr-clone
```

2. Configure cameras in `config.json`:

```json
{
  "cameras": [
    {
      "id": "test",
      "rtsp_url": "http://61.211.241.239/nphMotionJpeg?Resolution=320x240&Quality=Standard",
      "enabled": true,
      "recording": {
        "save": true,
        "path": "recordings/front_door/",
        "max_file_size_mb": 500
      }
    }
  ]
}
```

3.

Run docker container:

```bash
docker run -p 5000:5000 mini-nvr-clone
```

Open `http://localhost:5000` to view **live feeds with YOLOv8n detections**.

