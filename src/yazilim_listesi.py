import winreg, datetime
from jinja2 import Template
from _common import ask_report_path

UNINSTALL_PATHS = [
    r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
    r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
]

def enum_installed():
    rows = []
    for root in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
        for path in UNINSTALL_PATHS:
            try:
                with winreg.OpenKey(root, path) as key:
                    for i in range(0, winreg.QueryInfoKey(key)[0]):
                        try:
                            sk = winreg.OpenKey(key, winreg.EnumKey(key, i))
                            name = ver = pub = ""
                            try: name = winreg.QueryValueEx(sk, "DisplayName")[0]
                            except: pass
                            try: ver = winreg.QueryValueEx(sk, "DisplayVersion")[0]
                            except: pass
                            try: pub = winreg.QueryValueEx(sk, "Publisher")[0]
                            except: pass
                            if name: rows.append((name, ver, pub))
                        except: pass
            except: pass
    rows.sort(key=lambda x: x[0].lower())
    return rows

def main():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = enum_installed()
    html = Template("""
    <html><head><meta charset="utf-8"><title>Yüklü Yazılımlar</title>
    <style>body{font-family:Arial;padding:20px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccc;padding:8px}th{background:#f5f5f5}</style>
    </head><body><h1>Yüklü Yazılımlar</h1><p><b>Tarih:</b> {{ts}}</p>
    <table><tr><th>Ad</th><th>Sürüm</th><th>Yayımcı</th></tr>
    {% for n,v,p in rows %}<tr><td>{{n}}</td><td>{{v}}</td><td>{{p}}</td></tr>{% endfor %}
    </table><p style="margin-top:24px;color:#666;font-size:12px">GNNcreative tarafından hazırlanmıştır.</p></body></html>
    """).render(ts=ts, rows=data)

    out = ask_report_path(default_prefix="Yazilim_Listesi")
    with open(out, "w", encoding="utf-8") as f: f.write(html)

if __name__ == "__main__": main()
