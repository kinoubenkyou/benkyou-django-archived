# benkyou-django

## config

```shell
git config core.hooksPath hooks
docker compose run --no-deps --rm --volume .:/app app sh -c "tr -dc [:alnum:] < /dev/urandom | head -c 50 > django_secret_key"
docker compose run --no-deps --rm --volume .:/app app sh -c "tr -dc [:alnum:] < /dev/urandom | head -c 20 > postgres_password"
docker compose run --rm app sh -c "python manage.py migrate"
```

## start

```shell
docker compose up -d
```

## stop

```shell
docker compose stop
```

## test

```shell
docker compose run --rm app sh -c "python manage.py test"
```

## shell

```shell
docker exec -it benkyou-django-app-1 sh
```
