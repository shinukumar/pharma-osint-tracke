import os
import csv
from datetime import datetime
import requests

EVIDENCE_LOG = "threat_intel_reports/osint_evidence_matrix.csv"

def initialize_evidence_vault():
    if not os.path.exists("threat_intel_reports"):
        os.makedirs("threat_intel_reports")

def execute_target_intel_sweep(username):
    print("\n=======================================================")
    print("     OSINT TARGET INVESTIGATOR - EVIDENCE HARVESTER    ")
    print("=======================================================")
    print(f"[+] Commencing cross-platform reconnaissance sweep on alias: {username}")
    initialize_evidence_vault()
    
    # Explicit domain linkages to bypass terminal parsing glitches
    target_vectors = {
        "X (Twitter)": "https://x.com" + username,
        "Instagram": "https://instagram.com" + username,
        "TikTok": "https://tiktok.com@" + username,
        "Reddit": "https://reddit.com" + username,
        "GitHub": "https://github.com" + username,
        "Pinterest": "https://pinterest.com" + username
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    }
    
    evidence_records = []
    
    for platform, url in target_vectors.items():
        print(f"  [→] Probing digital surface array: {platform}...")
        try:
            res = requests.get(url, headers=headers, timeout=10, allow_redirects=False)
            if res.status_code == 200:
                print(f"    [!] POSITIVE INDICATOR: Active asset found on {platform}")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
                
                evidence_records.append({
                    "Timestamp": timestamp,
                    "Target Alias": username,
                    "Platform Vector": platform,
                    "Forensic URL Link": url,
                    "Case Description": "Active target footprint located. Profile validation mandatory for potential impersonation or data exposure metrics."
                })
        except Exception as e:
            print(f"    [-] Interface timeout on platform vector {platform}: {e}")
            
    if evidence_records:
        print(f"\n[!] Sweep complete. Hardcoding {len(evidence_records)} evidence fields to database...")
        fields = ["Timestamp", "Target Alias", "Platform Vector", "Forensic URL Link", "Case Description"]
        
        with open(EVIDENCE_LOG, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(evidence_records)
        print(f"[✓] Case evidence logging matrix saved successfully: {EVIDENCE_LOG}")
    else:
        print("\n[-] Scan execution complete. No target footprint visibility indicators found on public vectors.")
    print("=======================================================\n")

if __name__ == "__main__":
    execute_target_intel_sweep("dhruvshi")
