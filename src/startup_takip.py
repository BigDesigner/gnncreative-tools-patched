import subprocess, datetime, html
from _common import ask_report_path

def runps(ps):
    cmd = f'powershell -Command "{ps}"'
    try: return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e: return e.output

def main():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    startup = runps("Get-CimInstance Win32_StartupCommand | Select Name, Command, Location | Format-Table -Auto")
    body = f"<p><b>Tarih:</b> {ts}</p><h2>Startup Programları</h2><pre>{html.escape(startup)}</pre>"
    out = ask_report_path(default_prefix="Startup_Takip")
    with open(out,"w",encoding="utf-8") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'><title>Startup Takip</title></head><body><h1>Startup Takip</h1>{body}<p style='color:#666;font-size:12px'>GNNcreative</p></body></html>")

if __name__ == "__main__": main()
