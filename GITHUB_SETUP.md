# Налаштування GitHub Репозиторію

## Кроки для створення публічного репозиторію:

### 1. Створення репозиторію на GitHub

1. Відкрийте [GitHub](https://github.com) та увійдіть в обліковий запис
2. Натисніть зелену кнопку "New" або перейдіть до https://github.com/new
3. Заповніть форму:
   - **Repository name**: `flask-blog` (або інша назва)
   - **Description**: `Сучасний веб-додаток блогу на Flask з автентифікацією та коментарями`
   - **Visibility**: Public (публічний)
   - **НЕ** додавайте README, .gitignore або LICENSE (вони вже створені)

### 2. Підключення локального репозиторію

Виконайте команди в терміналі проєкту:

```bash
# Додати віддалений репозиторій
git remote add origin https://github.com/ВАШ_ЛОГІН/flask-blog.git

# Додати всі файли
git add .

# Створити перший коміт
git commit -m "Initial commit: Flask Blog application

- User authentication system
- Post creation and editing
- Comment system
- Category management
- Responsive Bootstrap design
- PostgreSQL database support"

# Відправити код на GitHub
git branch -M main
git push -u origin main
```

### 3. Налаштування репозиторію

Після публікації:

1. **Додати теги релізу**:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

2. **Налаштувати GitHub Pages** (опційно):
   - Settings → Pages → Source: Deploy from a branch → main

3. **Додати topics** в налаштуваннях репозиторію:
   - `flask`
   - `python`
   - `blog`
   - `bootstrap`
   - `web-application`
   - `postgresql`

### 4. Опис для GitHub

Використайте цей опис для репозиторію:

```
🚀 Сучасний веб-додаток блогу на Flask з автентифікацією користувачів, системою постів та коментарів. Адаптивний дизайн з Bootstrap, підтримка PostgreSQL та повний функціонал для ведення блогу.
```

### 5. Файли проєкту

Репозиторій містить:

- ✅ `README.md` - Детальна документація
- ✅ `LICENSE` - MIT ліцензія
- ✅ `.gitignore` - Виключення файлів
- ✅ `dependencies.txt` - Python залежності
- ✅ `DEPLOYMENT.md` - Інструкції для розгортання
- ✅ Повний код додатку

### 6. Клонування репозиторію

Інші користувачі зможуть клонувати проєкт:

```bash
git clone https://github.com/ВАШ_ЛОГІН/flask-blog.git
cd flask-blog
pip install -r dependencies.txt
python main.py
```

## Корисні команди Git

```bash
# Перевірити статус
git status

# Додати зміни
git add .

# Створити коміт
git commit -m "Опис змін"

# Відправити на GitHub
git push

# Перегляд історії
git log --oneline
```

Репозиторій готовий до публікації!