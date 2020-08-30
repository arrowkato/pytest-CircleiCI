# 目標1
VSCodeでの保存時にPythonファイルを自動整形


## 関連情報

- [2020年5月におけるPython開発環境の選択肢](https://qiita.com/nicco_mirai/items/80ba4b4bf9db11ac54c6)
- [VSCodeのPython開発環境でpylintの代わりにflake8を導入し自動整形を設定する](https://qiita.com/psychoroid/items/2c2acc06c900d2c0c8cb)
- [Blackできれいに自動整形！flake8とBlack導入と実行](https://qiita.com/tsu_0514/items/2d52c7bf79cd62d4af4a)
- [VS Code コーディング規約を快適に守る](https://qiita.com/firedfly/items/00c34018581c6cec9b84)
- [python PEP8 VSCodeでautopep8とflake8を適用する](http://trelab.info/visual-studio-code/python-vscode%E3%81%A7autopep8%E3%82%92%E9%81%A9%E7%94%A8%E3%81%99%E3%82%8B/)
- [超簡単VSCodeでPythonソースコード自動チェック・整形（venv・flake8・mypy・black利用](https://note.com/10mohi6/n/n87e7867bfb79)
- [これで決まり！最強自動コード整形ツール3選！](https://www.kimoton.com/entry/20181223/1545540702)


## linter

VSCodeを使っていると、pylint がデフォルトで推奨されるがflake8を使用する

flake8 と autopep8をインストール (実行済み)

```zsh
cd dev_template
poetry add flake8
```
VSCodeを使っていると、Linter pylint is not installed というポップアップが出てきますが、
Do not show again　を選んでおきましょう。

1. ツールバー Code -> 基本設定 → 設定[⌘,]をクリック
2. 検索欄に python.linting.flake8Enable を入力
3. Whether to lint Python file using flake8 をチェック

${PROJECT_HOME}/.vscode/settings.json ファイル内に、 ```  "python.linting.enabled": true ``` があるとOK。
-> git clone しているとすでにあるはず。

すでにpylintをインストールしていた人は、pylintを使わないように
${PROJECT_HOME}/.vscode/settings.json  に ``` "python.linting.pylintEnabled": false ``` を追加してください。


## fomatter

- [2020年5月におけるPython開発環境の選択肢](https://qiita.com/nicco_mirai/items/80ba4b4bf9db11ac54c6)
- [これで決まり！最強自動コード整形ツール3選！](https://www.kimoton.com/entry/20181223/1545540702)

選択肢は下記の3つ
- [autopep8](https://github.com/hhatto/autopep8)
- [yapf](https://github.com/google/yapf)
- [black](https://github.com/psf/black)

2020/08/26現在だと、blackが一番starが多いけど、
拡張性が高いらしいので、yapfを選択。
~~Googleが開発してるから脳死してこれで良いっしょ~~

```zsh
cd dev_template
poetry add yapf
```

.vscode/settings.jsonに保存時に自動でyapfが実行されて、オートフォーマットされるように設定済みです。

試しに、 ぐちゃぐちゃのソースの src/sample.py を開いて、保存を実行してください。
きれいに整形されたなら、正常に動作しています。

[想定しているbefore after](https://github.com/google/yapf#example)


# 目標2
Dockerfileのチェック

VSCodeで[hadolint](https://marketplace.visualstudio.com/items?itemName=exiasr.hadolint)をインストールしておいてください。

任意ですが、[hadolintの公式](https://github.com/hadolint/hadolint#install)に従って、CLIのhadolintもインストールしておくと
後々役に立つかもしれないです。

チェック条件を緩めるためには, <project_root_dir>/.hadolint.yaml を編集してください。
デフォルトでは、[DL3026](https://github.com/hadolint/hadolint/wiki/DL3026)のチェックをしないようにしています。
