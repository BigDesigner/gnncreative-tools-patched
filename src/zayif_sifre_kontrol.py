import html
from _common import runps, page_wrap, save_html_report, is_admin

def main():
    # Varsayılan olarak parola denemesi YOK; yalnızca hesap/politika özeti
    acc = runps("net accounts")
    pol = runps("secedit /export /cfg $env:TEMP\\secpol.cfg; Get-Content $env:TEMP\\secpol.cfg | Out-String")

    warn = ""
    if not is_admin():
        warn = '<div class="notice">Uyarı: Admin yetkisi yok, bazı denetimler eksik olabilir. Varsayılan olarak parola denemesi yapılmaz.</div>'

    body = warn + f"<h2>Net Accounts</h2><pre>{html.escape(acc)}</pre><h2>Security Policy (secedit)</h2><pre>{html.escape(pol)}</pre>"
    html_page = page_wrap("Zayıf Şifre Kontrol (Özet)", body)
    path = save_html_report(html_page)
    print(path)

if __name__ == "__main__":
    main()
