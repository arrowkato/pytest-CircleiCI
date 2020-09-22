# Testing Framework
[PythonのTesting frameworkはいくつかあります](https://www.softwaretestinghelp.com/python-testing-frameworks/)。
[pytest](https://docs.pytest.org/en/stable/)を使います。

testコードは、<pj_root_dir>/test に配置してください。
テストコードを書くファイルは、test_<テストしたいファイル> にするのが一般的です。

e.g
- テスト対象のファイル: src/four_basic_arithmetic_operations.py
- テストコードのファイル: tests/tests_four_basic_arithmetic_operations.py

テストの実行方法
```zsh
cd dev-template
poetry run pytest
```

少し高度ですが、例外を含めて設計、実装できていることのテストまで行うと堅牢なコードになり、バグが起こりにくくなります。
[Pythonでpytestを試してみる(pytest 例外発生テスト)](https://qiita.com/__init__/items/fde37a3f28d6b17a9ce1)

# 以下メモ

## 使用しているライブラリがwarningを出している場合を出している場合に無視する
pytestの公式document [Warnings Capture](https://docs.pytest.org/en/latest/warnings.html) より

特に、[DeprecationWarning and PendingDeprecationWarning]( https://docs.pytest.org/en/latest/warnings.html#deprecationwarning-and-pendingdeprecationwarning) の章が対象。

### 事象
pytestを実行すると↓がでる。
```
========================== warnings summary =====================================
tests/test_CRUD.py::test_read
tests/test_CRUD.py::test_read
  /root/.cache/pypoetry/virtualenvs/dev-template-KUBuAAr9-py3.8/lib/python3.8/site-packages/mysql/connector/connection_cext.py:487: DeprecationWarning: PY_SSIZE_T_CLEAN will be required for '#' formats
    self._cmysql.query(query,

-- Docs: https://docs.pytest.org/en/latest/warnings.html

===========================6 passed, 2 warnings in 0.33s ===========================
```
<前略>/mysql/connector/connection_cext.py:487
なので、mysqlのライブラリの警告なので、修正対象にはしたくない。

### 解決策
pytest.ini or pyproject.tomlに無視するwarningを書く。

どちらでもいいので、直感的にわかりやすい名前のpytest.iniを作る。

pytest.iniファイル


```toml
<前略>
filterwarnings = ignore: .*PY_SSIZE_T_CLEAN.*self._cmysql.query.*:DeprecationWarning
<後略>
```
対象となるwarning messageが下記なので、
```plaintext
DeprecationWarning: PY_SSIZE_T_CLEAN will be required for '#' formats
    self._cmysql.query(query,
```
```PY_SSIZE_T_CLEAN will be required for``` を正規表現でマッチさせたいので、
```.*PY_SSIZE_T_CLEAN will be required for.*``` を
```ignore:``` と ```:DeprecationWarning```の間に記載した。

