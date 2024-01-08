# from pyrogram import Client, filters

# app = Client("sosi",
#     api_id = 22230530,
#     api_hash= "472c8bac308c531696119ab0bcdd86be",
#     plugins = dict(root = "modules"))

# #@app.on_message(filters.me & filters.command("test", "."))
# #@app.on_message(filters.command("test", "."))
# @app.on_message()
# async def test(app, msg):
#     await msg.reply('Что-то умное')


# app.run()


from pyrogram import Client, filters
from pyrogram.types import Message

app = Client("my_account",
    api_id = 22230530,
    api_hash= "472c8bac308c531696119ab0bcdd86be",
    plugins = dict(root = "modules"))



#Автоответчик
@app.on_message(filters.private)
async def echo(app, message: Message):
  if message.text in ["Привет", "привет"]:  # Проверяем, содержит ли текст сообщения "Привет" или "привет"
    await app.send_message(message.chat.id, "И тебе привет!\n\nНапиши лучше на мой основной аккаунт @Dmitrii_GO")
  elif message.text in ["Что?", "Что"]:  # Проверяем, содержит ли текст сообщения "Привет" или "привет"
    await app.send_message(message.chat.id, "Капчто")
  else:
    await app.send_message(message.chat.id, "Здравствуйте, по всем вопросам пишите @Dmitrii_GO")    
  

app.run()
