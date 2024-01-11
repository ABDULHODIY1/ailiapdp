# from aiogram import Bot,Dispatcher,types
# from openai import OpenAI
# from others import *
# import logging
# import asyncio
# with open("PAPICode.codecore","r")as code:
#     machine_codes = code.read()
#
# API_TOKEN=qayta_oqib_chiqarilgan_soz # TELEGRAM BOT TOKEN
# # OPEN_AI_API_KEY="YOUR_API_KEY"
# b=Bot(API_TOKEN)
# dp=Dispatcher(b)
# async def main() -> None:
# # Initialize Bot instance with a default parse mode which will be passed to all API␣
#
# bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
# # And the run events dispatching
# await dp.start_polling(bot)
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())
#
# # client = OpenAI(
# #     api_key=OPEN_AI_API_KEY,
# # )
# # bot=Bot(token=API_TOKEN)
# # dp=Dispatcher(OPEN_AI_API_KEY)
# # while True:
# #     requests = input("Message For GPT Asistsnt")
# #     chat_completion = client.chat.completions.create(
# #         model="gpt-3.5-turbo",
# #        messages=[{"role": "user", "content": f"{requests}"}]
# #     )
# #     message = chat_completion.choices[0].message
# #     print(message)
# # #
# #
# # client = OpenAI(
# #     api_key="YOURAPI",
# # )
# #
# #
# # while True:
# #     requests = input("Message For GPT Asistsnt")
# #     chat_completion = client.chat.completions.create(
# #         model="gpt-3.5-turbo",
# #        messages=[{"role": "user", "content": f"{requests}"}]
# #     )
# #     message = chat_completion.choices[0].message
# #     print(message)
