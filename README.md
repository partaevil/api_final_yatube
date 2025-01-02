
# api_final
api final

## описание

я не знаю о чем это проект 

но что-то связанное с котами (возможно)

## установка

```bash
git clone этот репозиторий
cd туда
python -m venv .venv  
source .venv/bin/activate 
pip install -r requirements.txt
cd yatube_api 
python manage.py migrate 
python manage.py runserver
```

> [!CAUTION]
> возможно нужно обновить библиотеки из requirements.txt чтобы заработало (лично я обновил)

## примеры

```bash
curl -X GET http://127.0.0.1:8000/api/v1/follow/ \
-H "Authorization: Token <токен>"
```

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/follow/?search=john" \
-H "Authorization: Token <токен>"
```
