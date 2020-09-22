# pytest-CircleiCI

pytest-CircleCIでのCIパイプラインをつくってみる

# 手っ取り早く開発を始めたい人へ

1. 予めdocker desktopをインストールしておいてください。
2. 下記のコマンドを実行してください。
```zsh
git clone https://github.com/arrowkato/pytest-CircleiCI.git
cd pytest-CircleiCI
docker-compose up -d --build
docker exec -it app /bin/bash
poetry install
```
これで、pythonファイルが置いてある app コンテナ上での開発ができる状態です。
host側の<project_root>/dev-template が container側の/code/dev-templateと
同期しているので、host or containerのどちらでもいいので、ソースを書いてください。  
実行は、コンテナ内から下記を実行してください。
```zsh
poetry run python <実行したいpythonファイル>
```

# 前提
pytestとCirlceCI以前の前提の話。
[2020年5月におけるPython開発環境の選択肢](https://qiita.com/nicco_mirai/items/80ba4b4bf9db11ac54c6)

[pyenv](./doc/pyenv_setting.md)
pyenv自体は、Pythonのバージョン切り替え目的なので、Dockerで環境をつくるなら、無理にインストールする必要はないです。

[poetryの設定](./doc/poetry_setting.md)

[linterとformatter](./doc/linter_formatter_sertting.md)

~~[型チェッカー](./doc/static_type_checker.md)~~ 設定方法まで調べきれていないです。

# testing framework
[pytest](./doc/pytest_setting.md)
MySQLと連携したテストまで。


# CircleCI
[CircleCIの設定](./doc/circleci_setting.md)


# 補足
構築者の好みとわかりやすさ重視で、プロジェクト固有の名前はあまり省略名を使っていないです。  
e.g. mysql_container

各種名前はお好みで変えてください。
