# 概要
pythonが入った app コンテナからアクセスできるmysqlが入ったコンテナについてです。

REAME.mdにも似たようなことを書きましたが、
下記のコマンドを実行するとport番号3306で動きます。
```
docker-compose up -d --build
```
もしホスト側で別のMySQLを動かしている場合は、MySQL on Dockerの起動に
失敗する可能性があるので、停止させておいてください。

# 設定
設定については、mysqlフォルダ配下とdocker-compose.ymlに書いてあることが全てです。

アプリを書く人は、``` <project_root>/mysql/docker/mysql/initdb.d ```
配下にある schema.sqlとtestdata.sqlにテスト用の初期データを
登録してする必要があると覚えてください。

# 参考文献
- [CircleCI実践入門のリポジトリ](https://github.com/circleci-book/python-sample)
- [docker-composeでMySQL5.7を起動して接続してみた](https://qiita.com/Manabu-man/items/58d0f98a15656ed65136)
- [DockerのMySQLコンテナに外部からアクセスする方法まとめ改](https://qiita.com/saken649/items/00e752d89f2a6c5a82f6)
