""" CRUDのシンプルな処理

Notes
-----
テンプレなので、割と生に近い状態で書きます。
使用用途によって、ORMを使ったり、各種フレームワークの機能を使ってください。
"""
import mysql.connector
from mysql.connector import errorcode

class CRUD:
    def __init__(self,config=None):
        # 特に指定がない場合はデフォルト値
        if(config is None):
            self.connection_config = {
                'user': 'user',
                'password': 'password',
                'host': 'mysql_container',
                'database': 'sample_db',
                'port': '3306',
            }
        else:
            self.connection_config = config

    def read(self):
        """普通にDBからselectするだけ
        Args:
            None
        Returns:
            listにつめて返却
        """
        # mysqlへのコネクション
        conn = None
        # データの取得結果
        rows = []
        try:
            conn = mysql.connector.connect(**self.connection_config)
            cursor = conn.cursor()
            cursor.execute('select * from users')
            for row in cursor.fetchall():
                # rowはtuple
                rows.append(row)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        finally:
            if conn is not None:
                conn.close()
        return rows

    def show_member_info(self):
        """データを取ってきて加工
        普通はLow layerを担当するクラスとは別クラスにするのがクラスの責務の分離として正しいが、
        サンプルなのでCRUDのメソッドとして書いています
        Args:
            None
        Returns:
            listにつめて返却
        """
        rows = self.read()
        row = rows[0]
        return "会員番号" + str(row[0]) + "番の人は、"+ row[1] + "で、メールアドレスは、" + row[2] + "です。"


if __name__ == "__main__":
    crud = CRUD()
    print(crud.show_member_info())

