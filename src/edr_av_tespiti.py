import subprocess, datetime, html
from _common import ask_report_path

def run_wmi(namespace, klass):
    ps = f'Get-CimInstance -Namespace {namespace} -ClassName {klass} | Select-Object * | Format-List'
    cmd = f'powershell -Command "{ps}"'
    try: return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e: return e.output

def main():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    av = run_wmi("root/SecurityCenter2", "AntiVirusProduct")
    body = f"<p><b>Tarih:</b> {ts}</p><h2>AV/EDR Ürünleri</h2><pre>{html.escape(av)}</pre>"
    out = ask_report_path(default_prefix="EDR_AV_Tespiti")
    with open(out,"w",encoding="utf-8") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'><title>EDR/AV Tespiti</title></head><body><h1>EDR/AV Tespiti</h1>{body}<p style='color:#666;font-size:12px'>GNNcreative</p></body></html>")

if __name__ == "__main__": main()
