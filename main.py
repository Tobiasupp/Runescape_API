import logging
from src.api_client import OSRSApiClient
from src.service import ItemService

# Konfigurera den globala loggern
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

PROFIT_SCHOOL_AGENT = "osrs_item_lookup_tool - contact: myemail@example.com"


def log_item_info(item):
    logger.info("--- Träff hittades ---")
    logger.info("Item: %s (ID: %d)", item.name, item.id)
    
    ha_str = f"{item.high_alch:,} gp" if item.high_alch is not None else "Saknas"
    high_str = f"{item.ge_high:,} gp" if item.ge_high is not None else "Saknas"
    low_str = f"{item.ge_low:,} gp" if item.ge_low is not None else "Saknas"
    
    logger.info("High Alch Value : %s", ha_str)
    logger.info("GE High (Köp)   : %s", high_str)
    logger.info("GE Low (Sälj)   : %s", low_str)
    
    if item.alch_profit is not None:
        logger.info("Bruttovinst Alch: %s gp", f"{item.alch_profit:,}")


def main():
    api_client = OSRSApiClient(user_agent=PROFIT_SCHOOL_AGENT)
    service = ItemService(api_client=api_client)

    query = input("Sök på ett OSRS item (t.ex. Rune scimitar): ").strip()
    if not query:
        logger.warning("Användaren angav en tom söksträng.")
        return

    logger.info("Startar sökning efter: '%s'", query)
    
    try:
        item = service.get_item_by_name(query)
        if item:
            log_item_info(item)
        else:
            logger.warning("Hittade inget item med namnet '%s'.", query)
    except Exception as e:
        logger.error("Ett fel uppstod vid sökning: %s", e, exc_info=True)


if __name__ == "__main__":
    main()