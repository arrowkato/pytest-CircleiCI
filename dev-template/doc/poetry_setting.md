
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

dev-templateという開発環境を作成
```zsh
poetry new dev-template
```

### すでにインストールパッケージが指定されている場合


## コマンド

poetry install 

poetry show




