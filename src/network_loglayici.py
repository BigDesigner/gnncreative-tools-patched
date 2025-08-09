import subprocess, datetime, html, time
from _common import ask_report_path

def run(cmd):
    try: return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e: return e.output

def main():
    duration = input("Kaç saniye netstat örneklemesi? (örn 5): ").strip()
    try: duration = max(1, int(duration))
    except: duration = 5
    samples = []
    for _ in range(duration):
        samples.append(run("netstat -ano"))
        time.sleep(1)

    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    joined = "\n\n--- SAMPLE ---\n\n".join([html.escape(s) for s in samples])
    body = f"<p><b>Tarih:</b> {ts}</p><h2>Netstat Örnekleri ({duration} sn)</h2><pre>{joined}</pre>"
    out = ask_report_path(default_prefix="Network_Loglayici")
    with open(out,"w",encoding="utf-8") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'><title>Network Loglayıcı</title></head><body><h1>Network Loglayıcı</h1>{body}<p style='color:#666;font-size:12px'>GNNcreative</p></body></html>")

if __name__ == "__main__": main()
