# srcディレクトリとは別にtestsフォルダを作成して、
# そのフォルダ内にテストコードを書くというディレクトリ構造が基本です。

# そのために、srcフォルダにあるファイルをimportします。
from src import four_basic_arithmetic_operations
import pytest


# 以下、テストコードの本体
# 正常系
def test_add():
    assert four_basic_arithmetic_operations.add(2, 3) == 5


# 正常系
def test_subtract():
    assert four_basic_arithmetic_operations.subtract(2, 3) == -1


# 正常系
def test_multiply():
    assert four_basic_arithmetic_operations.multiply(2, 3) == 6


# 正常系
def test_divide():
    assert four_basic_arithmetic_operations.divide(6, 3) == 2


# 異常系
# 例外(ZeroDivisionError)が起こることが正しい場合の書き方
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        four_basic_arithmetic_operations.divide(6, 0)
