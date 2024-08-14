# benkyou-django

## config

```shell
tr -dc [:alnum:] < /dev/urandom | head -c 50 > django_secret_key
```

## start

```shell
docker compose up -d
```

## stop

```shell
docker compose stop
```

## shell

```shell
docker exec -it benkyou-django-app-1 sh
```
