# Workshop Booking System

Система управления бронированием мастер-классов. Пользователи просматривают мастер-классы и записываются на них, администраторы управляют каталогом.

## Стек

**Backend**
- Django 6 + Python 3.13
- Django REST Framework
- SQLite (файл `data/db.sqlite3`)
- JWT-аутентификация (djangorestframework-simplejwt)
- djangorestframework-camel-case (snake_case → camelCase для фронта)

**Frontend**
- Next.js 16 + TypeScript
- Tailwind CSS v4

**Инфраструктура**
- Docker + docker-compose

## Запуск

```bash
docker-compose up --build
```

API доступен на `http://localhost:8000`, клиент — `http://localhost:3000`.

<details>
<summary>Запуск без Docker</summary>

```bash
# Backend (порт 8000)
python3 -m venv django-env
source django-env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000

# Frontend (порт 3000)
cd client
npm install
npm run dev
```

</details>

## Функционал

**Для всех**
- Просмотр списка мастер-классов с количеством свободных мест
- Детальная страница мастер-класса

**Для авторизованных пользователей**
- Запись на мастер-класс (с проверкой вместимости и дублирования)
- Просмотр своих броней (`/my-bookings`)
- Отмена брони

**Для администратора**
- Создание, редактирование, удаление мастер-классов (`/admin/workshops`)

## API

| Метод  | Путь                    | Доступ           |
|--------|-------------------------|------------------|
| POST   | /api/auth/register/     | Публичный        |
| POST   | /api/auth/login/        | Публичный        |
| GET    | /api/workshops/         | Публичный        |
| GET    | /api/workshops/:id/     | Публичный        |
| POST   | /api/workshops/         | Admin            |
| PUT    | /api/workshops/:id/     | Admin            |
| DELETE | /api/workshops/:id/     | Admin            |
| POST   | /api/bookings/my/       | Авторизованный   |
| GET    | /api/bookings/my/       | Авторизованный   |
| DELETE | /api/bookings/:id/      | Авторизованный   |

## Структура проекта

```
django-booking/
├── apps/
│   ├── bookings/      # бронирования
│   ├── core/          # валидаторы
│   ├── users/         # аутентификация, кастомная модель User
│   └── workshops/     # мастер-классы
├── client/            # Next.js фронтенд
├── config/            # настройки Django, urls
├── data/              # SQLite база данных
├── docker-compose.yml
└── manage.py
```

## Учётные данные администратора

```
Email:    admin@test.com
Password: secret123
```

Создаются автоматически при первом запуске (`migrate`).
