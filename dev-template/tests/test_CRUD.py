"""理想的な状態
あくまでMySQL+pytestの初期導入のサンプルとして書いています。
DBの接続をメソッドごとに行う場合は少ないので、下記のように前処理、後処理を書くほうがいいです。
https://dev.classmethod.jp/articles/pytest-getting-started/
なおかつ、pytestのテストスイートを実行する前のテーブルの状態は毎回同じになるのが望ましいです。
この場合だと、usersテーブルをDROP -> CREATE -> 初期レコードをINSERTしたほうがいいです。
"""
from src import CRUD as my_crud
import pytest


def test_read():
    crud = my_crud.CRUD()
    rows = crud.read('select * from users')
    # sample_db.user テーブルには (1, "TOM", "xxxx@mail.co.jp") のみが入っているはず
    row = rows[0]
    # auto increment されているid はアプリから制御できるものではないので、チェックからは外す。
    # assert row[0] == 1
    assert row[1] == "TOM"
    assert row[2] == "xxxx@mail.co.jp"


def test_get_member_info():
    crud = my_crud.CRUD()
    member_info = crud.get_member_info()
    assert member_info == "会員名:TOMのメールアドレスは、xxxx@mail.co.jpです。"


def test_create():
    """insert文の発行テスト
    insertされて、行数が増えていればOKという判定基準にします。
    """
    crud = my_crud.CRUD()
    # insertする前
    before_list = crud.read('select * from users')
    # テストしたいメソッド
    crud.create("INSERT INTO users (name, email) " +
                " VALUES ('LeBron', 'James@example.com')")
    # insertした後
    after_list = crud.read('select * from users')
    # insertが成功しているならば、挿入前から1レコード増えているはず。
    assert (len(before_list) + 1) == len(after_list)


def test_update():
    crud = my_crud.CRUD()
    # テストしたいメソッド
    crud.update("UPDATE users " + " SET email = 'Tom@example.com' " +
                " WHERE name = 'TOM' ")
    # update後
    member_info = crud.get_member_info()
    assert (member_info == "会員名:TOMのメールアドレスは、Tom@example.comです。")
    # もとに戻しておく
    crud.update("UPDATE users " + " SET email = 'xxxx@mail.co.jp' " +
                " WHERE name = 'TOM' ")


def test_delete():
    """DELETE文の発行テスト
    DELETEされて、行数が減っていればOKという判定基準にします。
    """
    crud = my_crud.CRUD()
    # deleteする前
    before_list = crud.read('select * from users')
    # テストしたいメソッド create で増やしているはずのレコード
    crud.delete("DELETE FROM users WHERE email = 'James@example.com'")
    # deleteした後
    after_list = crud.read('select * from users')
    # DELETEが成功しているならば、挿入前から1レコード増えているはず。
    assert (len(before_list) > len(after_list))
