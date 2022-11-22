from models.message import Message

import modules.telegram.telegram_module as telegram_module
import modules.parser.parser_module as parser_module
import modules.signals_processor.signals_processor_module as signals_processor_module


def run_bot():
    print('starting bot')
    telegram_module.initialize(__on_message)


def __on_message(message: Message):
    signal = parser_module.parse_message(message)
    if not signal:
        return

    signals_processor_module.process_signal(signal)
