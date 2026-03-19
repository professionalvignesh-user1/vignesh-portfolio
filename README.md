# Nephrologist Portfolio

Production-ready Django portfolio website for Dr. Vigneshwaran S.

## Features

- Premium single-page homepage with responsive layout
- SEO-ready metadata, schema markup, `robots.txt`, and `sitemap.xml`
- WhiteNoise static file serving for simple deployments
- Environment-based production settings for secret key, allowed hosts, and canonical site URL

## Local Run

1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` values into your host environment or local shell.
4. Run:
   `python manage.py migrate`
   `python manage.py collectstatic --noinput`
   `python manage.py runserver`

Open `http://127.0.0.1:8000/`.

## Deployment

Set these environment variables in production:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`
- `SITE_URL`
- `DJANGO_EMAIL_HOST`
- `DJANGO_EMAIL_PORT`
- `DJANGO_EMAIL_HOST_USER`
- `DJANGO_EMAIL_HOST_PASSWORD`
- `DJANGO_DEFAULT_FROM_EMAIL`
- `APPOINTMENT_NOTIFICATION_EMAIL`
- `DATABASE_URL` if using PostgreSQL or another hosted database

Start command:

`gunicorn nephrologist_portfolio.wsgi --log-file -`

Before going live run:

- `python manage.py migrate`
- `python manage.py collectstatic --noinput`
