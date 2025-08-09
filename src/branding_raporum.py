import datetime
from _common import ask_report_path

def main():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = input("Rapor üstbilgisine eklenecek not (ör: GNNcreative Denetimi): ").strip() or "GNNcreative Denetimi"
    body = f"<p><b>Tarih:</b> {ts}</p><p>{text}</p><p>Raporlarınızda bu notu üst bilgi olarak kullanın.</p>"
    out = ask_report_path(default_prefix="Branding_Raporum")
    with open(out,"w",encoding="utf-8") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'><title>Branding Raporum</title></head><body><h1>Branding Raporum</h1>{body}<p style='color:#666;font-size:12px'>GNNcreative</p></body></html>")

if __name__ == "__main__": main()
