# Tournament Data Fetcher

This repository contains scripts to fetch tournament event information and registered players from PickleballTournaments.com.

## Scripts

- `fetch_events.py` - fetches basic tournament event data.
- `fetch_events_with_players.py` - visits the tournament page with Playwright and then retrieves participants for each event via API.

Run `python fetch_events_with_players.py` to generate `tournament_events_with_players.json`.
