
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


