# Створення GitHub Репозиторію для Flask Blog

## Крок 1: Створення репозиторію на GitHub

1. Перейдіть на https://github.com/new
2. Заповніть дані:
   - **Repository name**: `flask-blog`
   - **Description**: `Modern Flask blog application with authentication, posts, and comments`
   - **Public** (публічний репозиторій)
   - **НЕ додавайте** README, .gitignore або LICENSE (вони вже є)

## Крок 2: Завантаження коду

Скопіюйте ці команди та виконайте їх у терміналі:

```bash
# Перехід до папки проєкту
cd /path/to/your/project

# Ініціалізація Git (якщо потрібно)
git init

# Додавання віддаленого репозиторію (замініть USERNAME на ваш логін)
git remote add origin https://github.com/USERNAME/flask-blog.git

# Додавання всіх файлів
git add .

# Створення першого комміту
git commit -m "Initial commit: Complete Flask Blog Application

Features:
- User authentication (register, login, logout)
- Post management (create, edit, delete)
- Comment system
- Category organization
- Responsive Bootstrap design
- PostgreSQL database support
- Admin functionality"

# Встановлення основної гілки
git branch -M main

# Завантаження на GitHub
git push -u origin main
```

## Структура файлів для репозиторію:

### Основні файли додатку:
- `app.py` - Flask application setup
- `main.py` - Entry point
- `models.py` - Database models
- `routes.py` - URL routes and handlers
- `forms.py` - WTForms definitions

### Шаблони (templates/):
- `base.html` - Base template
- `index.html` - Homepage
- `login.html` - Login page
- `register.html` - Registration page
- `create_post.html` - Post creation
- `edit_post.html` - Post editing
- `post_detail.html` - Post view
- `profile.html` - User profile
- `create_category.html` - Category creation
- `error.html` - Error pages

### Статичні файли:
- `static/style.css` - Custom styles

### Документація:
- `README.md` - Project documentation
- `LICENSE` - MIT License
- `dependencies.txt` - Python packages
- `DEPLOYMENT.md` - Deployment guide
- `.gitignore` - Git ignore rules

## Крок 3: Налаштування репозиторію

Після створення:

1. **Додайте теги**:
   ```bash
   git tag -a v1.0.0 -m "Release 1.0.0"
   git push origin v1.0.0
   ```

2. **Налаштуйте About section**:
   - Website: URL вашого деплою
   - Topics: `flask`, `python`, `blog`, `bootstrap`, `web-app`

3. **Створіть Release**:
   - Releases → Create a new release
   - Tag: v1.0.0
   - Title: "Flask Blog v1.0.0"

## Результат

Ваш репозиторій буде містити повнофункціональний Flask блог з:
- Системою автентифікації
- Управлінням постами
- Коментарями
- Адаптивним дизайном
- Повною документацією

URL репозиторію: `https://github.com/USERNAME/flask-blog`