# testTaskWithSomeNginxUsage

## Installation
0. `docker v20.10.X`
1. `python 3.11.X`
2. `activate venv`
3. `pip install -r requirements.txt`

## Run nginx and web service
(Yoo should run command under venv in root project directory)
`docker run -d --rm --name test_cache_nginx --net host -v $PWD/nginx_conf/config/nginx.conf:/etc/nginx/nginx.conf:ro -v $PWD/nginx_conf/web_data:/usr/share/nginx/html:ro nginx:alpine && fastapi run http_service/service_cache.py --port 8080 && docker stop test_cache_nginx`
( http://localhost:80 )

There is no automatic startup for web server for now

## Run tests
`pytest . -m nginx_cache`
