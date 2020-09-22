""" CRUDのシンプルな処理
あくまでサンプルなので、
create()の引数ににdelte文の文字列指定しても動作するとかのツッコミはなしでお願いします。
Notes
-----
テンプレなので、割と生に近い状態で書きます。
使用用途によって、ORMを使ったり、各種フレームワークの機能を使ってください。
"""
import mysql.connector
from mysql.connector import errorcode


class CRUD:
    def __init__(self, config=None):
        # 特に指定がない場合はデフォルト値
        if (config is None):
            self.connection_config = {
                'user': 'user',
                'password': 'password',
                'host': 'mysql_container',
                'database': 'sample_db',
                'port': '3306',
            }
        else:
            self.connection_config = config

    def create(self, insert_statement):
        """普通にDBにinsertするだけするだけ
        Args:
            None
        Returns:
            insertに成功したらtrue,失敗したらfalse
        """
        insertion_succeed = False
        # mysqlへのコネクション
        conn = None
        try:
            conn = mysql.connector.connect(**self.connection_config)
            cursor = conn.cursor()
            if insert_statement == "":
                insert_statement = "INSERT INTO users (name, email) "
                + " VALUES ('LeBron', 'James@example.com')"
            cursor.execute(insert_statement)
            conn.commit()
            insertion_succeed = True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            insertion_succeed = False
        finally:
            if conn is not None:
                conn.close()
        return insertion_succeed

    def read(self, select_statement):
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

    def update(self, update_statement):
        """普通にupdateするだけ
        Args:
            update_statement
        Returns:
            updateに成功したらtrue,失敗したらfalse
        """
        update_succeed = False
        # mysqlへのコネクション
        conn = None
        try:
            conn = mysql.connector.connect(**self.connection_config)
            cursor = conn.cursor()
            cursor.execute(update_statement)
            conn.commit()
            update_succeed = True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            update_succeed = False
        finally:
            if conn is not None:
                conn.close()
        return update_succeed

    def delete(self, delete_statement):
        delete_succeed = False
        # mysqlへのコネクション
        conn = None
        try:
            conn = mysql.connector.connect(**self.connection_config)
            cursor = conn.cursor()
            cursor.execute(delete_statement)
            conn.commit()
            delete_succeed = True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            delete_succeed = False
        finally:
            if conn is not None:
                conn.close()
        return delete_succeed

    def get_member_info(self):
        """データを取ってきて加工
        普通はLow layerを担当するクラスとは別クラスにするのが
        クラスの責務の分離として正しいですが、
        サンプルなのでCRUDのメソッドとして書いています
        Args:
            None
        Returns:
            listにつめて返却
        """
        rows = self.read("select * from users limit 1")
        # 普通は、select * from users limit 1; とかを発行するけどサンプルなので、許して。
        row = rows[0]
        return "会員名:" + row[1] + "のメールアドレスは、" + row[2] + "です。"


if __name__ == "__main__":
    crud = CRUD()
    print(crud.get_member_info())

    # for row in crud.read("select * from users"):
    #     print(row)
