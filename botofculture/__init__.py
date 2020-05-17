'''
A Discord bot named "Bot of Culture".
'''
__title__ = 'botofculture-discord'
__author__ = 'addianto'
__copyright__ = f'Copyright (c) 2020 {__author__}'
__license__ = 'MIT'
__version__ = '0.1.0'

from . import bot
import logging
import os

DEBUG = True if os.getenv('DEBUG', 'False') == 'True' else False
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

logging.basicConfig(
    datefmt='%Y-%m-%dT%H:%M:%S%z',
    format='%(asctime)s | %(levelname)s | %(name)s | %(filename)s#%(funcName)s()#L%(lineno)d | %(message)s',  # noqa
    level=logging.DEBUG if DEBUG else logging.INFO
)
logging.info(f'Debug mode: {DEBUG}')


def run():
    bot.run(DISCORD_TOKEN)