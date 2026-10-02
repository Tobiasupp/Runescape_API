import logging
import requests
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


class OSRSApiClient:
    BASE_URL = "https://prices.runescape.wiki/api/v1/osrs"
    
    def __init__(self, user_agent: str):
        self.headers = {"User-Agent": user_agent}

    def fetch_mapping(self) -> List[Dict[str, Any]]:
        """Hämtar alla items med namn, ID och High Alch-värde."""
        logger.info("Hämtar mapping-data från API...")
        try:
            response = requests.get(f"{self.BASE_URL}/mapping", headers=self.headers)
            response.raise_for_status()
            logger.debug("Mapping-data hämtades framgångsrikt.")
            return response.json()
        except requests.RequestException as e:
            logger.error("Misslyckades med att hämta mapping-data: %s", e)
            raise

    def fetch_latest_prices(self) -> Dict[str, Dict[str, Any]]:
        """Hämtar de senaste GE-priserna för alla items."""
        logger.info("Hämtar senaste prisdata från API...")
        try:
            response = requests.get(f"{self.BASE_URL}/latest", headers=self.headers)
            response.raise_for_status()
            logger.debug("Prisdata hämtades framgångsrikt.")
            return response.json().get("data", {})
        except requests.RequestException as e:
            logger.error("Misslyckades med att hämta prisdata: %s", e)
            raise