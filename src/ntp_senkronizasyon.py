import html
from _common import run, runps, page_wrap, save_html_report

def main():
    status = run("w32tm /query /status")
    peers = run("w32tm /query /peers")
    if ("The following error occurred" in status) or (not status.strip()):
        status = runps("Get-Service W32Time | Format-Table Status, StartType, Name -Auto")
        if not peers.strip():
            peers = runps("w32tm /query /peers")

    body = f"<h2>NTP Durumu</h2><pre>{html.escape(status)}</pre><h2>Peers</h2><pre>{html.escape(peers)}</pre>"
    html_page = page_wrap("NTP Senkronizasyon", body)
    path = save_html_report(html_page)
    print(path)

if __name__ == "__main__":
    main()
