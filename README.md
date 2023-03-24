# Run project

1. ```docker build tthack/videohosting .```
2. ```cp config.example.toml config.toml``` - change some constants if you need to
3. ```docker-compose up```
4. ```docker exec -ti tthack-videohosting poetry run alembic upgrade head```