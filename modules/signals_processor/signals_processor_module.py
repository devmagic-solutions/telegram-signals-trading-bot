from models.signal import Signal

from constants import *

import modules.futures.futures_module as futures_module


def process_signal(signal: Signal):
    amount = _get_amount()

    if signal.side == SELL:
        futures_module.place_short_order(signal.symbol,
                                         signal.entry_price,
                                         amount,
                                         signal.leverage,
                                         signal.take_profit,
                                         signal.stop_loss)
    elif signal.side == BUY:
        futures_module.place_long_order(signal.symbol,
                                        signal.entry_price,
                                        amount,
                                        signal.leverage,
                                        signal.take_profit,
                                        signal.stop_loss)
    else:
        raise "Wrong sile"


def _get_amount():
    return 10
