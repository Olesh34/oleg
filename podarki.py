import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('gifts.db')
cursor = conn.cursor()

# Создаем таблицу
cursor.execute('''
CREATE TABLE IF NOT EXISTS gifts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    gift_name TEXT NOT NULL,
    price REAL NOT NULL,
    status TEXT NOT NULL
)
''')

# Вставляем данные
gifts_data = [
    ('Иванов Иван Иванович', 'Книга', 500.00, 'Куплен'),
    ('Петрова Мария Сергеевна', 'Конфеты', 300.00, 'Не куплен'),
    ('Сидоров Александр Викторович', 'Настольная игра', 1200.00, 'Куплен'),
    ('Кузнецова Анна Владимировна', 'Косметика', 1500.00, 'Не куплен'),
    ('Семенов Сергей Алексеевич', 'Часы', 2500.00, 'Куплен'),
    ('Федорова Ольга Игоревна', 'Сумка', 2000.00, 'Не куплен'),
    ('Дмитриев Николай Петрович', 'Флешка', 1000.00, 'Куплен'),
    ('Егорова Наталья Павловна', 'Плед', 800.00, 'Не куплен'),
    ('Романов Евгений Александрович', 'Спорт. инвентарь', 4500.00, 'Куплен'),
    ('Светлова Маргарита Владимировна', 'Билеты на концерт', 3000.00, 'Не куплен')
]

# Вставляем данные в таблицу
cursor.executemany('INSERT INTO gifts (full_name, gift_name, price, status) VALUES (?, ?, ?, ?)', gifts_data)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()