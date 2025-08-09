import html
from _common import run, runps, page_wrap, save_html_report

def main():
    services = run("sc query type= service state= all")
    if not services.strip() or services.startswith("[HATA]"):
        services = runps("Get-Service | Sort-Object Status, DisplayName | Format-Table -Auto")

    body = f"<h2>Servis Listesi</h2><pre>{html.escape(services)}</pre>"
    html_page = page_wrap("OS & Servis Tespiti", body)
    path = save_html_report(html_page)
    print(path)

if __name__ == "__main__":
    main()
