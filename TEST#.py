import asyncio
import logging
import sys
from others import *
from other2 import *
from aiogram import types, Bot, Dispatcher, executor
# from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types.bot_command import BotCommand
import openai
from time import sleep
# OpenAI API key
openai.api_key = qayta_oqib_chiqarilgan_soz

# Telegram Bot Token
TOKEN = qayta_oqib_chiqarilgan_soz2

# Telegram Bot initialization
bot = Bot(TOKEN)
dp = Dispatcher(bot)

# Bot commands



# Keyboard buttons
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


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Bot haqida ma'lumot"),
        ]
    )
# Command handler for /start
@dp.message_handler(commands="start")
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom Agar siz {message.from_user.full_name} 23-211 gurux azosi bolsangiz bu Bot aynan siz uchun")

# Message handler
@dp.message_handler()
async def echo_handler(message: types.Message) -> None:
    await message.reply("Iltimos Bot hali sinov mudatida uni javobi kelishi uchun 15 soniya kuting tez orada bu muamo hal boladi")

    sleep(15)
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
    assistant_response = assistant_response.replace("GPT3", "PDPAI")
    assistant_response = assistant_response.replace("GPT3.5", "PDPAI")
    assistant_response = assistant_response.replace("Modeli", "PDPAI")
    assistant_response = assistant_response.replace("gpt3.5", "PDPAI")
    assistant_response = assistant_response.replace("gpt3", "PDPAI")
    assistant_response = assistant_response.replace("modeli", "PDPAI")
    assistant_response = assistant_response.replace("MODELI", "PDPAI")
    assistant_response = assistant_response.replace("MODEL", "PDPAI")
    assistant_response = assistant_response.replace("ChatGPT3", "PDPAI")
    assistant_response = assistant_response.replace("CHATGPT3", "PDPAI")
    assistant_response = assistant_response.replace("OpenAI", "OpenAI [lekin men ushbu botda muhiddinov abdul hodiy tomonidan yaxshiroq darajaga yetqaildim]")
    assistant_response = assistant_response.replace("openai", "openai [lekin men ushbu botda muhiddinov abdul hodiy tomonidan yaxshiroq darajaga yetqaildim]")
    # assistant_response = assistant_response.replace("", "PDPAI")
    assistant_response = assistant_response.replace("OPENAI", "openai [lekin men ushbu botda muhiddinov abdul hodiy tomonidan yaxshiroq darajaga yetqaildim]")

    assistant_response = assistant_response.replace("Salom! Sizga qanday yordam berishim mumkin?", "Salom Ozimni tanishtiray men PDP.AI man mening modelim esa (ChatGPT3.5) hisoblaqnadi bu bot yani men [Muhiddinov Abdulhodiy Tomonida Yasalganman] Hozirda men bazibir tuzatishlarga muhtojman agar men jsvob berishni kechiktirsam yoki boshq biron hatoga yol qoysam meni kechiring Men Endi rivojlanyapman va 23-211 gurux Yordamchisi sifatida yasaldim sizga raxmat! ")
    assistant_response = assistant_response.replace("Muhiddinov Abdulhodiy is not a well-known public figure, so there is limited information available about him. It is possible that he is a private individual with no significant presence or notable achievements in the public domain.", "Muhiddinov Abdulhodiy Fargona Viloyatida Tavallud Topgan u Backend Dasturchi Uning Loihalari Asosan Suni ong bilan bogliq bolib (Jumladan men ham uning loihasi man) U AI ga juda qiziqadi")
    # ... (qolgan o'zgartirishlar)

    ans = assistant_response.strip("\n").strip()

    await message.answer("Biroz kuting")
    await message.answer(f"{ans}")
    chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})

# Startup and shutdown messages
async def on_startup(dp):
    await bot.send_message(chat_id='5640990557', text='Bot Ishga tushdi!')
async def on_shutdown(dp):
    await set_default_commands(dp)
    await bot.send_message(chat_id='5640990557', text='Bot Ochib qoldi')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
