#!/usr/bin/env python3
"""Render the GitHub contribution calendar as a monochrome SVG."""
import datetime as dt
import json
import os
import sys
import urllib.request

LOGIN = "hyeongdongE"
OUT = "assets/contributions.svg"
TONES = ["#F0F0F0", "#C8C8C8", "#969696", "#5A5A5A", "#000000"]
LEVELS = ["NONE", "FIRST_QUARTILE", "SECOND_QUARTILE", "THIRD_QUARTILE", "FOURTH_QUARTILE"]
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
QUERY = """query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{
totalContributions weeks{contributionDays{date contributionLevel}}}}}}"""


def fetch(token):
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)
    if data.get("errors"):
        raise SystemExit(f"GitHub API error: {data['errors']}")
    calendar = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = [
        [(dt.date.fromisoformat(day["date"]), LEVELS.index(day["contributionLevel"]))
         for day in week["contributionDays"]]
        for week in calendar["weeks"]
    ]
    return calendar["totalContributions"], weeks


def cell(x, y, size, tone):
    return f'<rect x="{x:.2f}" y="{y:.2f}" width="{size:.2f}" height="{size:.2f}" rx="2" fill="{tone}"/>'


def render(total, weeks):
    width = 720
    pitch = width / len(weeks)
    size = pitch - 2.2
    top = 26
    bottom = top + pitch * 7
    height = bottom + 36
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-8 -8 {width + 16} {height + 16:.2f}" '
        f'role="img" aria-label="{total:,} contributions in the last year">',
        f'<rect x="-8" y="-8" width="{width + 16}" height="{height + 16:.2f}" rx="10" fill="#FFFFFF"/>',
        f'<g font-family="{FONT}" font-size="15" fill="#595959">',
    ]
    last_label = -3
    previous_month = None
    for column, week in enumerate(weeks):
        month = week[0][0].month
        if month != previous_month and column - last_label >= 3 and column < len(weeks) - 2:
            parts.append(f'<text x="{column * pitch + 1:.2f}" y="15">{week[0][0]:%b}</text>')
            last_label = column
        previous_month = month
    parts.append(f'<text x="1" y="{height - 3:.2f}">{total:,} contributions in the last year</text></g>')
    for column, week in enumerate(weeks):
        for day, level in week:
            row = (day.weekday() + 1) % 7
            parts.append(cell(column * pitch + 1.1, top + row * pitch + 1.1, size, TONES[level]))
    for index, tone in enumerate(TONES):
        parts.append(cell(width - (5 - index) * pitch + 1.1, height - pitch - 1, size, tone))
    parts.append("</svg>")
    return "".join(parts)


def main():
    token = os.environ.get("GH_TOKEN")
    if not token:
        raise SystemExit("GH_TOKEN is required")
    total, weeks = fetch(token)
    if total == 0:
        print("No public contribution data returned; keeping the current graph.")
        return
    with open(OUT, "w", encoding="utf-8") as file:
        file.write(render(total, weeks))


if __name__ == "__main__":
    sys.exit(main())
