# pytest-CircleiCI

pytest-CircleCIでのCIパイプラインをつくってみる

# 前提
pytestとCirlceCI以前の前提の話。
[2020年5月におけるPython開発環境の選択肢](https://qiita.com/nicco_mirai/items/80ba4b4bf9db11ac54c6)

[pyenv](./doc/pyenv_setting.md)
pyenv自体は、Pythonのバージョン切り替え目的なので、Dockerで環境をつくるなら、無理にインストールする必要はないです。

[poetryの設定](./doc/poetry_setting.md)

[linterとformatter](./doc/linter_formatter_sertting.md)

~~[型チェッカー](./doc/static_type_checker.md)~~ 設定方法まで調べきれていないです。


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
poetry run pytest
```

少し高度ですが、例外を含めて設計、実装できていることのテストまで行うと堅牢なコードになり、バグが起こりにくくなります。
[Pythonでpytestを試してみる(pytest 例外発生テスト)](https://qiita.com/__init__/items/fde37a3f28d6b17a9ce1)
