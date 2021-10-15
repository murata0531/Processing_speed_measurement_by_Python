# Processing_speed_measurement_by_Python

Pythonで処理速度を測るリポジトリ

単純な計算やデータベースアクセスの速度を測る

## 構築

各種コンテナをつなぐnetworkを設定

    docker network create fastapi_network

## コンテナ起動

    docker-compose up -d

## データベースマイグレーション
    
    docker-compose run api bash

    # cd /usr/src/app/db

マイグレーションファイル生成

    # alembic revision --autogenerate -m 'コメント'

マイグレーション実行

    # alembic upgrade head

データベースの設定は ` app/settings.py ` の ` DATABASES ` 項目にある

http://localhost:8000/docs 