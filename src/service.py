import logging
from typing import Optional
from src.api_client import OSRSApiClient
from src.models import Item

logger = logging.getLogger(__name__)


class ItemService:
    def __init__(self, api_client: OSRSApiClient):
        self.api_client = api_client

    def get_item_by_name(self, name: str) -> Optional[Item]:
        """Söker upp ett item via namn och kombinerar mapping med GE-priser."""
        mapping_data = self.api_client.fetch_mapping()
        
        matched_dict = next(
            (item for item in mapping_data if item.get("name", "").lower() == name.lower()),
            None
        )

        if not matched_dict:
            logger.info("Ingen matchning hittades i mapping för: '%s'", name)
            return None

        item_id = matched_dict["id"]
        logger.info("Matchning funnen: %s (ID: %d)", matched_dict['name'], item_id)

        prices_data = self.api_client.fetch_latest_prices()
        item_prices = prices_data.get(str(item_id), {})

        return Item(
            id=item_id,
            name=matched_dict["name"],
            high_alch=matched_dict.get("highalch"),
            ge_high=item_prices.get("high"),
            ge_low=item_prices.get("low")
        )