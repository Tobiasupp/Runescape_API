# OSRS Item Lookup Tool

Ett Python-program som hämtar information om föremål i Old School RuneScape (OSRS), inklusive High Alch-värden och aktuella priser från Grand Exchange.

## Externa tjänster och Data
Projektet använder **OSRS Wiki API** (`https://prices.runescape.wiki/api/v1/osrs`):
- `/mapping`: Innehåller ID, namn och High Alch-värden för alla items.
- `/latest`: Innehåller realtidsdata för Grand Exchange-priser (köp/sälj).

API-anropen kväler en anpassad `User-Agent`-header enligt OSRS Wikis riktlinjer


## Installation och körning

1. **Klona eller ladda ned projektet.**
2. **Skapa och aktivera en virtuell miljö (valfritt men rekommenderat):**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate



Jag använder mig enbart av Pythons standardbibliotek så inga externa pip paket behöver installeras.

För att köra programmet: python main.py