# alpine系は実行速度が遅いので、debian系列のdistributionの使用を推奨
# busterの中でも比較的軽量なslim-busterを選択
FROM python:3.8.5-slim-buster
ENV PYTHONUNBUFFERED 1

# 必要なライブラリのインストール
RUN apt-get update \
    # CircleCI用にgitを追加
    && apt-get -y install --no-install-recommends git \
    default-mysql-client \
    # 不要なら消してください。
    vim less \
    # Docker imageのサイズ削減
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# poetryはapt-getに入っていないのでpip経由でいれる
RUN pip install poetry==1.0.10

# dev-template はプロジェクトごとに変更してください。
RUN mkdir -p /code/dev-template
WORKDIR /code/dev-template


