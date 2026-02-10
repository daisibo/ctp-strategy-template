from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class TickData:
    symbol: str
    last_price: float
    volume: int
    open_interest: int
    datetime: datetime

@dataclass
class OrderData:
    symbol: str
    order_id: str
    direction: str
    offset: str
    price: float
    volume: int
    status: str

class CtaTemplate(ABC):
    """
    Base class for CTA (Commodity Trading Advisor) strategies.
    Designed for Trading Brains Studio internal execution engine.
    """
    
    author: str = "Trading Brains Studio"
    
    def __init__(self, cta_engine: Any, strategy_name: str, setting: Dict):
        self.cta_engine = cta_engine
        self.strategy_name = strategy_name
        self.setting = setting
        self.trading = False
        self.pos = 0  # Current position

    @abstractmethod
    def on_init(self):
        """Callback when strategy is initialized."""
        pass

    @abstractmethod
    def on_start(self):
        """Callback when strategy is started."""
        pass

    @abstractmethod
    def on_stop(self):
        """Callback when strategy is stopped."""
        pass

    @abstractmethod
    def on_tick(self, tick: TickData):
        """Callback for new tick data."""
        pass

    @abstractmethod
    def on_bar(self, bar: Any):
        """Callback for new K-line bar data."""
        pass

    def buy(self, price: float, volume: int, stop: bool = False):
        """Send buy order (Open Long)."""
        return self.cta_engine.send_order(self, "BUY", "OPEN", price, volume, stop)

    def sell(self, price: float, volume: int, stop: bool = False):
        """Send sell order (Close Long)."""
        return self.cta_engine.send_order(self, "SELL", "CLOSE", price, volume, stop)

    def short(self, price: float, volume: int, stop: bool = False):
        """Send short order (Open Short)."""
        return self.cta_engine.send_order(self, "SELL", "OPEN", price, volume, stop)

    def cover(self, price: float, volume: int, stop: bool = False):
        """Send cover order (Close Short)."""
        return self.cta_engine.send_order(self, "BUY", "CLOSE", price, volume, stop)

    def write_log(self, msg: str):
        """Write log message."""
        print(f"[{datetime.now()}] {self.strategy_name}: {msg}")
