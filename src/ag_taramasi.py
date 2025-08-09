import os, socket, datetime, platform, getpass, psutil
from jinja2 import Template
from _common import ask_report_path

def main():
    hostname = socket.gethostname()
    try: ip_address = socket.gethostbyname(hostname)
    except: ip_address = "N/A"
    user = getpass.getuser()
    os_info = platform.platform()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nets = []
    for iface, addrs in psutil.net_if_addrs().items():
        for a in addrs:
            if getattr(socket, "AF_INET", None) and a.family == socket.AF_INET:
                nets.append({"interface": iface, "ip": a.address, "netmask": a.netmask, "broadcast": a.broadcast})

    html = Template("""
    <!DOCTYPE html><html><head><meta charset="utf-8"><title>{{t}}</title>
    <style>body{font-family:Arial;padding:20px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccc;padding:8px}th{background:#f5f5f5}</style>
    </head><body>
    <h1>{{t}}</h1>
    <p><b>Tarih:</b> {{ts}}</p><p><b>Bilgisayar:</b> {{h}}</p><p><b>Kullanıcı:</b> {{u}}</p><p><b>IP:</b> {{ip}}</p><p><b>OS:</b> {{os}}</p>
    <h2>Ağ Arayüzleri</h2>
    <table><tr><th>Arayüz</th><th>IP</th><th>Netmask</th><th>Broadcast</th></tr>
    {% for n in nets %}<tr><td>{{n.interface}}</td><td>{{n.ip}}</td><td>{{n.netmask}}</td><td>{{n.broadcast}}</td></tr>{% endfor %}
    </table>
    <p style="margin-top:24px;color:#666;font-size:12px">GNNcreative tarafından hazırlanmıştır.</p>
    </body></html>
    """).render(t=f"Sistem Bilgi Taraması – {hostname}", ts=timestamp, h=hostname, u=user, ip=ip_address, os=os_info, nets=nets)

    out = ask_report_path(default_prefix="Ag_Taramasi")
    with open(out, "w", encoding="utf-8") as f: f.write(html)

if __name__ == "__main__": main()
