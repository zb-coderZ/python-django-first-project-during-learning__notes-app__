# Django Notes Management System

A beginner-friendly Django project built to learn the fundamentals of Django development. This project demonstrates how to work with models, relationships, templates, views, the Django ORM, and forms for filtering existing data.

---

## Features

- Display all notes
- View note details
- Search stores by selecting a note variety
- Display matching stores based on the selected note
- Responsive UI using Tailwind CSS
- Django Admin integration
- Database relationships (One-to-One, One-to-Many, Many-to-Many)

---

## Technologies Used

- Python
- Django
- SQLite
- HTML5
- Tailwind CSS

---

## Project Structure

```
firstProject/
│
├── notes/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── templates/
│
├── static/
├── media/
├── templates/
└── manage.py
```

---

## Concepts Learned

### Django Fundamentals

- Django Project & App
- URL Routing
- Views
- Templates
- Template Inheritance
- Static & Media Files

### Django Models

- Creating Models
- Model Fields
- Migrations
- Django ORM
- QuerySets

### Model Relationships

- One-to-Many (`ForeignKey`)
- Many-to-Many (`ManyToManyField`)
- One-to-One (`OneToOneField`)
- `related_name`

### Django Admin

- Registering Models
- `list_display`
- `TabularInline`

### Django Forms

- Creating Forms
- `ModelChoiceField`
- Handling GET & POST Requests
- Form Validation
- `cleaned_data`
- Searching Database Records
- Displaying Filtered Results

---

## Database Models

### Note

- Name
- Image
- Description
- Created Date

### Reviews

- User
- Rating
- Comment
- Related Note

### Store

- Name
- Location
- Related Note Varieties (Many-to-Many)

### Certificate

- Certificate Name
- Issue Date
- Valid Until
- Related Note (One-to-One)

---

## Search Functionality

Users can:

1. Select a Note Variety.
2. Submit the form.
3. Django validates the form.
4. The application searches the database using Django ORM.
5. Matching stores are displayed with their name and location.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project folder:

```bash
cd firstProject
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## purpose

This project was built as part of my Django learning journey to understand:

- Django architecture (MTV)
- Database relationships
- Django ORM
- Forms
- Request handling
- Template rendering
- Building dynamic web applications

---

## Author

**Zohaib Zulfiqar**
