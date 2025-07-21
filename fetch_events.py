import json, requests

url = "https://pickleballtournaments.com/tournaments/api/tourneyEvents?slug=5th-annual-gladstone-happy-rockin-by-pig&searchTerm=&needAPartnerOnly=false"
res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
res.raise_for_status()
data = res.json()
with open('tournament_events.json', 'w') as f:
    json.dump(data, f, indent=2)
print('saved tournament_events.json')
