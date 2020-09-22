"""理想的な状態
DBの接続をメソッドごとに行う場合は少ないので、下記のように前処理、後処理を書くほうがいいです。
https://dev.classmethod.jp/articles/pytest-getting-started/
"""
from src import CRUD as my_crud
import pytest


def test_read():
    crud = my_crud.CRUD()
    rows = crud.read()
    # sample_db.user テーブルには (1, "TOM", "xxxx@mail.co.jp") のみが入っているはず
    row = rows[0]
    assert row[0] == 1
    assert row[1] == "TOM"
    assert row[2] == "xxxx@mail.co.jp"

def test_show_member_info():
    crud = my_crud.CRUD()
    member_info = crud.show_member_info()
    assert member_info == "会員番号1番の人は、TOMで、メールアドレスは、xxxx@mail.co.jpです。"
