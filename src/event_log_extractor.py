import html
from _common import runps, save_html_report, page_wrap, is_admin

def main():
    sec = "(Yönetici değil: Security log atlandı.)"
    if is_admin():
        sec = runps("Get-WinEvent -LogName Security -MaxEvents 50 | Select-Object TimeCreated, Id, ProviderName, LevelDisplayName, Message | Format-Table -Auto")

    sysl = runps("Get-WinEvent -LogName System -MaxEvents 50 | Select-Object TimeCreated, Id, ProviderName, LevelDisplayName, Message | Format-Table -Auto")
    appl = runps("Get-WinEvent -LogName Application -MaxEvents 50 | Select-Object TimeCreated, Id, ProviderName, LevelDisplayName, Message | Format-Table -Auto")

    body = f"<h2>Security (50)</h2><pre>{html.escape(sec)}</pre>" \
           f"<h2>System (50)</h2><pre>{html.escape(sysl)}</pre>" \
           f"<h2>Application (50)</h2><pre>{html.escape(appl)}</pre>"
    html_page = page_wrap("Event Log Extractor", body)
    path = save_html_report(html_page)
    print(path)

if __name__ == "__main__":
    main()
