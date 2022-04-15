import logging
from aiogram import executor
from create_bot import dp
from derectory import bot_def

logging.basicConfig(level=logging.INFO)

bot_def.register_hendlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

