# Pharma OSINT Tracker
This is my solo project tracking pharmaceutical open-source intelligence.
# Asset Mapping & Reconnaissance Pipeline (Pharma OSINT)

An automated target reconnaissance framework built inside Kali Linux designed to map external data assets, simulate manual browser session handshakes to bypass perimeter firewalls, and parse text matrices for specific tracking signatures.

## ⚡ Technical Capabilities Developed
* **Dynamic Access Spoofing:** Utilizes browser session-state cookie replication (`JSESSIONID`) and targeted User-Agent headers to bypass server-side HTML redirect defenses.
* **Asset Discovery Array:** Deep-scans layout rows and unstructured PDF binary elements to extract hidden alphanumeric markers (such as Batch: `SID2041A`).
* **Dual Reporting Engine:** Compiles tracked data streams into structured CSV logs for database indexing while concurrently producing human-readable Markdown summaries.

## 🛠️ Deployment Stack
* **Environment:** Kali Linux (Testing & Extraction Space)
* **Automation Core:** Python 3, PyPDF Core Engine
* **Transport Protocols:** Python Requests Session Layer, Wget Profiling

## 📊 Live System Reporting Preview
Every execution pass compiles an updated text asset log automatically:

```text
# PHARMA OSINT TRACKER - EXECUTIVE THREAT SUMMARY
**Classification:** SYSTEM AUTOMATION AUDIT LOG

## 🚨 Watchlist Alert Overview
System Status: ACTION REQUIRED / TARGET SIGNATURES DETECTED

### Incident #1: Potential Spurious / Counterfeit Match
* Target Rule Group: Sun Pharma Pantocid (Batch: SID2041A)
* Source Document: spurious_evidence.pdf (Page 1)
* Extracted Log Data: "Pantocid - SID2041A 07/2022 06/2025"
```
