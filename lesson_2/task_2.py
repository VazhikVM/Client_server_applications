"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:

Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). В это словаре параметров обязательно должны присутствовать
юникод-символы, отсутствующие в кодировке ASCII.
Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину
отступа в 4 пробельных символа;
Необходимо также установить возможность отображения символов юникода: ensure_ascii=False;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as file_json:
        file = json.load(file_json)
    file['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})
    with open('orders.json', 'w', encoding='utf-8') as file_json:
        json.dump(file, file_json, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    write_order_to_json('Кукла', '100', '100', 'Алексеев ИВан', '2021-05-15')
