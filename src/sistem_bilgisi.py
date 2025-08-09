import platform, os, getpass, datetime, socket, psutil
from jinja2 import Template
from _common import ask_report_path

def main():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    h = socket.gethostname()
    u = getpass.getuser()
    osinfo = platform.platform()
    cpu = platform.processor()
    mem = psutil.virtual_memory().total // (1024*1024)
    disks = [{"device": p.device, "mount": p.mountpoint, "fstype": p.fstype} for p in psutil.disk_partitions()]

    html = Template("""
    <html><head><meta charset="utf-8"><title>Sistem Bilgisi</title>
    <style>body{font-family:Arial;padding:20px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccc;padding:8px}th{background:#f5f5f5}</style>
    </head><body><h1>Sistem Bilgisi</h1>
    <p><b>Tarih:</b> {{ts}}</p><p><b>Host:</b> {{h}}</p><p><b>Kullanıcı:</b> {{u}}</p><p><b>OS:</b> {{os}}</p><p><b>CPU:</b> {{cpu}}</p><p><b>RAM (MB):</b> {{mem}}</p>
    <h2>Diskler</h2><table><tr><th>Aygıt</th><th>Bağlama</th><th>FS</th></tr>
    {% for d in disks %}<tr><td>{{d.device}}</td><td>{{d.mount}}</td><td>{{d.fstype}}</td></tr>{% endfor %}
    </table><p style="margin-top:24px;color:#666;font-size:12px">GNNcreative tarafından hazırlanmıştır.</p></body></html>
    """).render(ts=ts, h=h, u=u, os=osinfo, cpu=cpu, mem=mem, disks=disks)

    out = ask_report_path(default_prefix="Sistem_Bilgisi")
    with open(out, "w", encoding="utf-8") as f: f.write(html)

if __name__ == "__main__": main()
