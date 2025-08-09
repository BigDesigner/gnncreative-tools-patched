import html
from _common import runps, page_wrap, save_html_report

def main():
    state = runps("(Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol).State")
    if not state.strip():
        state = runps("dism /online /Get-Features /Format:Table | Select-String -Pattern '^SMB1Protocol' | Out-String")
    reg = runps('Get-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\LanmanServer\\Parameters" -Name SMB1 -ErrorAction SilentlyContinue | Format-List')

    body = f"<h2>SMBv1 Durumu</h2><pre>{html.escape(state)}</pre><h2>Registry</h2><pre>{html.escape(reg)}</pre>"
    html_page = page_wrap("SMBv1 Kontrol", body)
    path = save_html_report(html_page)
    print(path)

if __name__ == "__main__":
    main()
