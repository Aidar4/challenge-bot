# Bot schedule
Бот напоминалка

# Локальное разворачивание 
1) Установить зависимости (python 3.10)
```bash
pip install pip-tools
make install
```
2) Cоздать в корне `.env` файл на основе `.env.example`
3) Запустить:
```bash
python bot4.py
```

# Первый запуск на сервере
1) Спулить репозиторий
```bash
git clone ...
```
2) Cоздать в корне `.env` файл на основе `.env.example`
4) Собрать билд и запустить сервис:
```bash
make release
```

## Обновить версию на сервере
```bash
make release
```