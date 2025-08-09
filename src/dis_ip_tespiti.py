import subprocess, datetime, html
from _common import ask_report_path

def run(cmd):
    try: return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e: return e.output

def main():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    routes = run("route print")
    netrn  = run("netstat -rn")
    body = f"<p><b>Tarih:</b> {ts}</p><h2>route print</h2><pre>{html.escape(routes)}</pre><h2>netstat -rn</h2><pre>{html.escape(netrn)}</pre>"
    out = ask_report_path(default_prefix="Dis_IP_Tespiti")
    with open(out,"w",encoding="utf-8") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'><title>Dış IP Tespiti</title></head><body><h1>Dışarıya Erişimi Olan IP Tespiti</h1>{body}<p style='color:#666;font-size:12px'>GNNcreative</p></body></html>")

if __name__ == "__main__": main()
