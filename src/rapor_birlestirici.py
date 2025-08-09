import os, glob, datetime
from _common import ask_report_path

def main():
    folder = input("Raporları içeren klasör (boş: mevcut klasör): ").strip() or os.getcwd()
    files = sorted(glob.glob(os.path.join(folder, "*.html")))
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    links = "".join([f"<li><a href='file:///{os.path.abspath(f)}'>{os.path.basename(f)}</a></li>" for f in files])
    body = f"<p><b>Tarih:</b> {ts}</p><h2>Bulunan Raporlar</h2><ul>{links or '<li>Yok</li>'}</ul>"
    out = ask_report_path(default_prefix="Rapor_Birlestirici")
    with open(out,"w",encoding="utf-8") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'><title>Rapor Birleştirici</title></head><body><h1>Rapor Birleştirici</h1>{body}<p style='color:#666;font-size:12px'>GNNcreative</p></body></html>")

if __name__ == "__main__": main()
