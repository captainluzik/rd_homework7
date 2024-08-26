## Running the Services
### Flask (WSGI)
```gunicorn wsgi:app -w 4 -k gthread```
### Quart (ASGI)
```hypercorn asgi:app```
### Starlette (ASGI)
```uvicorn starlette:app --workers 4 --loop asyncio```
### FastAPI (ASGI)
```uvicorn fastapi_app:app --workers 4 --loop asyncio```

## Testing the Services
```hey -n 10000 -c 100 http://127.0.0.1:8000/```