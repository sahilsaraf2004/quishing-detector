import cv2
import requests
import numpy as np

def extract_qr_payload(image_bytes: bytes) -> str:
    """Decodes QR code using built-in OpenCV (No C++ DLL issues)."""
    # Convert raw bytes to image array
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        return None

    # Initialize OpenCV's native QR Detector
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    
    if data:
        return data
    return None

def trace_url_redirects(initial_url: str):
    """Follows URL shorteners to find the true target URL."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.head(initial_url, headers=headers, allow_redirects=True, timeout=5)
        chain = [r.url for r in response.history] + [response.url]
        return response.url, chain
    except Exception:
        return initial_url, [initial_url]