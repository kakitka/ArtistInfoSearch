import requests
import time
from typing import List
import telebot
from telebot import types
from telebot.callback_data import CallbackData
from bot_func_abc import AtomicBotFunctionABC

class AtomicSearchArtistBotFunction(AtomicBotFunctionABC):
    commands: List[str] = ["Text_Generate", "Genre_Generate"]
    authors: List[str] = ["IHVH"]
    about: str = "Генерация текста заданой длины!"
    description: str = """В поле  *description* поместите подробную информацию о работе функции.
    Описание способов использования, логики работы. Примеры вызова функции - /ebf 
    Возможные параметры функции `/example`  """
    state: bool = True

    bot: telebot.TeleBot
    example_keyboard_factory: CallbackData

    
    def set_handlers(self, bot: telebot.TeleBot):

        self.bot = bot

        @bot.message_handler(commands=self.commands[0])
        def SearchArtistInfo_handler(message: types.Message):
            bot.reply_to(message, "Введите количество генерируемых строк:")
            bot.register_next_step_handler(message, Handle_user_input)
            
        def Text_Generator(length_Text):
            url = "https://binaryjazz.us/wp-json/genrenator/v1/story"
            length_Text_url = f"{url}/{length_Text}/"
            response = requests.get(length_Text_url)
            Finished_Text = response.json()
            return Finished_Text
        
        def Handle_user_input(message:types.Message):
            length_Text = message.text.strip().upper()
            TextForSong = Text_Generator(length_Text)
            bot.reply_to(message, f"Сгенерированный текст: \n{TextForSong}")

        @bot.message_handler(commands=self.commands[1])
        def SearchArtistInfo_handler(message: types.Message):
            Genre_text = Genre_Generate
            bot.reply_to(message, f"Сгенерированный жанр: \n{Genre_text}")
            
        def Genre_Generate():
            url = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
            response = requests.get(url)
            Finished_Text = response.json()
            return Finished_Text
        
        
        