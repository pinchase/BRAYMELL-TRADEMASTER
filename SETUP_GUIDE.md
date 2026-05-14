# Braymell Website - Complete Setup & Deployment Guide

![Braymells](/core/static/images/logo.jpeg)

> A modern Django web application for Braymell's public-facing website and comprehensive admin-managed portfolio content management system.

**Status:** Production Ready | **Last Updated:** May 2026

---

## 📋 Quick Navigation

- **🏠 [Getting Started](#getting-started)** - Quick start guide
- **💻 [Local Development](LOCAL_SETUP.md)** - Full local setup instructions
- **🚀 [Render Deployment](RENDER_DEPLOYMENT_GUIDE.md)** - Complete deployment guide
- **📚 [Project Structure](#project-structure)** - Codebase overview
- **🔧 [Technology Stack](#technology-stack)** - Tools and frameworks

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL
- Git

### Quick Start (5 minutes)

1. **Clone and Setup:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/braymell.git
   cd braymell/backend
   python3.11 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure Environment:**

   ```bash
   cp .env.example .env
   # Edit .env with your database and API credentials
   ```

3. **Initialize Database:**

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run Development Server:**
   ```bash
   python manage.py runserver
   ```

Access the app at: `http://localhost:8000`

---

## 📚 Documentation

### For Local Development

**Read:** [`LOCAL_SETUP.md`](LOCAL_SETUP.md)

- Complete environment setup
- Database configuration (Docker/PostgreSQL)
- Development commands
- Troubleshooting guide

### For Production Deployment

**Read:** [`RENDER_DEPLOYMENT_GUIDE.md`](RENDER_DEPLOYMENT_GUIDE.md)

- Step-by-step Render deployment
- Environment variables configuration
- Database setup on Render
- Post-deployment verification
- Troubleshooting

---

## 🎯 Features

### Public Website

| Route                  | Feature                             |
| ---------------------- | ----------------------------------- |
| **`/`**                | Homepage with featured content      |
| **`/clients/`**        | Client portfolio gallery            |
| **`/clients/<slug>/`** | Detailed client case studies        |
| **`/brands/<slug>/`**  | Brand-specific narratives           |
| **`/testimonials/`**   | Client testimonials with pagination |
| **`/about/`**          | Company information                 |
| **`/contact/`**        | Contact form                        |

### Admin Dashboard (Jazzmin)

- **Content Management**: Clients, Projects, Brands, Testimonials
- **Media Management**: Image uploads via Cloudinary
- **Analytics**: Track performance metrics
- **User Management**: Team access control

### API (REST Framework)

- **OpenAPI/Swagger Documentation** at `/api/docs/`
- **REDOCs** at `/api/redoc/`
- **Filtering, Searching, Pagination** built-in
- **API Versioning** (`/api/v1/`)

---

## 🔧 Technology Stack

### Backend

- **Framework:** Django 4.2.11
- **API:** Django REST Framework 3.14
- **Database:** PostgreSQL
- **Server:** Gunicorn
- **Admin:** Jazzmin (Django Admin enhancement)

### Frontend (Templating)

- **Template Engine:** Django Templates
- **CSS:** Custom CSS with responsive design
- **Static Files:** WhiteNoise middleware

### Storage & Media

- **Media Storage:** Cloudinary
- **Static Files:** WhiteNoise

### Development Tools

- **API Docs:** drf-spectacular
- **Image Processing:** Pillow
- **Rich Text Editor:** django-ckeditor
- **Linting/Tools:** django-extensions

### Deployment

- **Hosting:** Render.com
- **Process Manager:** Gunicorn
- **Continuous Deployment:** Git integration

---

## 📁 Project Structure

```
braymell/
├── backend/                          # Django application root
│
├── 📄 Configuration Files
│   ├── manage.py                    # Django CLI
│   ├── requirements.txt             # Python dependencies
│   ├── runtime.txt                  # Python version (3.11.9)
│   ├── Procfile                     # Render process definition
│   ├── .env.example                 # Environment variables template
│   └── .gitignore                   # Git ignore rules
│
├── 🔨 Deployment Scripts
│   ├── build.sh                     # Build script for Render
│   └── start.sh                     # Local start script
│
├── 📖 Documentation
│   ├── README.md                    # Original project README
│   ├── LOCAL_SETUP.md               # Local development guide
│   └── RENDER_DEPLOYMENT_GUIDE.md   # Production deployment guide
│
├── config/                          # Django settings
│   ├── settings.py                  # Main configuration
│   ├── urls.py                      # URL routing
│   ├── wsgi.py                      # WSGI application
│   └── asgi.py                      # ASGI application
│
├── core/                            # Main application
│   ├── models.py                    # Database models
│   ├── views.py                     # View logic
│   ├── serializers.py               # REST API serializers
│   ├── urls.py                      # App URLs
│   ├── admin.py                     # Admin configuration
│   │
│   ├── templates/core/              # HTML templates
│   │   ├── base.html                # Base template
│   │   ├── home.html                # Homepage
│   │   ├── clients.html             # Clients list
│   │   ├── client_detail.html       # Client detail
│   │   ├── brand_detail.html        # Brand detail
│   │   ├── testimonials.html        # Testimonials
│   │   ├── about.html               # About page
│   │   └── contact.html             # Contact page
│   │
│   ├── static/                      # Static assets
│   │   ├── css/
│   │   │   └── style.css            # Main stylesheet
│   │   ├── js/
│   │   │   └── main.js              # Main JavaScript
│   │   └── images/
│   │       └── logo.jpeg            # Logo and images
│   │
│   └── migrations/                  # Database migrations
│
├── staticfiles/                     # Collected static files (generated)
└── media/                           # Local media (production uses Cloudinary)
```

---

## 🗄️ Database Models

### Client

- `name`: Client company name
- `slug`: URL-friendly identifier
- `description`: Company overview
- `logo`: Brand logo (Cloudinary)

### Project (Portfolio Work)

- `title`: Project name
- `slug`: URL-friendly identifier
- `client`: Foreign key to Client
- `description`: Project overview
- `objective`: Business objective
- `execution`: Execution story
- `outcomes`: Results achieved
- `team_size`: Team count
- `activation_footprint`: Geographic reach
- `work_summary`: Brief summary

### Brand (Product Brands)

- `name`: Brand name
- `slug`: URL-friendly identifier
- `client`: Foreign key to Client
- `objective`: Brand objective
- `execution`: Brand execution story
- `outcomes`: Brand results
- `caption`: Brand caption
- `logo`: Brand logo (Cloudinary)

### Testimonial

- `client`: Foreign key to Client
- `author`: Author name
- `position`: Author position
- `content`: Testimonial text
- `rating`: Star rating (1-5)
- `created_at`: Timestamp

---

## 🔐 Security Features

- ✅ **HTTPS:** Automatically enforced on Render
- ✅ **CSRF Protection:** Django built-in
- ✅ **CORS:** Configurable by environment
- ✅ **Secret Key:** Environment-based, never hardcoded
- ✅ **Debug Mode:** Disabled in production
- ✅ **SQL Injection Protection:** Django ORM prevents this
- ✅ **XSS Protection:** Django templates auto-escape
- ✅ **Secure Headers:** Security middleware enabled

---

## 📊 Database Schema

### Entity Relationships

```
Client
├── has many → Project
└── has many → Brand
└── has many → Testimonial

Project
├── belongs to → Client
└── has many → ProjectImage

Brand
├── belongs to → Client
└── has many → BrandImage

Testimonial
└── belongs to → Client
```

---

## 🚀 Deployment Process

### Quick Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] `requirements.txt` updated
- [ ] Environment variables set on Render
- [ ] Database migrations applied
- [ ] Superuser created
- [ ] Static files collected
- [ ] Domain configured
- [ ] CORS settings updated

### One-Command Deployment

After first setup, just:

```bash
git push origin main
```

Render automatically deploys on push!

---

## 🔧 Configuration Management

### Environment Variables

**Development (`.env` file):**

```bash
DEBUG=True
DATABASE_URL=postgresql://user:pass@localhost/braymell
SECRET_KEY=dev-key-here
```

**Production (Render Settings):**

```bash
DEBUG=False
DATABASE_URL=postgresql://...render.com:5432/...
SECRET_KEY=strong-random-key
CLOUDINARY_CLOUD_NAME=...
CLOUDINARY_API_KEY=...
CLOUDINARY_API_SECRET=...
```

### ALLOWED_HOSTS Configuration

```python
# .env
ALLOWED_HOSTS=braymell.onrender.com,braymell.com,www.braymell.com
```

### CORS Configuration

```python
# .env
CORS_ALLOWED_ORIGINS=https://braymell.com,https://www.braymell.com
```

---

## 🧪 Testing

### Run Tests

```bash
python manage.py test
```

### Create Test Data

```bash
python manage.py shell

from core.models import Client, Project
from django.utils.text import slugify

# Create test client
client = Client.objects.create(
    name="Test Corp",
    slug=slugify("Test Corp"),
    description="Test company"
)
```

---

## 📈 Performance Optimization

### Implemented Features

- ✅ **Whitenoise:** Serves static files efficiently
- ✅ **Database Indexing:** Configured on key fields
- ✅ **Query Optimization:** select_related/prefetch_related
- ✅ **Pagination:** 9 items per page by default
- ✅ **Cloudinary CDN:** Image optimization and delivery

### Recommendations

- Enable Render caching
- Add Redis for session storage
- Configure image optimization settings
- Monitor database query performance

---

## 🐛 Troubleshooting

### Common Issues

**502 Bad Gateway**
→ Check Render logs for errors

**Static files not loading**
→ Run `python manage.py collectstatic --clear --noinput`

**Database connection failed**
→ Verify DATABASE_URL and PostgreSQL status

**Cloudinary images not showing**
→ Verify credentials and API keys

See [RENDER_DEPLOYMENT_GUIDE.md](RENDER_DEPLOYMENT_GUIDE.md#troubleshooting) for detailed solutions.

---

## 📞 Support Resources

- **Django:** https://docs.djangoproject.com/
- **DRF:** https://www.django-rest-framework.org/
- **Render:** https://render.com/docs
- **Cloudinary:** https://cloudinary.com/documentation
- **PostgreSQL:** https://www.postgresql.org/docs/

---

## 📝 Commands Reference

### Common Commands

```bash
# Development
python manage.py runserver

# Database
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser

# Static files
python manage.py collectstatic

# Interactive shell
python manage.py shell

# Admin tasks
python manage.py createsuperuser
python manage.py changepassword username

# Testing
python manage.py test
```

---

## 🎓 Learning Resources

- Start with [LOCAL_SETUP.md](LOCAL_SETUP.md) for development
- Review [RENDER_DEPLOYMENT_GUIDE.md](RENDER_DEPLOYMENT_GUIDE.md) for production
- Check Django docs for model/view queries
- Explore API at `/api/docs/` when running

---

## 📄 License

This project is proprietary to Braymell. All rights reserved.

---

## 👥 Team

**Braymell Team** - Route-to-market strategy, retail execution, and brand growth support.

**Website:** https://braymell.com
**Email:** info@braymell.com

---

## 🔄 Workflow Summary

### For Developers

1. **Local Development**

   ```bash
   source venv/bin/activate
   python manage.py runserver
   ```

2. **Make Changes**

   - Edit models/views
   - Create migrations: `makemigrations`
   - Test locally

3. **Deploy**
   ```bash
   git add .
   git commit -m "message"
   git push origin main
   ```

### For Content Managers

1. **Access Admin**
   → https://braymell.onrender.com/admin/

2. **Create Content**
   → Add Clients, Projects, Brands, Testimonials

3. **Publish**
   → Changes appear immediately on website

---

## 🎯 Next Steps

1. **Set up locally:** Follow [LOCAL_SETUP.md](LOCAL_SETUP.md)
2. **Deploy to Render:** Follow [RENDER_DEPLOYMENT_GUIDE.md](RENDER_DEPLOYMENT_GUIDE.md)
3. **Configure domain:** Add your custom domain to Render
4. **Start creating content:** Use admin dashboard

---

**Ready to get started? Head to [LOCAL_SETUP.md](LOCAL_SETUP.md) or [RENDER_DEPLOYMENT_GUIDE.md](RENDER_DEPLOYMENT_GUIDE.md)!** 🚀
