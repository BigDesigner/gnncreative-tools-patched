import html, os
from _common import run, runps, page_wrap, save_html_report

def main():
    # 1) Environment Variables (HTTP(S)_PROXY)
    env_info = "\n".join([f"{k}={v}" for k,v in os.environ.items() if k.upper() in ("HTTP_PROXY","HTTPS_PROXY","ALL_PROXY","NO_PROXY")])

    # 2) WinHTTP proxy
    winhttp = run("netsh winhttp show proxy")

    # 3) IE/WinInet proxy (registry)
    ie_proxy = runps('Get-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" | Select-Object ProxyEnable, ProxyServer, AutoConfigURL | Format-List')

    body = (f"<h2>Environment</h2><pre>{html.escape(env_info or '-')}</pre>"
            f"<h2>netsh winhttp</h2><pre>{html.escape(winhttp)}</pre>"
            f"<h2>WinInet/IE Proxy (HKCU)</h2><pre>{html.escape(ie_proxy)}</pre>")

    html_page = page_wrap("Proxy Tespiti", body)
    path = save_html_report(html_page)
    print(path)

if __name__ == "__main__":
    main()
