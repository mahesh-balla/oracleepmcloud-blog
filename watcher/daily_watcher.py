import os
import smtplib
import requests
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Config from environment variables
EMAIL_FROM = os.environ["WATCHER_EMAIL_FROM"]
EMAIL_TO = os.environ["WATCHER_EMAIL_TO"]
EMAIL_PASSWORD = os.environ["WATCHER_EMAIL_PASSWORD"]
SITE_URL = "https://www.oracleepmcloud.com"
GITHUB_REPO = "mahesh-balla/oracleepmcloud-blog"

# All routes to check
ROUTES = [
    "/",
    "/epm-cloud-updates/",
    "/epm-cloud-updates/tutorials/",
    "/epm-cloud-updates/tips/",
    "/epm-cloud-updates/use-cases/",
    "/epm-cloud-updates/latest-release/",
    "/narrative-reporting/",
    "/narrative-reporting/tutorials/",
    "/narrative-reporting/tips/",
    "/narrative-reporting/use-cases/",
    "/narrative-reporting/latest-release/",
    "/planning-cloud/",
    "/planning-cloud/tutorials/",
    "/planning-cloud/tips/",
    "/planning-cloud/use-cases/",
    "/planning-cloud/latest-release/",
    "/rss.xml",
]

def check_routes():
    results = []
    for route in ROUTES:
        url = SITE_URL + route
        try:
            r = requests.get(url, timeout=10)
            status = r.status_code
            ok = status == 200
        except Exception as e:
            status = "ERROR"
            ok = False
        results.append({"route": route, "status": status, "ok": ok})
    return results

def get_recent_commits():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/commits?per_page=5"
    try:
        r = requests.get(url, timeout=10)
        commits = r.json()
        return [
            {
                "sha": c["sha"][:7],
                "message": c["commit"]["message"].split("\n")[0],
                "author": c["commit"]["author"]["name"],
                "date": c["commit"]["author"]["date"],
            }
            for c in commits
        ]
    except Exception:
        return []

def get_vercel_status():
    url = f"https://api.vercel.com/v6/deployments?app=oracleepmcloud-blog&limit=1"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        deployments = data.get("deployments", [])
        if deployments:
            d = deployments[0]
            return {
                "state": d.get("state", "unknown"),
                "url": d.get("url", ""),
                "created": d.get("created", ""),
            }
    except Exception:
        pass
    return {"state": "unknown", "url": "", "created": ""}

def build_email(route_results, commits, vercel):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    total = len(route_results)
    passed = sum(1 for r in route_results if r["ok"])
    failed = total - passed

    # Route rows
    route_rows = ""
    for r in route_results:
        color = "#2da44e" if r["ok"] else "#cf222e"
        icon = "✓" if r["ok"] else "✗"
        route_rows += f"""
        <tr>
          <td style="padding:6px 12px;font-family:monospace;font-size:13px;">{r["route"]}</td>
          <td style="padding:6px 12px;color:{color};font-weight:600;">{icon} {r["status"]}</td>
        </tr>"""

    # Commit rows
    commit_rows = ""
    for c in commits:
        commit_rows += f"""
        <tr>
          <td style="padding:6px 12px;font-family:monospace;font-size:12px;color:#0969da;">{c["sha"]}</td>
          <td style="padding:6px 12px;font-size:13px;">{c["message"]}</td>
          <td style="padding:6px 12px;font-size:12px;color:#656d76;">{c["author"]}</td>
        </tr>"""

    summary_color = "#2da44e" if failed == 0 else "#cf222e"
    summary_text = "All systems operational" if failed == 0 else f"{failed} route(s) failing"

    html = f"""
    <html><body style="font-family:Arial,sans-serif;max-width:700px;margin:0 auto;padding:20px;color:#24292f;">

      <div style="background:#0969da;padding:20px;border-radius:8px;margin-bottom:24px;">
        <h1 style="color:white;margin:0;font-size:20px;">Oracle EPM Cloud Blog — Daily Report</h1>
        <p style="color:#cae8ff;margin:8px 0 0;font-size:13px;">{now}</p>
      </div>

      <div style="background:{summary_color};color:white;padding:14px 20px;border-radius:8px;margin-bottom:24px;font-size:15px;font-weight:600;">
        {summary_text} — {passed}/{total} routes OK
      </div>

      <h2 style="font-size:15px;margin-bottom:8px;">Route Health Check</h2>
      <table style="width:100%;border-collapse:collapse;border:1px solid #d0d7de;border-radius:8px;margin-bottom:24px;">
        <thead>
          <tr style="background:#f6f8fa;">
            <th style="padding:8px 12px;text-align:left;font-size:12px;color:#656d76;">Route</th>
            <th style="padding:8px 12px;text-align:left;font-size:12px;color:#656d76;">Status</th>
          </tr>
        </thead>
        <tbody>{route_rows}</tbody>
      </table>

      <h2 style="font-size:15px;margin-bottom:8px;">Recent Commits</h2>
      <table style="width:100%;border-collapse:collapse;border:1px solid #d0d7de;border-radius:8px;margin-bottom:24px;">
        <thead>
          <tr style="background:#f6f8fa;">
            <th style="padding:8px 12px;text-align:left;font-size:12px;color:#656d76;">SHA</th>
            <th style="padding:8px 12px;text-align:left;font-size:12px;color:#656d76;">Message</th>
            <th style="padding:8px 12px;text-align:left;font-size:12px;color:#656d76;">Author</th>
          </tr>
        </thead>
        <tbody>{commit_rows}</tbody>
      </table>

      <h2 style="font-size:15px;margin-bottom:8px;">Vercel Deployment</h2>
      <table style="width:100%;border-collapse:collapse;border:1px solid #d0d7de;border-radius:8px;margin-bottom:24px;">
        <tbody>
          <tr><td style="padding:8px 12px;color:#656d76;font-size:13px;">State</td><td style="padding:8px 12px;font-size:13px;font-weight:600;">{vercel["state"]}</td></tr>
          <tr style="background:#f6f8fa;"><td style="padding:8px 12px;color:#656d76;font-size:13px;">URL</td><td style="padding:8px 12px;font-size:13px;">{vercel["url"]}</td></tr>
        </tbody>
      </table>

      <p style="font-size:12px;color:#656d76;border-top:1px solid #d0d7de;padding-top:16px;">
        Automated report from oracleepmcloud.com watcher · 
        <a href="https://github.com/{GITHUB_REPO}" style="color:#0969da;">View Repository</a>
      </p>

    </body></html>
    """
    return html

def send_email(html, failed_count):
    subject = f"{'✓' if failed_count == 0 else '✗'} EPM Cloud Blog — Daily Report {datetime.now(timezone.utc).strftime('%Y-%m-%d')}"
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    print(f"Email sent to {EMAIL_TO}")

def main():
    print("Running EPM Cloud blog watcher...")
    route_results = check_routes()
    commits = get_recent_commits()
    vercel = get_vercel_status()
    failed = sum(1 for r in route_results if not r["ok"])
    html = build_email(route_results, commits, vercel)
    send_email(html, failed)
    print("Done.")
    if failed > 0:
        exit(1)

if __name__ == "__main__":
    main()