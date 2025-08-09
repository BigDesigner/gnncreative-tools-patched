import subprocess, datetime, html
from _common import ask_report_path

def run(cmd):
    try: return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e: return e.output

def main():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    qfe = run("wmic qfe get HotFixID,InstalledOn /format:table")
    body = f"<p><b>Tarih:</b> {ts}</p><h2>Yüklü Hotfix'ler</h2><pre>{html.escape(qfe)}</pre>"
    out = ask_report_path(default_prefix="Patch_Yama_Denetleyici")
    with open(out,"w",encoding="utf-8") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'><title>Patch/Yama Denetleyici</title></head><body><h1>Patch/Yama Denetleyici</h1>{body}<p style='color:#666;font-size:12px'>GNNcreative</p></body></html>")

if __name__ == "__main__": main()
