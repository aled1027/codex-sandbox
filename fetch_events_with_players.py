import json
from pathlib import Path
import requests
from playwright.sync_api import sync_playwright

EVENTS_URL = "https://pickleballtournaments.com/tournaments/api/tourneyEvents?slug=5th-annual-gladstone-happy-rockin-by-pig&searchTerm=&needAPartnerOnly=false"
PLAYERS_URL = "https://pickleballtournaments.com/tournaments/api/eventPlayers"


def visit_events_page():
    """Use Playwright to visit the events page just to verify connectivity."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(ignore_https_errors=True)
        page.goto("https://pickleballtournaments.com/tournaments/5th-annual-gladstone-happy-rockin-by-pig/events")
        page.wait_for_timeout(1000)
        print("Visited events page:", page.title())
        browser.close()


def fetch_events():
    res = requests.get(EVENTS_URL, headers={"User-Agent": "Mozilla/5.0"})
    res.raise_for_status()
    return res.json()["events"]


def fetch_players(activity_id, activity_split_id):
    params = {
        "activityId": activity_id,
        "activitySplitId": activity_split_id,
    }
    res = requests.get(PLAYERS_URL, params=params, headers={"User-Agent": "Mozilla/5.0"})
    res.raise_for_status()
    return res.json()


def main():
    visit_events_page()  # attempt with Playwright
    all_events = fetch_events()
    for group in all_events:
        for event in group.get("events", []):
            if event.get("activityId") and event.get("activitySplitId"):
                try:
                    event["players"] = fetch_players(event["activityId"], event["activitySplitId"])
                except Exception as e:
                    print("failed to fetch players for", event.get("title"), e)
    Path("tournament_events_with_players.json").write_text(json.dumps(all_events, indent=2))
    print("saved tournament_events_with_players.json")


if __name__ == "__main__":
    main()
