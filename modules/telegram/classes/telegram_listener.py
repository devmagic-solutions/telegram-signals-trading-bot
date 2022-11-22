from telethon import TelegramClient, events

from models.message import Message


class TelegramListener:
    api_id = 7297500
    api_hash = '30cc3b84cb9739f69d29430e31e60569'

    def __init__(self):
        self.handlers = []
        self.telegram_client = TelegramClient('anon', self.api_id, self.api_hash)

    def initialize(self):
        print('initializing telegram listener')

        @self.telegram_client.on(events.NewMessage())
        async def new_message_event_handler(event):
            # print('new message received')

            message = Message()
            message.payload = event.raw_text
            message.publisher_id = str(event.chat_id * -1).replace('100', '')

            if len(self.handlers) > 0:
                self.handlers[0](message)

        print('starting telegram client')
        self.telegram_client.start()

    def on_message(self, handler):
        print('adding handler')

        self.handlers.append(handler)

    def wait_till_end(self):
        self.telegram_client.run_until_disconnected()
