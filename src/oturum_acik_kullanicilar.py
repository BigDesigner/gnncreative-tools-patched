import subprocess, datetime, html
from _common import ask_report_path

def run(cmd):
    try: return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e: return e.output

def main():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quser = run("query user")
    wmic = run("wmic computersystem get username")
    body = f"<p><b>Tarih:</b> {ts}</p><h2>query user</h2><pre>{html.escape(quser)}</pre><h2>WMIC username</h2><pre>{html.escape(wmic)}</pre>"
    out = ask_report_path(default_prefix="Oturum_Acik_Kullanicilar")
    with open(out,"w",encoding="utf-8") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'><title>Oturum Açık Kullanıcılar</title></head><body><h1>Oturum Açık Kullanıcılar</h1>{body}<p style='color:#666;font-size:12px'>GNNcreative</p></body></html>")

if __name__ == "__main__": main()
