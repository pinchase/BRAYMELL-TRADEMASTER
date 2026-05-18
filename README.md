# Braymell Website

![Braymells](core/static/images/logo.jpeg)

> A modern Django web application for Braymell's public-facing website and comprehensive admin-managed portfolio content management system.

**Status:** Production Ready | **Last Updated:** May 2026

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Quick Start](#-quick-start)
- [Content Management](#-content-management)
- [Project Structure](#-project-structure)
- [Useful Commands](#-useful-commands)

## ✨ Features

### Public Website

| Route                                      | Description                                                                                                                         |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Homepage** `/`                           | Route-to-market positioning, service summary, featured testimonials, and client logo carousel                                       |
| **Clients** `/clients/`                    | Curated client logo gallery with caption listing and links to detailed case studies                                                 |
| **Client Detail** `/clients/<slug>/`       | Comprehensive client overview including objective, activation footprint, team size, work summary, achievements, and brand portfolio |
| **Brand Detail** `/brands/<slug>/`         | Brand-specific narrative with objective, execution story, outcomes, curated image gallery, and related brands                       |
| **Testimonials** `/testimonials/`          | Client feedback and ratings with pagination support                                                                                 |
| **About & Contact** `/about/`, `/contact/` | Company information and contact channels                                                                                            |

### Admin Content Management System

#### Core Entities

**Clients**

- Name, slug, and company branding
- Logo, caption, and detailed description
- Client work narrative (objective, activation footprint, team size, execution summary, achievements)
- Active/inactive status with inline brand management

**Brands**

- Parent client association
- Name with auto-generated slug
- Brand identity (logo, caption)
- Strategic narrative (objective, execution, outcome)
- Display ordering and active/inactive status
- Inline gallery management

**Brand Images**

- Full image upload and management
- Caption and metadata
- Custom display ordering with lightbox support

**Testimonials**

- Client attribution (name, company, position)
- Feedback content with star ratings
- Optional imagery
- Featured content toggle for homepage promotion

**Projects** (Legacy)

- Retained for backward compatibility and internal data preservation
- Supports legacy content (objective, mechanisms, achievements, imagery)
- Automatic fallback when brand story fields are incomplete

## 🛠 Technology Stack

| Component             | Version | Purpose                         |
| --------------------- | ------- | ------------------------------- |
| Django                | 4.2.11  | Web framework                   |
| Django REST Framework | 3.14.0  | API development                 |
| drf-spectacular       | Latest  | OpenAPI/Swagger documentation   |
| django-filter         | Latest  | Advanced filtering capabilities |
| django-cors-headers   | Latest  | Cross-origin request handling   |
| Pillow                | Latest  | Image processing and uploads    |
| SQLite                | Latest  | Local development database      |

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- Virtual environment manager (venv)

### Installation Steps

**1. Navigate to the backend directory:**

```bash
cd backend
```

**2. Create and activate a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

**4. Apply database migrations:**

```bash
python manage.py migrate
```

**5. Create a superuser account:**

```bash
python manage.py createsuperuser
```

**6. Start the development server:**

```bash
python manage.py runserver
```

### Access Points

| Service           | URL                             |
| ----------------- | ------------------------------- |
| Homepage          | http://localhost:8000/          |
| Admin Panel       | http://localhost:8000/admin/    |
| API Documentation | http://localhost:8000/api/docs/ |

**Note:** If port 8000 is in use, specify an alternative:

```bash
python manage.py runserver 8001
```

## 📝 Content Management

### Workflow Overview

The content structure follows a hierarchical model:

```
Homepage Client Logo
    ↓
Client Detail Page (objective, team, execution)
    ↓
Brand Logo
    ↓
Brand Detail Page (execution story, results, gallery)
```

### Step-by-Step Guides

#### Adding a New Client

1. Navigate to `/admin/` and select **Clients**
2. Click **Add Client**
3. Enter client information:
   - Client name and slug
   - Company logo upload
   - Caption and description
4. Fill the client work narrative:
   - Objective and strategic focus
   - Stores activated / activation footprint
   - Team size deployed
   - Work executed by Braymell
   - Key achievements and results
5. Toggle **Active** to publish
6. Save

#### Adding Brands to a Client

1. Open the client record in admin
2. Use the **Brands** inline section, or navigate to **Brands** directly
3. Create or assign a brand with:
   - Brand name (slug auto-generates)
   - Brand logo
   - Caption and description
   - Strategic narrative:
     - Objective
     - Execution story
     - Outcome/results
4. Set display order
5. Toggle **Active** to publish
6. Save

#### Building a Brand Gallery

1. Open the brand record in admin
2. Scroll to **Brand Images** inline section
3. Add images with:
   - Image file upload
   - Image caption/description
   - Display order
4. Save

**Tip:** Images are automatically displayed in a lightbox gallery on the brand detail page.

## 📁 Project Structure

```
backend/
├── config/                          # Django project configuration
│   ├── settings.py                  # Project settings and environment config
│   ├── urls.py                      # Root URL routing
│   ├── wsgi.py                      # WSGI application (deployment)
│   └── asgi.py                      # ASGI application (async support)
├── core/                            # Main application
│   ├── admin.py                     # Django admin customization
│   ├── models.py                    # Database models (Client, Brand, Testimonial, etc.)
│   ├── serializers.py               # DRF serializers for API
│   ├── views.py                     # API views and endpoints
│   ├── urls.py                      # App URL routing
│   ├── migrations/                  # Database migration files
│   ├── static/                      # Static assets (CSS, JS, images)
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/                   # HTML templates
│       └── core/
├── media/                           # User-uploaded content
│   ├── brand_images/                # Brand gallery images
│   ├── brand_logos/                 # Brand logos
│   ├── client_logos/                # Client logos
│   ├── project_images/              # Legacy project images
│   └── testimonial_images/          # Testimonial photos
├── staticfiles/                     # Collected static files (production)
├── db.sqlite3                       # Local development database
├── manage.py                        # Django management script
└── requirements.txt                 # Python dependencies
```

## 🔧 Useful Commands

### Development

| Command                           | Purpose                                |
| --------------------------------- | -------------------------------------- |
| `python manage.py check`          | Verify project configuration and setup |
| `python manage.py runserver`      | Start development server               |
| `python manage.py runserver 8001` | Start on alternative port              |

### Database Management

| Command                           | Purpose                    |
| --------------------------------- | -------------------------- |
| `python manage.py makemigrations` | Create new migration files |
| `python manage.py migrate`        | Apply pending migrations   |
| `python manage.py migrate --list` | Show migration status      |

### Testing & Validation

| Command                      | Purpose                    |
| ---------------------------- | -------------------------- |
| `python manage.py test`      | Run all unit tests         |
| `python manage.py test core` | Run tests for specific app |

### Static Files

| Command                                  | Purpose                            |
| ---------------------------------------- | ---------------------------------- |
| `python manage.py collectstatic`         | Gather static files for production |
| `python manage.py collectstatic --clear` | Clear and recollect static files   |

### Admin Access

| Command                                      | Purpose                  |
| -------------------------------------------- | ------------------------ |
| `python manage.py createsuperuser`           | Create new admin account |
| `python manage.py changepassword <username>` | Reset admin password     |

## 📚 Additional Resources

- **Django Documentation:** https://docs.djangoproject.com/
- **Django REST Framework:** https://www.django-rest-framework.org/
- **drf-spectacular:** https://drf-spectacular.readthedocs.io/

## 🐛 Troubleshooting

### Database Errors

If you encounter database errors, try resetting your local database:

```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Port Already in Use

Run the server on a different port:

```bash
python manage.py runserver 8001
```

### Static Files Not Loading

Collect static files for development:

```bash
python manage.py collectstatic --no-input
```

### Missing Dependencies

Reinstall all dependencies:

```bash
pip install -r requirements.txt --force-reinstall
```

## 📧 Support

For questions or issues, please refer to the project documentation or contact the development team.

---

**Last Updated:** May 2026 | **Django Version:** 4.2.11 | **Status:** Production Ready
