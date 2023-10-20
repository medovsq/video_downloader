import aiogram
import config
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialise bot & dispatcher
bot = aiogram.Bot(token=config.TOKEN, parse_mode='HTML')
dp = aiogram.Dispatcher(bot)
