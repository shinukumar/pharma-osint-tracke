import os
import requests

def passive_recon(domain):
    print(f"\n=== ATTACK SURFACE MANAGEMENT: ASSET MAPPER ===")
    print(f"[+] Probing public log registries for target: {domain}")
    
    # Fully qualified query endpoint string
    url = f"https://crt.sh%.{domain}&output=json"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
    
    try:
        res = requests.get(url, headers=headers, timeout=25)
        if res.status_code != 200:
            print(f"[-] Log node dropped connection. Status: {res.status_code}")
            return
            
        data = res.json()
        subdomains = set()
        
        for r in data:
            name_value = r.get("name_value", "")
            for item in name_value.split("\n"):
                clean = item.strip().lower()
                if "*" not in clean and clean.endswith(domain):
                    subdomains.add(clean)
                    
        print(f"[!] Active Recon Loop Complete. Isolated {len(subdomains)} unique digital assets.")
        
        os.makedirs("threat_intel_reports", exist_ok=True)
        with open("threat_intel_reports/subdomain_asset_map.txt", "w") as f:
            for sub in sorted(subdomains):
                f.write(f"[+] Mapped Exposed Endpoint: {sub}\n")
                
        print(f"[✓] Mapping dashboard logged cleanly to: threat_intel_reports/subdomain_asset_map.txt")
        
    except Exception as e:
        print(f"[-] Processing loop encountered an error: {e}")
    print("=============================================\n")

if __name__ == "__main__":
    passive_recon("cipla.com")
Deploy passive subdomain mapping framework
