# testTaskWithSomeNginxUsage

## Installation
0. `docker v20.10.X`
1. `python 3.11.X`
2. `activate venv`
3. `pip install -r requirements.txt`

## Run nginx
`docker run -d --rm -p 80:80 -v $PWD/nginx_conf/config/nginx.conf:/etc/nginx/nginx.conf:ro -v ./nginx_conf/web_data:/usr/share/nginx/html:ro nginx:alpine`
( http://localhost:80 )

## Run tests
`pytest . -m nginx_cache`
