# Member Management System

A Django-based web application for managing member information with full CRUD (Create, Read, Update, Delete) operations.

## Project Overview

This is a simple yet functional member management system built with Django 5.0.1. The application allows users to manage member records including personal information such as names, email, phone numbers, and country details.

## Features

- **View Members**: Display all members in a tabular format
- **Add Members**: Create new member records with personal information
- **Update Members**: Edit existing member information
- **Delete Members**: Remove member records from the database
- **Responsive UI**: Clean and user-friendly interface with custom CSS styling

## Architecture

### Project Structure

```
mypro/                      # Main Django project
├── mypro/                  # Project configuration
│   ├── __init__.py
│   ├── settings.py         # Django settings and configuration
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── newapp/                 # Main application
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   ├── index.html      # Member list view
│   │   ├── add.html        # Add member form
│   │   └── update.html     # Update member form
│   ├── static/
│   │   └── style.css       # Custom styling
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # App URL routing
│   ├── admin.py            # Admin configuration
│   └── apps.py             # App configuration
├── db.sqlite3              # SQLite database file
└── manage.py               # Django management script
```

### Technology Stack

- **Backend**: Django 5.0.1 (Python web framework)
- **Database**: SQLite3 (default Django database)
- **Frontend**: HTML5, CSS3
- **Template Engine**: Django Templates

## Data Storage

### Database Configuration

The application uses SQLite3 as the default database, configured in `mypro/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Data Model

The application has a single model `Member` defined in `newapp/models.py`:

```python
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
```

**Database Schema:**
- **Table**: `newapp_member`
- **Fields**:
  - `id`: Auto-incrementing primary key (BigAutoField)
  - `firstname`: VARCHAR(100) - Member's first name
  - `lastname`: VARCHAR(100) - Member's last name
  - `email`: VARCHAR(100) - Member's email address
  - `phonenumber`: VARCHAR(100) - Member's phone number
  - `country`: VARCHAR(100) - Member's country

## Application Flow

### URL Routing

**Main URLs** (`mypro/urls.py`):
- `/admin/` - Django admin interface
- `/` - Redirects to newapp URLs

**App URLs** (`newapp/urls.py`):
- `/` - Display all members (index view)
- `/add/` - Show add member form
- `/addrec/` - Process add member form submission
- `/delete/<id>/` - Delete specific member
- `/update/<id>/` - Show update form for specific member
- `/update/uprec/<id>/` - Process update form submission

### View Functions

1. **index(request)**: Retrieves all members and displays them in a table
2. **add(request)**: Renders the add member form
3. **addrec(request)**: Processes POST data to create new member
4. **delete(request, id)**: Deletes member by ID and redirects to index
5. **update(request, id)**: Retrieves member by ID and shows update form
6. **uprec(request, id)**: Processes POST data to update existing member

### Data Flow

1. **Create**: User fills form → POST to `/addrec/` → Data saved to database → Redirect to index
2. **Read**: User visits `/` → View queries all members → Template renders table
3. **Update**: User clicks update → GET member data → Show pre-filled form → POST to `/update/uprec/<id>/` → Update database → Redirect to index
4. **Delete**: User clicks delete → POST to `/delete/<id>/` → Remove from database → Redirect to index

## Installation & Setup

### Prerequisites

- Python 3.8+
- Django 5.0.1

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mypro
   ```

2. **Install dependencies**
   ```bash
   pip install django==5.0.1
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Main app: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

1. **View Members**: Navigate to the home page to see all registered members
2. **Add Member**: Click "Add Member" button and fill in the required information
3. **Update Member**: Click "Update" button next to any member to edit their information
4. **Delete Member**: Click "Delete" button next to any member to remove them

## Security Considerations

⚠️ **Important**: This is a development setup with the following security considerations:

- `DEBUG = True` - Should be `False` in production
- `SECRET_KEY` is exposed - Should be environment variable in production
- `ALLOWED_HOSTS = []` - Should be configured for production domains
- No input validation - Should add form validation for production use
- Email field uses CharField instead of EmailField - Consider using proper field types

## Future Enhancements

- Add form validation and error handling
- Implement user authentication and authorization
- Add search and filtering functionality
- Implement pagination for large datasets
- Add email validation and phone number formatting
- Include unit tests and integration tests
- Add API endpoints for mobile/external integrations

