import logging
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token='YOUR_BOT_TOKEN')
dp = Dispatcher(bot, storage=MemoryStorage())

# Подключение к базе данных SQLite
db = sqlite3.connect('YOUR_DATABASE_FILE.db')
cursor = db.cursor()

# Создание таблицы задач, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT NOT NULL
    )
''')
db.commit()

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Отправка приветственного сообщения и списка доступных команд
    await message.reply('Привет! Я бот для управления списком задач. Доступные команды:\n'
                        '/add <задача> - добавить новую задачу\n'
                        '/done <индекс> - отметить задачу как выполненную\n'
                        '/list - показать список задач\n'
                        '/delete <индекс> - удалить задачу')

# Обработчик команды /add
@dp.message_handler(commands=['add'])
async def add_command(message: types.Message):
    # Извлечение текста задачи из сообщения пользователя
    task_text = message.text.replace('/add', '').strip()
    if task_text:
        # Добавление новой задачи в базу данных
        cursor.execute('INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)', (task_text, '', 'не выполнена'))
        db.commit()
        await message.reply(f'Задача "{task_text}" добавлена')
    else:
        await message.reply('Пожалуйста, укажите текст задачи')

# Обработчик команды /done
@dp.message_handler(commands=['done'])
async def done_command(message: types.Message):
    # Извлечение индекса задачи из сообщения пользователя
    task_index = message.text.replace('/done', '').strip()
    if task_index.isdigit():
        # Получение списка задач из базы данных
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        if 0 < int(task_index) <= len(tasks):
            task_id = tasks[int(task_index) - 1][0]
            # Обновление статуса задачи на "выполнена"
            cursor.execute('UPDATE tasks SET status=? WHERE id=?', ('выполнена', task_id))
            db.commit()
            await message.reply('Задача успешно выполнена!')
        else:
            await message.reply('Некорректный индекс задачи')
    else:
        await message.reply('Пожалуйста, укажите индекс задачи')

# Обработчик команды /list
@dp.message_handler(commands=['list'])
async def list_command(message: types.Message):
    # Получение списка задач из базы данных
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    if tasks:
        # Форматирование списка задач в текстовый вид
        task_list_text = '\n'.join(f'{i+1}. {task[1]} ({task[3]})' for i, task in enumerate(tasks))
        await message.reply(f'Список задач:\n{task_list_text}')
    else:
        await message.reply('Список задач пуст')

# Обработчик команды /delete
@dp.message_handler(commands=['delete'])
async def delete_command(message: types.Message):
    # Извлечение индекса задачи из сообщения пользователя
    task_index = message.text.replace('/delete', '').strip()
    if task_index.isdigit():
        # Получение списка задач из базы данных
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        if 0 < int(task_index) <= len(tasks):
            task_id = tasks[int(task_index) - 1][0]
            # Удаление задачи из базы данных
            cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
            db.commit()

if __name__ == '__main__':
    import asyncio

    # Запуск бота
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(dp.start_polling())
    except Exception as e:
        logging.exception('Ошибка во время работы бота:')
    finally:
        loop.close()
