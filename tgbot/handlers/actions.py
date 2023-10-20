import aiogram.types
import dispatcher
from YouTube_download import download_video
import time
from config import YOUTUBE_PATH
from os import remove
import re


@dispatcher.dp.message_handler(commands=['start', 'help'])
async def start_command(message: aiogram.types.Message) -> None:
    await message.answer('Привет, отправь мне ссылку на видео из YouTube, и я пришлю тебе скачанное видео')



@dispatcher.dp.message_handler()
async def start_command(message: aiogram.types.Message) -> None:
    if re.match(r"http(s)?:\/\/(www.)?youtube\.com\/", message.text):
        filename = f'{message.from_user.id}_{time.time()}.mp4'
        msg = await message.bot.send_message(message.chat.id, 'Ваше видео загружается. Подождите немного...')
        status = download_video(message.text, filename)
        if status == 0:
            return await msg.edit_text('Ссылка недействительна')
        elif status == -1:
            return await msg.edit_text('Файл очень большой')
        
        await message.bot.send_video(message.chat.id, open(YOUTUBE_PATH / filename, 'rb'))
        await msg.delete()
        remove(YOUTUBE_PATH / filename)
    else:
        await message.answer('Ссылка некорректна')


