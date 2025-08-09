import os, sys, subprocess, datetime, ctypes, shlex, html

# ==== Privilege & command helpers ====
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def run(cmd):
    try:
        # Use shell=True for Windows builtins; ensure text output
        return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT, encoding="utf-8", errors="ignore")
    except subprocess.CalledProcessError as e:
        return f"[HATA] {cmd}\n{e.output.strip()}"

def runps(ps_cmd):
    # Robust PowerShell execution
    ps_full = f'powershell -NoProfile -ExecutionPolicy Bypass -Command "{ps_cmd}"'
    return run(ps_full)

# ==== Reporting helpers ====
def get_auto_report_path():
    """Create report path next to the executable/script with same base name and .html extension."""
    exe_path = os.path.abspath(sys.argv[0])
    base, _ = os.path.splitext(exe_path)
    return f"{base}.html"

# Backward compatibility: old tools call ask_report_path(...)
def ask_report_path(default_dir_name="Reports", default_prefix="Rapor"):
    """Return auto path without prompting (keeps old API so tools don't need changes)."""
    return get_auto_report_path()

def save_html_report(html_content):
    path = get_auto_report_path()
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_content)
    except Exception as e:
        # Fallback to CWD if writing next to EXE fails
        base = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        path = os.path.abspath(f"{base}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_content)
    return path

def page_wrap(title, body_html):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<style>
body{{font-family:Segoe UI,Arial,sans-serif;padding:20px}}
h1{{margin-top:0}} pre{{white-space:pre-wrap; background:#f7f7f7; padding:12px; border-radius:8px; border:1px solid #eee}}
table{{border-collapse:collapse;width:100%}} td,th{{border:1px solid #ddd;padding:8px}} th{{background:#f5f5f5}}
.footer{{color:#666;font-size:12px;margin-top:16px}}
.notice{{padding:8px 12px; background:#fff8e1; border:1px solid #ffe082; border-radius:8px; margin:12px 0}}
.err{{padding:8px 12px; background:#ffebee; border:1px solid #ffcdd2; border-radius:8px; margin:12px 0}}
code{{background:#f2f2f2; padding:1px 4px; border-radius:4px}}
</style></head>
<body>
<h1>{html.escape(title)}</h1>
<p><b>Tarih:</b> {ts}</p>
{body_html}
<p class="footer">GNNcreative</p>
</body></html>"""
