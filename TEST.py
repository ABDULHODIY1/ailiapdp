import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import BotCommand
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from others import *
from other2 import *
import openai

# Bot token can be obtained via https://t.me/BotFather
with open("PAPICode.codecore","r") as machine_codex:
    machine_code_r = machine_codex.read()
TOKEN = qayta_oqib_chiqarilgan_soz2

# All handlers should be attached to the Router (or Dispatcher)
bot= Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)
buttons=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Sen kimsan?'),
            KeyboardButton(text='Vazifang nima?'),
            KeyboardButton(text='Seni Kim Yasagan?'),
            KeyboardButton(text='Muhiddinov Abdulhodiy Kim?'),
            KeyboardButton(text='PDP Qanqa Univesitet?'),
        ]
    ],resize_keyboard=True
)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    openai.api_key = qayta_oqib_chiqarilgan_soz

    chat_log = []

    user_message = message.text
    chat_log.append({"role": "user", "content": user_message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log
    )
    assistant_response = response['choices'][0]['message']['content']

    # Additional replacements
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
    ans = assistant_response.strip("\n").strip()
    await message.answer(f"{ans}")
    chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "botni ishga tushuriish"),
        types.BotCommand("help", "bot haqida malumot"),
    ])

async def main() -> None:
    # await dp.start_polling(bot)
    await set_default_commands(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
