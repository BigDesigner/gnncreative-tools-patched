import html
from _common import run, runps, page_wrap, save_html_report

def have(cmd):
    w = run(f"where {cmd}")
    return (("INFO: Could not find" not in w) and ("not found" not in w.lower()))

def main():
    whoami = run("whoami /all")
    if have("dsquery"):
        ds_user = run("dsquery user -limit 50")
        ds_comp = run("dsquery computer -limit 50")
    else:
        ds_user = runps("try { Get-ADUser -Filter * -ResultSetSize 50 | Select-Object SamAccountName, Enabled | Out-String } catch { 'AD cmdlet yok/RSAT gerek.' }")
        ds_comp = runps("try { Get-ADComputer -Filter * -ResultSetSize 50 | Select-Object Name, Enabled | Out-String } catch { 'AD cmdlet yok/RSAT gerek.' }")

    gp = run("gpresult /r")

    body = (f"<h2>whoami /all</h2><pre>{html.escape(whoami)}</pre>"
            f"<h2>AD Kullanıcıları (ilk 50)</h2><pre>{html.escape(ds_user)}</pre>"
            f"<h2>AD Bilgisayarları (ilk 50)</h2><pre>{html.escape(ds_comp)}</pre>"
            f"<h2>Group Policy (gpresult /r)</h2><pre>{html.escape(gp)}</pre>")
    html_page = page_wrap("AD Bilgisi", body)
    path = save_html_report(html_page)
    print(path)

if __name__ == "__main__":
    main()
