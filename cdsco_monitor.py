import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Targeting the direct alerts submenu discovered in your recon logs
TARGET_SUBPAGE = "https://cdsco.gov.in/opencms/opencms/en/Latest-Alerts/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def monitor_intel_targets():
    print("\n=======================================================")
    print("      PHARMA OSINT TRACKER - LIVE TARGET AGENT         ")
    print("=======================================================")
    
    # Define our active target watchlist
    watchlist = {
        "pantocid": "Sun Pharma Pantocid (Batch: SID2041A)",
        "urimax": "Cipla Urimax D"
    }
    
    print(f"[+] Activating scanner on subpage: {TARGET_SUBPAGE}")
    try:
        response = requests.get(TARGET_SUBPAGE, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            print(f"[-] Access tracking failed. Status code: {response.status_code}")
            return
            
        print("[+] Processing live data layout columns...")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Scrape and map table alert records
        alert_records = []
        table_rows = soup.find_all('tr')
        
        for row in table_rows:
            cells = row.find_all(['td', 'th'])
            row_text = " ".join([cell.get_text().strip() for cell in cells])
            
            # Extract any document attachments linked inside the row
            link_element = row.find('a', href=True)
            download_url = urljoin(TARGET_SUBPAGE, link_element['href']) if link_element else "None"
            
            if len(row_text) > 5:
                alert_records.append({"data": row_text, "url": download_url})

        print(f"[+] Total threat reports parsed on landing index: {len(alert_records)}")
        print("\n[!] WATChLIST CORRELATION REPORT:")
        
        matches_found = 0
        for record in alert_records:
            record_lower = record["data"].lower()
            
            # Check row metrics against tracking keywords
            for keyword, description in watchlist.items():
                if keyword in record_lower or "spurious" in record_lower or "nsq" in record_lower:
                    matches_found += 1
                    print(f"  [{matches_found}] FLAG: Potential Threat Group Match!")
                    print(f"      Target Rule : {description}")
                    print(f"      Matched Logs: {record['data']}")
                    print(f"      Download URL: {record['url']}\n")
                    break # Move to next record to prevent duplicate printing

        if matches_found == 0:
            print("  [-] Alert level: Green. No active signature overlaps detected in this pass.")
            
    except Exception as e:
        print(f"[-] Execution alert error: {e}")

if __name__ == "__main__":
    monitor_intel_targets()
