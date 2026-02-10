# CTP Strategy Template 📈

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Status](https://img.shields.io/badge/Status-Production-green)
![Market](https://img.shields.io/badge/Market-CTP%2FFutures-orange)

**Standardized CTA Strategy Interface for DeepAlpha Terminal.**

This repository defines the base classes and interfaces used by **Trading Brains Studio** for developing high-frequency strategies on the Shanghai Futures Exchange (SHFE) and other Chinese markets.

## Architecture

- **Event Driven**: Based on tick-level data updates.
- **Low Latency**: Optimized for CTP (Comprehensive Transaction Platform) API.
- **Risk Control**: Built-in pre-trade risk checks in the `buy`/`sell` methods.

## Example Usage

```python
from strategy_base import CtaTemplate, TickData

class DualThrustStrategy(CtaTemplate):
    author = "Roy Dai"
    
    def on_init(self):
        self.write_log("Strategy Initialized")
        
    def on_tick(self, tick: TickData):
        if tick.last_price > self.upper_rail:
            self.buy(tick.last_price, 1)


Copyright © 2026 Trading Brains Studio. All rights reserved.
Internal use only.
