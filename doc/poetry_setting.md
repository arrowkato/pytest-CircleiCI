
## Poetry

### Poetry自体のインストール
https://qiita.com/ragnar1904/items/0e5b8382757ccad9a56c
を見ながら設定

```zsh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

$HOME/.zprofileに↓が追記されている
export PATH="$HOME/.poetry/bin:$PATH"


環境変数の利用設定
```zsh
poetry config virtualenvs.in-project true
```
設定の変更確認
```zsh
poetry config --list
```
virtualenvs.in-project true になっていればOK

dev-templateという開発用directoryを作成
```zsh
poetry new dev-template
```

### すでにインストールパッケージが指定されている場合


## コマンド
[公式docの日本語訳](https://cocoatomo.github.io/poetry-ja/basic-usage/)

```zsh
cd <開発用directory>
poetry add <パッケージ名>
```
例) ``` poetry add flake8 ```

インストールパッケージの一覧表示
```zsh
poetry show
```


インストールパッケージの削除
```zsh
poetry remove <パッケージ名>
```

CLIからのpythonファイルの実行
'''zsh
poetry run python mysql_connector_sample.py
'''
単純に下記コマンドだと、デフォルトでインストールされているpythonが呼び出されるので、
poetryでインストールしたパッケージが反映されないことに注意してください。
'''zsh
python mysql_connector_sample.py
'''

# IDEにpoetryの仮想環境を認識させる
## PyCharm
[PyCharmとの連携](https://qiita.com/toto1310/items/ffb3a9ae6d1d26554932#pycharm%E3%81%A8%E3%81%AE%E9%80%A3%E6%90%BA)

PyCharm（2019.03）なら、pyproject.tomlを認識して、仮想環境を検出してくれた。 とのこと。

## VSCodeとの連携
https://qiita.com/toto1310/items/ffb3a9ae6d1d26554932#vitual-studio-code%E3%81%A8%E3%81%AE%E9%80%A3%E6%90%BA


