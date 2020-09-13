# CircleCI
CI/CDパイプラインの構築には、CircleCIを使います。

## 採用理由
デファクトスタンダードなので、採用します。
他の候補としては下記あたりなので、各リーダーが使いやすいサービスを採用してください。
- GitHub Actions
- AWSのCode Commit, Code Build, Code Deploy, Code Pipeline,
- GCPのCloud Build　Artifact Regisry
AWS以外は、無料枠がどのサービスもあるはずなので、試しに使ってみてから決めてもいいかもしれません。

## 便利ツール
CircleCI自体の設定を config.yml
コミットせずに、.circleci/config.yml の動作確認ができるツールです。
[CircleCI のローカル CLI の使用](https://circleci.com/docs/ja/2.0/local-cli/)

Macの場合
```zsh
brew install circleci
```

## CircleCIで使用するDocker Imageを登録する
[GitHubのDockerfileを自動的にビルドして、Dockerhubに登録する方法](https://qiita.com/kon_yu/items/7c40f4dfbd1cce006ce7#github%E3%81%A8%E9%80%A3%E6%90%BA%E3%81%99%E3%82%8B%E3%82%AA%E3%82%B9%E3%82%B9%E3%83%A1) があります。
