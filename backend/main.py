from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from qr_engine import extract_qr_payload, trace_url_redirects
from feature_extractor import analyze_url_risk

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Quishing Detector API is running!"}

@app.post("/api/scan")
async def scan_qr(file: UploadFile = File(...)):
    image_bytes = await file.read()
    
    # 1. Immediate exit on frame skips / no QR found
    payload = extract_qr_payload(image_bytes)
    if not payload:
        raise HTTPException(status_code=400, detail="No QR code found in the image.")
    
    # 2. Executed ONLY when a real QR code is detected in the video frame
    final_url, redirect_chain = trace_url_redirects(payload)
    risk_analysis = analyze_url_risk(final_url)
    
    return {
        "raw_payload": payload,
        "redirect_chain": redirect_chain,
        **risk_analysis
    }