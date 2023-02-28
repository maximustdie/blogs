# Blogs

### Запуск
```
cd blogs
docker compose -f docker-compose.local.yml up --build -d
```
### Просмотр логов приложения
```
docker logs -f call_api
```
### Открытие консоли
```
docker exec -it call_api bash
```