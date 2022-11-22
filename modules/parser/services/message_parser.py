import re

from models.message import Message
from models.signal import Signal
from modules.parser.parsers.parsers_aggregator import ParsersAggregator

parser_aggregator = ParsersAggregator()


def parse_message(message: Message) -> Signal:
    parser = parser_aggregator.get_parser(message.publisher_id)
    if not parser:
        return False

    signal = __parse_content(message.payload, parser)
    return signal


def __parse_content(content, parser):
    signal = Signal()

    matches = re.search(parser['parser_regex'], content)

    signal.symbol = matches.group('symbol')
    signal.side = matches.group('side')
    signal.entry_price = matches.group('entry_price')
    signal.take_profit = matches.group('take_profit_price')
    signal.stop_loss = matches.group('stop_loss_price')
    signal.leverage = matches.group('leverage')

    return 0

