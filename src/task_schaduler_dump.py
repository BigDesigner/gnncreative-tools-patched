import html
from _common import run, runps, page_wrap, save_html_report

def main():
    tasks = run("schtasks /query /fo LIST /v")
    if not tasks.strip() or tasks.startswith("[HATA]"):
        tasks = runps("Get-ScheduledTask | Get-ScheduledTaskInfo | Select-Object TaskName, LastRunTime, NextRunTime, State | Format-Table -Auto")

    body = f"<h2>Zamanlanmış Görevler</h2><pre>{html.escape(tasks)}</pre>"
    html_page = page_wrap("Task Scheduler Dump", body)
    path = save_html_report(html_page)
    print(path)

if __name__ == "__main__":
    main()
