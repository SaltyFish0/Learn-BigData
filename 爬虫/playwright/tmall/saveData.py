"""
存储数据
"""
# -*- coding: utf-8 -*-
import json
import os
import re
import pymysql


def save(dirName: str, data_list: list):
    """
    存储数据
    :param dirName:目录名
    :param data_list: 数据列表
    :return: None
    """
    os.makedirs('data/' + dirName, exist_ok=True)
    for data in data_list:
        with open(f"data/{dirName}/" + re.sub('[ ?|<>\"/*{}]*', '', data['product_name']) + ".txt", 'w+',
                  encoding='utf-8') as f:
            f.write(json.dumps(data, indent=4, ensure_ascii=False))


def saveDB():
    '''
    把数据存到数据鞠中
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root',
                         password='111111', port=3306, db='tmall')
    cursor = db.cursor()
    # 清空数据库
    # cursor.execute('truncate table product')
    # cursor.execute('truncate table classify_table')
    # db.commit()

    classify_name = os.listdir('data')
    for i, v in enumerate(classify_name):
        classify_sql = f'''
                insert into classify_table (classify_name) VALUE ('{v}')
            '''
        try:
            cursor.execute(classify_sql)
            db.commit()
            product_name = os.listdir(f'data/{v}')

            for j in product_name:
                with open(f'data/{v}/{j}', 'r', encoding='utf-8') as f:
                    product_data = json.loads(f.read())
                    product = product_data['product_name']
                    price = product_data['price']
                    shop_name = product_data['shop_name']
                    product_sql = f'''
                                    insert into product (product_name, classify_id, price, shop_name) VALUE ('{product}', '{i + 1}', '{price}', '{shop_name}')
                                '''
                    try:
                        cursor.execute(product_sql)
                        db.commit()
                    except:
                        db.rollback()
                        print('发生错误, 数据库已回滚', product_sql)

        except:
            db.rollback()
            print('发生错误, 数据库已回滚', classify_sql)
    db.close()


def main():
    saveDB()


if __name__ == '__main__':
    main()
