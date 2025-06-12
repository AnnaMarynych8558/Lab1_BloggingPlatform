# Deployment Guide

This document explains how to deploy the Flask Blog application.

## Environment Variables

Set the following environment variables:

```bash
# Required for production
DATABASE_URL=postgresql://username:password@host:port/database
SESSION_SECRET=your-very-secure-secret-key

# Optional - for development
FLASK_ENV=development
FLASK_DEBUG=1
```

## Production Deployment

### Using Gunicorn

```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 main:app
```

### Using Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY dependencies.txt .
RUN pip install -r dependencies.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "main:app"]
```

Build and run:

```bash
docker build -t flask-blog .
docker run -p 5000:5000 --env-file .env flask-blog
```

### Database Setup

For PostgreSQL production database:

```sql
CREATE DATABASE flask_blog;
CREATE USER flask_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE flask_blog TO flask_user;
```

## Platform-Specific Deployment

### Heroku

1. Create `Procfile`:
```
web: gunicorn main:app
```

2. Deploy:
```bash
heroku create your-app-name
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
```

### Railway

1. Connect your GitHub repository
2. Set environment variables in Railway dashboard
3. Deploy automatically

### DigitalOcean App Platform

1. Connect GitHub repository
2. Configure build settings
3. Set environment variables
4. Deploy

## Security Considerations

- Always use strong SECRET_KEY in production
- Use PostgreSQL instead of SQLite in production
- Enable HTTPS
- Set secure session cookies
- Regular security updates