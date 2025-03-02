# Yatube API Documentation

Yatube API позволяет управлять постами, комментариями и группами в социальной сети Yatube. API поддерживает создание, чтение, обновление и удаление постов и комментариев, а также получение информации о группах.

## Базовый URL

Все запросы выполняются к базовому URL:

```
https://domain.xxx/api/v1/
```

## Аутентификация

Для доступа к API требуется аутентификация по токену. Чтобы получить токен, выполните POST-запрос на эндпоинт:

```
POST /api/v1/api-token-auth/
```

**Параметры запроса:**

- `username` (строка): Логин пользователя.
- `password` (строка): Пароль пользователя.

**Пример запроса:**

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

**Пример ответа:**

```json
{
    "token": "ваш_токен"
}
```

Полученный токен необходимо передавать в заголовке `Authorization` для всех последующих запросов:

```
Authorization: Token ваш_токен
```

## Эндпоинты

### Посты

#### Получить список всех постов или создать новый пост

```
GET /api/v1/posts/
POST /api/v1/posts/
```

**GET-запрос:**

Возвращает список всех постов.

**Пример ответа:**

```json
[
    {
        "id": 14,
        "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
        "author": "anton",
        "image": null,
        "group": 1,
        "pub_date": "2021-06-01T08:47:11.084589Z"
    },
    ...
]
```

**POST-запрос:**

Создаёт новый пост.

**Параметры запроса:**

- `text` (строка): Текст поста.
- `group` (число, опционально): ID группы, к которой относится пост.

**Пример запроса:**

```json
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
}
```

**Пример ответа:**

```json
{
    "id": 14,
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
}
```

#### Получить, редактировать или удалить пост

```
GET /api/v1/posts/{post_id}/
PUT /api/v1/posts/{post_id}/
PATCH /api/v1/posts/{post_id}/
DELETE /api/v1/posts/{post_id}/
```

**GET-запрос:**

Возвращает информацию о посте с указанным `post_id`.

**PUT/PATCH-запрос:**

Редактирует пост с указанным `post_id`.

**DELETE-запрос:**

Удаляет пост с указанным `post_id`.

### Группы

#### Получить список всех групп

```
GET /api/v1/groups/
```

**Пример ответа:**

```json
[
    {
        "id": 1,
        "title": "Литература",
        "slug": "literature",
        "description": "Посты на тему литературы"
    },
    ...
]
```

#### Получить информацию о группе

```
GET /api/v1/groups/{group_id}/
```

**Пример ответа:**

```json
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
}
```

### Комментарии

#### Получить список всех комментариев поста или создать новый комментарий

```
GET /api/v1/posts/{post_id}/comments/
POST /api/v1/posts/{post_id}/comments/
```

**GET-запрос:**

Возвращает список всех комментариев для поста с указанным `post_id`.

**POST-запрос:**

Создаёт новый комментарий для поста с указанным `post_id`.

**Параметры запроса:**

- `text` (строка): Текст комментария.

**Пример запроса:**

```json
{
    "text": "тест тест"
}
```

**Пример ответа:**

```json
{
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "тест тест",
    "created": "2021-06-01T10:14:51.388932Z"
}
```

#### Получить, редактировать или удалить комментарий

```
GET /api/v1/posts/{post_id}/comments/{comment_id}/
PUT /api/v1/posts/{post_id}/comments/{comment_id}/
PATCH /api/v1/posts/{post_id}/comments/{comment_id}/
DELETE /api/v1/posts/{post_id}/comments/{comment_id}/
```

**GET-запрос:**

Возвращает информацию о комментарии с указанным `comment_id`.

**PUT/PATCH-запрос:**

Редактирует комментарий с указанным `comment_id`.

**DELETE-запрос:**

Удаляет комментарий с указанным `comment_id`.

## Формат данных

Все данные возвращаются в формате JSON.

## Ограничения

Ограничений на количество запросов нет.

## Коды ошибок

- `400 Bad Request`: Неверный запрос.
- `401 Unauthorized`: Требуется аутентификация.
- `403 Forbidden`: Доступ запрещён.
- `404 Not Found`: Ресурс не найден.
- `500 Internal Server Error`: Ошибка на сервере.

---

Для дополнительной информации, пожалуйста, свяжитесь с разработчиком.