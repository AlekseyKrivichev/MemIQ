# MemIQ

Telegram bot MemIQ — отправка мемов, цитат и фактов | Telegram bot MemIQ — sending memes, quotes, and facts

<img src="logo.png" alt="Memiq Logo" width="300" height="300"/>

---

## Описание / Description

| Русский | English |
|---------|---------|
| **MemIQ** — лёгкий и весёлый Telegram-бот. По нажатию кнопки он отправляет: | **MemIQ** is a lightweight, fun Telegram bot. On button click it sends: |
| - Случайный мем из папки `memes/` | - A random meme from `memes/` folder |
| - Цитату из файла `quotes.txt` | - A quote from `quotes.txt` |
| - Факт из файла `facts.txt` | - A fact from `facts.txt` |

---

## Автор / Author

| Русский | English |
|---------|---------|
| **Автор проекта:** @Noir_Codex | **Project author:** @Noir_Codex |
| GitHub: [@Noir_Codex](https://github.com/Noir-Codex) | GitHub: [@Noir_Codex](https://github.com/Noir-Codex) |
| Telegram: [@Noir_Codex](https://t.me/Noir_Codex) | Telegram: [@Noir_Codex](https://t.me/Noir_Codex) |

> Хочешь свой бот? Пиши! | Want your own bot? Contact me!

---

## Функционал / Features

| Кнопка / Button | Действие / Action |
|-----------------|-----------------|
| Мем / Meme      | Отправляет случайное изображение из `memes/` / Sends a random image from `memes/` |
| Цитата / Quote  | Отправляет случайную цитату из `quotes.txt` / Sends a random quote from `quotes.txt` |
| Факт / Fact     | Отправляет случайный факт из `facts.txt` / Sends a random fact from `facts.txt` |

> После действия кнопки остаются, можно нажимать снова! / Buttons remain after action, you can press again!

---

## Установка и запуск / Installation & Run

| Шаг / Step | Русский | English |
|------------|---------|---------|
| 1 | Клонируем репозиторий | Clone the repository |
|   | `git clone https://github.com/Noir-Codex/Memiq.git` | `git clone https://github.com/Noir-Codex/Memiq.git` |
|   | `cd Memiq` | `cd Memiq` |
| 2 | Создаём виртуальное окружение | Create a virtual environment |
|   | `python -m venv venv` | `python -m venv venv` |
|   | `source venv/bin/activate # Linux / macOS` | `source venv/bin/activate # Linux / macOS` |
|   | `venv\Scripts\activate # Windows` | `venv\Scripts\activate # Windows` |
| 3 | Устанавливаем зависимости | Install dependencies |
|   | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| 4 | Настройка конфигурации | Configure |
|   | В `config.py` вставьте токен и пути к файлам | In `config.py`, set your token and file paths |
| 5 | Подготовка контента | Prepare content |
|   | `quotes.txt` — по одной цитате на строку | `quotes.txt` — one quote per line |
|   | `facts.txt` — по одному факту на строку | `facts.txt` — one fact per line |
|   | Папка `memes/` — любые изображения | `memes/` folder — any images |
| 6 | Запуск бота | Run bot |
|   | `python memiq.py` | `python memiq.py` |

---

## Особенности / Features

| Русский | English |
|---------|---------|
| Защита от дублирования команды `/start` (не чаще 1 раза в секунду) | Prevent duplicate `/start` command |
| Авто-загрузка мемов при старте | Auto-load memes at startup |
| Поддержка всех популярных форматов изображений | Supports all popular image formats |
| Чистый, документированный код | Clean, well-documented code |
| Легкая кастомизация | Easy customization |

---

> Создано с любовью к Telegram / Made with love for Telegram  
> С уважением, @Noir_Codex / Best regards, @Noir_Codex
