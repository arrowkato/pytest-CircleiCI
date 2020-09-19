# alpine系は実行速度が遅いので、debian系列のdistributionの使用を推奨
# busterの中でも比較的軽量なslim-busterを選択
FROM python:3.8.5-slim-buster
ENV PYTHONUNBUFFERED 1

# 必要なライブラリのインストール
RUN apt-get update \
    # CircleCI用にgitを追加
    && apt-get -y install --no-install-recommends git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# poetryはapt-getに入っていないのでpip経由でいれる
RUN pip install poetry==1.0.10

RUN mkdir /install
WORKDIR /install
# poetryでインストールしているパッケージをコンテナ側でもインストールさせる
COPY ./dev-template/poetry.lock /install/
COPY ./dev-template/pyproject.toml /install/
RUN poetry install

RUN mkdir /code
WORKDIR /code









