# 概要
型チェッカーを入れるとインテリセンス(入力補完)が効きやすくなって便利。

https://speakerdeck.com/tenajima/vs-codetopyrightdeshi-meruxing-falsearusheng-huo

# 比較検討
[2020年5月におけるPython開発環境の選択肢](https://qiita.com/nicco_mirai/items/80ba4b4bf9db11ac54c6#5-%E5%9E%8B%E3%83%81%E3%82%A7%E3%83%83%E3%82%AB%E3%83%BC) 
より

- エディタにVS CodeかVimを使うならPyright
- 使わないならmypy
- mypyの遅さに耐えられなかったらPyre

VSCodeなので、 [Pyright](https://github.com/microsoft/pyright) に決定

2020/07以降は、Pyrightと同じくMS製のプラグインの[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) も出ています。
ちなみに、Pylanceは現状Preview版。好きな人はどうぞ。

# インストール方法

## VSCodeの場合
最新公開バージョンのPyright VS Code拡張機能は、VS Codeから直接インストールできます。
拡張機能パネルを開いて"pyright"を検索するだけです。


## VimおよびNeovimの場合
生粋のVimmerおよびNeovim使いは [coc-pyright](https://github.com/fannheyward/coc-pyright/)をインストールしてください。


## Emacsの場合
emacsユーザーの場合、[lsp-pyright](https://github.com/emacs-lsp/lsp-pyright) を含む
[lsp-mode](https://github.com/emacs-lsp/lsp-mode)をインストールできます。
pyright拡張機能をアクティブにするには、[ドキュメント](https://emacs-lsp.github.io/lsp-pyright/)の
指示に従ってください。

# 使い方 

重厚な解説
[入力補完を充実させ、より堅牢なPythonコードのための型アノテーションとPyright入門](https://qiita.com/simonritchie/items/7492d1c1a3c13b2f27aa)


# 設定方法

使い始めた瞬間Pyrightってクソじゃんってならないために、
[Pyrightで型チェックしたいのにimportで怒られるときの対処法](https://qiita.com/tenajima/items/81e0ea8ef70b954f7f0f)

プロジェクトルート直下に pyrightconfig.json を作成してください。

[pyrightconfig.jsonの設定方法の公式解説](https://github.com/microsoft/pyright/blob/master/docs/configuration.md)
をまずは一読してください。一番下にあるサンプルを最初に見るのがおすすめです。



https://gist.github.com/n4cl/1bad0eee4f4bac728d259d8501372c0b


https://gist.github.com/kinow/4f9407f29a8bba4f3eb09fe516413b10

これが参考になるっぽい
https://github.com/microsoft/pyright/issues/30
ということは、 dev-templateフォルダーをごっそり移動する必要がありそう。

2020/08/27現在、相対パスは使えないっぽい　でもホントかどうかよくわからん
```json

```
