import aiogram.types
import dispatcher
from YouTube_download import YT_download_video
from VK_download import VK_download_video
import time
from config import YOUTUBE_PATH, VK_PATH
from os import remove
import re


@dispatcher.dp.message_handler(commands=['start', 'help'])
async def start_command(message: aiogram.types.Message) -> None:
    await message.answer('Привет, отправь мне ссылку на видео из YouTube, и я пришлю тебе скачанное видео')



@dispatcher.dp.message_handler()
async def start_command(message: aiogram.types.Message) -> None:
    if re.match(r"http(s)?:\/\/(www.)?youtube\.com\/", message.text):
        ytfilename = f'{message.from_user.id}_{time.time()}.mp4'
        msg = await message.bot.send_message(message.chat.id, 'Ваше видео загружается. Подождите немного...')
        status = YT_download_video(message.text, ytfilename)
        if status == 0:
            return await msg.edit_text('Ссылка недействительна')
        elif status == -1:
            return await msg.edit_text('Файл очень большой')
        
        await message.bot.send_video(message.chat.id, open(YOUTUBE_PATH / ytfilename, 'rb'))
        await msg.delete()
        remove(YOUTUBE_PATH / ytfilename)

    elif re.match(r"http(s)?:\/\/(www.)?vk\.com\/", message.text):
        vkfilename = f'{message.from_user.id}_{time.time()}.mp4'
        msg = await message.bot.send_message(message.chat.id, 'Ваше видео загружается. Подождите немного...')
        status = VK_download_video(message.text, vkfilename)

        if status == 0:
            return await msg.edit_text('Ссылка недействительна')
        
        await message.bot.send_video(message.chat.id, open(VK_PATH / vkfilename, 'rb'))
        await msg.delete()
        remove(VK_PATH / vkfilename)

    else:
        await message.answer('Ссылка некорректна')


