from dataclasses import dataclass
from typing import Optional


@dataclass
class Item:
    id: int
    name: str
    high_alch: Optional[int]
    ge_high: Optional[int]
    ge_low: Optional[int]

    @property
    def alch_profit(self) -> Optional[int]:
        """Beräknar vinst marginalen om vi bortser från Nature rune-kostnaden."""
        if self.high_alch is not None and self.ge_low is not None:
            return self.high_alch - self.ge_low
        return None