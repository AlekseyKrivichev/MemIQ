import random
from pathlib import Path
from aiogram.types import FSInputFile

token = "" # токен бота

menu_text = "Проект @Noir_Codex"
photo = FSInputFile("/Users/alex/Desktop/Memiq/logo.png") # путь до приветственной картинки

btn1_name = "Мем" # название кнопки 1

images_folder = "/Users/alex/Desktop/Memiq/memes" # путь до папки с мемами

# Загружаем список картинок один раз при старте
def load_images_list():
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
    images_path = Path(images_folder)
    return [str(img) for img in images_path.glob('*') if img.suffix.lower() in image_extensions]

images_list = load_images_list()

def get_random_image():
    return random.choice(images_list)


btn2_name = "Цитата" # название кнопки 2
with open("quotes.txt", mode="r", encoding="utf-8") as r_file: # открытие .txt файла и считывание строк
    file_text2 = r_file.readlines()


btn3_name = "Факт" # название кнопки 3
with open("facts.txt", mode="r", encoding="utf-8") as r_file: # открытие .txt файла и считывание строк
    file_text3 = r_file.readlines()
