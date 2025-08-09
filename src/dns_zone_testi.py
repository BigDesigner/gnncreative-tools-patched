import subprocess, datetime, html
from _common import ask_report_path

def run(cmd):
    try: return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e: return e.output

def main():
    domain = input("DNS domain (ör: example.local): ").strip()
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ns = run(f"nslookup -type=ns {domain}")
    axfr = run(f"nslookup -type=any -query=AXFR {domain}")

    body = f"<p><b>Tarih:</b> {ts}</p><p><b>Domain:</b> {html.escape(domain)}</p><h2>NS</h2><pre>{html.escape(ns)}</pre><h2>AXFR</h2><pre>{html.escape(axfr)}</pre>"
    out = ask_report_path(default_prefix="DNS_Zone_Testi")
    with open(out,"w",encoding="utf-8") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'><title>DNS Zone Testi</title></head><body><h1>DNS Zone Testi</h1>{body}<p style='color:#666;font-size:12px'>GNNcreative</p></body></html>")

if __name__ == "__main__": main()
