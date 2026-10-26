# hello-app — приклад до есе про Dockerfile

## Файли
- `app.py` — вебсервіс на Flask
- `requirements.txt` — залежності Python
- `Dockerfile` — опис образу
- `.dockerignore` — що не копіювати в образ
- `ese.md` — есе (індивідуальна робота)

## Запуск на сервері
```bash
cd dockerfile-project
docker build -t hello-app .
docker run -d -p 5000:5000 --name hello hello-app
curl http://localhost:5000      # -> Привіт з контейнера!
```
Ззовні: `http://<IP-сервера>:5000` (порт 5000 має бути відкритий у фаєрволі).

## Зупинити / видалити
```bash
docker stop hello && docker rm hello
```
