from classes.telegram_listener import TelegramListener


def initialize(handler):
    telegram_listener = TelegramListener()

    telegram_listener.initialize()
    telegram_listener.on_message(handler)

    telegram_listener.wait_till_end()
