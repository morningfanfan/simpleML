pwd = `pwd`

run:
  python3 src/main.py

build:
  docker build -t simple-ml:latest .

run-image:
  docker run -d --rm --name simpleML \
    -p 8080:80 --env-file .env \
    -v {{pwd}}/assets:/app/assets \
    -v {{pwd}}/database/local.db:/app/local.db \
    simple-ml:latest

copy-model:
  cp exp/*.pkl assets/models

icombo: build run-image