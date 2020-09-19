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
