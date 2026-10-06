import os
from pypdf import PdfReader

TARGET_FILES = [
    "threat_intel_reports/spurious_evidence.pdf"
]

def extract_target_context():
    print("\n=======================================================")
    print("      PHARMA OSINT TRACKER - DEEP CONTEXT EXTRACTOR   ")
    print("=======================================================")
    
    # Watch targets
    watchlist = ["pantocid", "sid2041a", "urimax"]
    
    for filepath in TARGET_FILES:
        if not os.path.exists(filepath):
            print(f"[-] Target missing: {filepath}")
            continue
            
        print(f"\n[+] Extracting hit lines from: {filepath}")
        try:
            reader = PdfReader(filepath)
            
            for page_idx, page in enumerate(reader.pages, 1):
                page_text = page.extract_text()
                if not page_text:
                    continue
                
                # Split the page text arrays into individual readable sentences/lines
                lines = page_text.split('\n')
                
                for line in lines:
                    line_lower = line.lower()
                    # Check if the line matches any target keywords
                    if any(target in line_lower for target in watchlist):
                        print(f"\n[!] MATCH DETECTED [PAGE {page_idx}]:")
                        print(f"    ↳ Context Data: {line.strip()}")
                        
        except Exception as e:
            print(f"    [×] Processing failure: {e}")
            
    print("\n=======================================================")
    print("[!] Intelligence text extraction cycle finished.")
    print("=======================================================")

if __name__ == "__main__":
    extract_target_context()
