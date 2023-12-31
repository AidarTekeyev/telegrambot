# telegrambot
Документация телеграм бота для создания и удаления задач (to-do list):

1. Файл bot.py

Файл bot.py является основным файлом бота, который содержит основную логику и запуск бота.

1.1. Импорт необходимых модулей и классов

В начале файла происходит импорт необходимых модулей и классов, включая модуль logging, aiogram для работы с Telegram API, Controller для управления списком задач и Task для представления отдельной задачи. Также происходит настройка логирования.

1.2. Создание объектов бота и диспетчера

Создается объект bot с использованием токена вашего Telegram бота. Затем создается объект dp (диспетчера) для управления обработкой входящих сообщений.

1.3. Команды и функции-обработчики

В этой части кода определяются функции-обработчики для различных команд бота.

start_command: Обработчик команды /start. Отправляет приветственное сообщение с доступными командами.

add_command: Обработчик команды /add. Добавляет новую задачу в список задач.

done_command: Обработчик команды /done. Отмечает задачу с указанным индексом как выполненную.

list_command: Обработчик команды /list. Выводит список всех задач с их статусами.

delete_command: Обработчик команды /delete. Удаляет задачу с указанным индексом из списка.

1.4. Запуск бота

Функция run_bot запускает бота. Внутри функции используется executor.start_polling для начала обработки входящих сообщений. В случае возникновения исключения, оно будет залогировано. Функция run_bot вызывается только при запуске файла bot.py напрямую, а не при его импорте в другие файлы.

2. Файл controller.py

Файл controller.py содержит класс Controller, который отвечает за управление списком задач.

2.1. Методы класса Controller

__init__: Инициализирует объект класса Controller и создает пустой список задач.

add_task: Добавляет новую задачу в список задач.

mark_task_done: Отмечает задачу с указанным индексом как выполненную.

get_task_list: Возвращает список всех задач.

delete_task: Удаляет задачу с указанным индексом из списка.

2.2. Класс Task

Класс Task представляет отдельную задачу и содержит поля для заголовка, описания и статуса задачи.

3. Файл database.py

Файл database.py отвечает за взаимодействие с базой данных SQLite для хранения списка задач.

3.1. Функции модуля database

create_table: Создает таблицу задач в базе данных, если она не существует.

insert_task: Вставляет новую задачу в базу данных.

update_task_status: Обновляет статус задачи в базе данных.

get_all_tasks: Возвращает все задачи из базы данных.

delete_task: Удаляет задачу из базы данных по ее индексу.

4. Использование бота

4.1. Запуск бота

Для запуска бота выполните команду python bot.py в терминале. Бот будет запущен и начнет ожидать входящих сообщений от пользователей.

4.2. Команды бота

/start: Используйте эту команду для запуска бота и получения приветственного сообщения с доступными командами.

/add <задача>: Добавляет новую задачу в список задач. Замените <задача> на текст вашей задачи.

/done <индекс>: Отмечает задачу с указанным индексом как выполненную. Замените <индекс> на числовой индекс задачи в списке.

/list: Выводит список всех задач с их статусами.

/delete <индекс>: Удаляет задачу с указанным индексом из списка. Замените <индекс> на числовой индекс задачи в списке.

Важно: При использовании команд /done, /list и /delete, указывайте индекс задачи, начиная с 1.

Бот для управления списком задач готов к использованию. Пользуйтесь командами для добавления, отметки выполнения, просмотра и удаления задач, чтобы эффективно организовать свои дела.
