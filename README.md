# Processing_speed_measurement_by_Python

Pythonで処理速度を測るリポジトリ

単純な計算やデータベースアクセスの速度を測る

# 構築

コンテナ起動

    docker-compose up -d

データベースマイグレーション
    docker-compose run --rm web python manage.py migrate

データベースの設定は ` app/settings.py ` の ` DATABASES ` 項目にある
