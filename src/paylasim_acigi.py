import html
from _common import run, runps, is_admin, page_wrap, save_html_report

def main():
    if is_admin():
        shares = runps("Get-SmbShare | Where-Object {$_.Special -eq $false} | Select-Object Name, Path, Description | Format-Table -Auto")
    else:
        shares = run("net share")

    body = f"<h2>Paylaşımlar</h2><pre>{html.escape(shares)}</pre>"
    html_page = page_wrap("Paylaşım Açığı", body)
    path = save_html_report(html_page)
    print(path)

if __name__ == "__main__":
    main()
