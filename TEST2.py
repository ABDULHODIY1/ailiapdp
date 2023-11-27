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
from  aiogram.types.bot_command import *
import openai

# OpenAI API key
openai.api_key = qayta_oqib_chiqarilgan_soz

# Telegram Bot Token
with open("PAPICode.codecore", "r") as machine_codex:
    machine_code_r = machine_codex.read()
TOKEN = qayta_oqib_chiqarilgan_soz2

# Telegram Bot initialization
bot = Bot(TOKEN)
dp = Dispatcher(bot)
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

# Bot commands
# BotCommand()


# Command handler for /start
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

# Message handler
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
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
