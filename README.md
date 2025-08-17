# GNN Creative Tools Patched

A collection of lightweight Python-based tools for **system auditing**, **network analysis**, and **security assessments**.  
This toolkit is intended for **IT administrators, security professionals, and researchers** to perform controlled and authorized evaluations of their own infrastructure.

---

## 📂 Tools Overview

The `src/` folder contains individual scripts, each designed for a specific task:

- **Network & System Scanning**
  - `ag_taramasi.py` → Basic network scanning
  - `os_servis_tespiti.py` → Operating system & service detection
  - `dis_ip_tespiti.py` → External IP detection
  - `dns_zone_testi.py` → DNS zone transfer test

- **Security & Vulnerability Checks**
  - `patch_yama_denetleyici.py` → Patch & update compliance checker
  - `paylasim_acigi.py` → Shared folder/SMB misconfiguration tester
  - `edr_av_tespiti.py` → EDR / Antivirus presence detection

- **System & Log Analysis**
  - `event_log_extractor.py` → Extract Windows event logs
  - `network_loglayici.py` → Network logger
  - `ntp_senkronizasyon.py` → NTP synchronization test
  - `oturum_acik_kullanicilar.py` → List active sessions

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/BigDesigner/gnncreative-tools-patched.git
cd gnncreative-tools-patched
pip install -r requirements.txt
```

Each tool can be run individually:

```bash
python src/ag_taramasi.py
```

---

## 🚀 Usage

- Designed for **internal audits** and **training environments**.
- Tools are modular; run only what you need.
- Many scripts generate basic reports or console outputs.

---

## 📦 Build (Optional)

This repository includes a GitHub Actions workflow (`.github/workflows/build.yml`)  
to package the scripts into executables (`.exe`) for Windows environments.

---

## 📜 License

MIT License — see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Legal Disclaimer

These tools are provided **for educational purposes, authorized penetration testing, and internal security assessments only**.  
Using them against systems **without explicit permission** is illegal and strictly prohibited.  

The author(s) assume **no liability** and **no responsibility** for any misuse or damage caused by this software.

---

## 🤝 Contributing

Contributions, improvements, and new audit modules are welcome!  
Please open an issue or pull request with details.
