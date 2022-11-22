from models.message import Message
from models.signal import Signal

import services.message_parser as message_parser


def parse_message(message: Message) -> Signal:
    return message_parser.parse_message(message)

