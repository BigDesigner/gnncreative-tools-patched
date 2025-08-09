import os, html
from _common import runps, page_wrap, save_html_report

def main():
    host = os.environ.get("COMPUTERNAME","")
    # Dil bağımsız: Yerel admin grubu SID ile
    admins = runps("$g = Get-LocalGroup -SID 'S-1-5-32-544'; Get-LocalGroupMember -Group $g | Select-Object Name, ObjectClass | Format-Table -Auto")
    if not admins.strip():
        # Fallback
        admins = runps("try { net localgroup Administrators } catch { $_ | Out-String }")

    body = f"<p><b>Host:</b> {html.escape(host)}</p><h2>Yöneticiler</h2><pre>{html.escape(admins)}</pre>"
    html_page = page_wrap("Yerel Admin Kontrol", body)
    path = save_html_report(html_page)
    print(path)

if __name__ == "__main__":
    main()
