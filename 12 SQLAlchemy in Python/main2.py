import sqlalchemy as database

engine = database.create_engine('sqlite:///database.db')
metadata = database.MetaData()

# - CREATE: Этот запрос используется для создания новой таблицы с помощью sqlalchemy
products = database.Table(
    'products', metadata,
    database.Column('product_id', database.Integer, primary_key=True),
    database.Column('product', database.String),
    database.Column('supplier', database.String),
    database.Column('price', database.Integer)
)

metadata.create_all(engine)

# С помощью контекста with мы достигаем безопасного использования запросов в БД, 
# а так же удобного закрытия БД  без постоянного вызова commit()
with engine.begin() as transaction:

    # INSERT: Этот запрос используется для добавления новых строк в таблицу.
    product = 'Бананы'
    supplier = 'Новые Бананы'
    price = 1200

    # вставка одного значения
    new_product = {"product": product, "supplier": supplier, "price": price}

    # insertion_query = products.insert().values(new_product)
    # transaction.execute(insertion_query) # отправка SQL запроса

    new_products = [
        {"product": "Помидоры", "supplier": "ООО Томатос", "price": 20},
        {"product": "Помело", "supplier": "ИП Энигов", "price": 20},
        {"product": product, "supplier": supplier, "price": price}
    ]

    # insertion_query = products.insert().values(new_products)
    # transaction.execute(insertion_query) # отправка SQL запроса

    # SELECT: Этот запрос используется для выборки данных из таблицы.

    # посмотреть всю данные с БД
    select_all_query = products.select()
    select_all_result = transaction.execute(select_all_query)

    # fetchall() возвращает все результирующие строки в виде кортежей
    result_select_all_result = select_all_result.fetchall() 
    print(result_select_all_result)

    # Поиск продукта с именем Помело и вывод его цены
    select_price_query = products.select().where(products.columns.price == 1200)
    select_price_result = transaction.execute(select_price_query)
    print(select_price_result.fetchone()) # возвращает найденный результат
    print(select_price_result.fetchall()) # возвращает все найденные результаты

    # UPDATE: Этот запрос используется для обновления всех существующих строк в таблице
    select_item = products.update().where(products.columns.supplier == 'Новые Бананы')
    update_query = select_item.values(supplier = 'Unated Fruits')
    transaction.execute(update_query) # UPDATE не возвращает результат

    select_all_query = products.select()
    select_all_result = transaction.execute(select_all_query)
    result_select_all_result = select_all_result.fetchall() 
    print(result_select_all_result)

    # UPDATE: Этот запрос используется для обновления существующих строк в таблице по лимиту
    select_item1 = products.select().where(products.columns.supplier == 'Unated Fruits').limit(1)
    result_select_item1 = products.update().where(products.columns.product_id == select_item1.c.product_id).values(supplier='Новые Бананы')
    transaction.execute(result_select_item1)

    # DELETE: Этот запрос используется для удаления строк из таблицы
    delete_query = products.delete().where(products.columns.supplier == 'Новые Бананы')
    transaction.execute(delete_query)


