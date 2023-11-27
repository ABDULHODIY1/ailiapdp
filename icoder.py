import asyncio
import logging
import sys
from others import *
from other2 import *
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import BotCommand

import openai

# Bot token can be obtained via https://t.me/BotFather

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
# Telegram Bot Token
with open("PAPICode.codecore", "r") as machine_codex:
    machine_code_r = machine_codex.read()
TOKEN = qayta_oqib_chiqarilgan_soz2

buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Sen kimsan?'),
            KeyboardButton(text='Vazifang nima?'),
            KeyboardButton(text='Seni Kim Yasagan?'),
            KeyboardButton(text='Muhiddinov Abdulhodiy Kim?'),
            KeyboardButton(text='PDP Qanqa Univesitet?'),
        ]
    ], resize_keyboard=True
)

@dp.message()
async def echo_handler(message: types.Message) -> None:
    chat_log = []

    user_message = message.text
    chat_log.append({"role": "user", "content": user_message})

    # OpenAI Chat Completion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log
    )

    assistant_response = response['choices'][0]['message']['content']

    assistant_response = assistant_response.replace("GPT3", "PDPAI")
    assistant_response = assistant_response.replace("GPT3.5", "PDPAI")
    # ... (qolgan o'zgartirishlar)

    ans = assistant_response.strip("\n").strip()
    await message.answer(f"{ans}")
    chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})



async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    # async def set_commands(da):
    #     await BotCommand(command="start", description="Botni ishga tushurish"),
    #     await BotCommand(command="help", description="Bot haqida yordam olish"),
        # await set_commands(dp)
    await dp.start_polling(bot)
# @dp.message(CommandStart())



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())