from aiogram import Dispatcher,types
import datetime
import main as m


async def date(message: types.Message):
    parsed_message = message.text[6:].split(',')
    if len(parsed_message) == 3:
        date = datetime.datetime(int(parsed_message[0]), int(parsed_message[1]), int(parsed_message[2]))
        datebase = date.ctime()
        dateday = m.selectday(datebase[:3])
        datedays = dateday[0][1]
        await message.reply(datedays)
    else:
        await message.reply("Некоректное сообщение.")

def register_hendlers(dp:Dispatcher):
    dp.register_message_handler(date,lambda message: message.text.startswith("/date "))