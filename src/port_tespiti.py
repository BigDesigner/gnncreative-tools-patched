import socket, concurrent.futures, ipaddress, datetime
from jinja2 import Template
from _common import ask_report_path

COMMON_PORTS = [21,22,23,25,53,80,110,135,139,143,389,443,445,587,636,993,995,1433,1521,2049,2375,27017,3306,3389,5432,5900,6379,8080,9200]

def scan_host(host):
    openp = []
    for p in COMMON_PORTS:
        try:
            with socket.create_connection((host, p), timeout=0.5):
                openp.append(p)
        except: pass
    return host, openp

def main():
    # IP aralığı al
    target = input("IP (tek IP veya CIDR /24): ").strip()
    hosts = []
    try:
        if "/" in target:
            net = ipaddress.ip_network(target, strict=False)
            hosts = [str(h) for h in net.hosts()]
        else:
            socket.inet_aton(target); hosts = [target]
    except:
        print("Geçersiz IP/CIDR. Ör: 192.168.1.0/24 veya 192.168.1.10"); return

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=128) as ex:
        for h, openp in ex.map(scan_host, hosts): results.append((h, openp))

    # HTML rapor
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = Template("""
    <html><head><meta charset="utf-8"><title>Port Tespiti</title>
    <style>body{font-family:Arial;padding:20px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccc;padding:8px}th{background:#f5f5f5}</style>
    </head><body><h1>Port Tespiti</h1><p><b>Tarih:</b> {{ts}}</p>
    <table><tr><th>Host</th><th>Açık Portlar</th></tr>
    {% for h,ports in rows %}<tr><td>{{h}}</td><td>{{ ", ".join(ports|map('string')) if ports else "-" }}</td></tr>{% endfor %}
    </table><p style="margin-top:24px;color:#666;font-size:12px">GNNcreative tarafından hazırlanmıştır.</p></body></html>
    """).render(ts=ts, rows=[(h, [str(p) for p in openp]) for h, openp in results])

    out = ask_report_path(default_prefix="Port_Tespiti")
    with open(out, "w", encoding="utf-8") as f: f.write(html)

if __name__ == "__main__": main()
