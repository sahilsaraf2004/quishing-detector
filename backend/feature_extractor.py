import re
from urllib.parse import urlparse

def analyze_url_risk(final_url: str):
    """Extracts features and calculates a comprehensive risk score."""
    parsed = urlparse(final_url)
    domain = parsed.netloc.lower()
    full_url_lower = final_url.lower()
    
    risk_score = 0
    flags = []

    # Check 1: Excessive URL length
    if len(final_url) > 75:
        risk_score += 20
        flags.append("Abnormally long URL length")

    # Check 2: IP address used instead of domain
    # Removes port number if present (e.g., 192.168.1.50:8080)
    clean_host = domain.split(':')[0]
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", clean_host):
        risk_score += 40
        flags.append("URL uses an IP address instead of a domain name")

    # Check 3: High-risk TLDs (scans full URL)
    suspicious_tlds = ['.xyz', '.top', '.club', '.work', '.tk', '.ga']
    if any(tld in full_url_lower for tld in suspicious_tlds):
        risk_score += 30
        flags.append("Suspicious Top-Level Domain detected in link")

    # Check 4: Typosquatting / Brand impersonation (scans full URL)
    targets = ["paypal", "paypa1", "google", "goog1e", "apple", "bankofamerica", "binance", "netflix"]
    for brand in targets:
        if brand in full_url_lower and not domain.endswith(f"{brand}.com"):
            risk_score += 35
            flags.append(f"Potential brand impersonation targeting: {brand}")

    # Determine Verdict
    if risk_score >= 60:
        verdict = "MALICIOUS"
    elif risk_score >= 30:
        verdict = "SUSPICIOUS"
    else:
        verdict = "SAFE"

    return {
        "final_url": final_url,
        "risk_score": min(risk_score, 100),
        "verdict": verdict,
        "flags": flags
    }