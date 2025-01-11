"""gfdfgdfg"""
from typing import List
import requests
import telebot
from telebot import types
from telebot.callback_data import CallbackData
from bot_func_abc import AtomicBotFunctionABC

class AtomicSearchArtistBotFunction(AtomicBotFunctionABC):
    """docstring"""
    commands: List[str] = ["Text_Generate", "genre_generate"]
    authors: List[str] = ["IHVH"]
    about: str = "Генерация текста заданой длины!"
    description: str = """В поле  *description* поместите подробную информацию о работе функции.
    Описание способов использования, логики работы. Примеры вызова функции - /ebf 
    Возможные параметры функции `/example`  """
    state: bool = True
    example_keyboard_factory: CallbackData
    bot: telebot.TeleBot

    def set_handlers(self, bot: telebot.TeleBot):

        self.bot = bot

        @bot.message_handler(commands=self.commands[0])
        def search_artist_info_handler(message: types.Message):
            bot.reply_to(message, "Введите количество генерируемых строк:")
            bot.register_next_step_handler(message, handle_user_input)

        def text_generator(length_text):
            url = "https://binaryjazz.us/wp-json/genrenator/v1/story"
            length_text_url = f"{url}/{length_text}/"
            response = requests.get(length_text_url, timeout=5)
            finished_text = response.json()
            return finished_text

        def handle_user_input(message:types.Message):
            length_text = message.text.strip().upper()
            text_for_song = text_generator(length_text)
            bot.reply_to(message, f"Сгенерированный текст: \n{text_for_song}")

        @bot.message_handler(commands=self.commands[1])
        def generate_genre(message: types.Message):
            genre_text = genre_generate
            bot.reply_to(message, f"Сгенерированный жанр: \n{genre_text}")

        def genre_generate():
            url = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
            response = requests.get(url, timeout=5)
            finished_text = response.json()
            return finished_text
