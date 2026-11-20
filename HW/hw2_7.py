import sqlite3

connect = sqlite3.connect('store.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
''')
connect.commit()

def create_product(name, price, quantity):
    cursor.execute(
        'INSERT INTO products(name, price, quantity) VALUES (?, ?, ?)',
        (name, price, quantity)
    )
    print('Товар создан!!')
    connect.commit()

# create_product("Laptop", 75000, 5)
# create_product("Mouse", 1200, 20)
# create_product("Keyboard", 2500, 10)

def read_products():
    cursor.execute('SELECT * FROM products')

    data = cursor.fetchall()
    for i in data:
        print(f'ID: {i[0]}, NAME: {i[1]}, PRICE: {i[2]}, QUANTITY: {i[3]}')

def update_product(row_id, price):
    cursor.execute(
        'UPDATE products SET price = ? WHERE id = ?',
        (price, row_id)
    )
    print("Цена товара обновлена")
    connect.commit()

def delete_product(row_id):
    cursor.execute(
        'DELETE FROM products WHERE id = ?',
        (row_id,)
    )
    print('Товар удален!')
    connect.commit()

# update_product(1, 80000)
# delete_product(2)
read_products()

connect.close()