cat << 'EOF' > README.md
# 🍽️ Food Ordering App (Django)

A Django-based restaurant menu application that displays categorized menu items with pricing, availability status, and detailed views for each item.

Built using:
- Python
- Django
- Bootstrap 5
- SQLite

---

## 📌 Features

- Categorized menu (Starters, Salads, Main Dishes, Desserts)
- Dynamic grouping using Django template logic
- Detail page for each menu item
- Status handling (Available / Unavailable)
- Bootstrap styling with list groups and badges
- Template inheritance using base.html
- Django Class-Based Views (ListView & DetailView)

---

## 🗂 Project Structure

50_Food_Ordering_App_with_Django/
│
├── manage.py
├── db.sqlite3
│
├── mysite/
│   └── settings.py
│
├── restaurant_menu/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
└── templates/
    ├── base.html
    ├── index.html
    └── menu_item_detail.html

---

## 🧠 Models

### MenuItem

Fields:
- meal (CharField)
- description (CharField)
- price (DecimalField)
- meal_type (ChoiceField)
- status (Available / Unavailable)
- author (ForeignKey to User)

---

## 🧭 Views

### MenuListView
- Displays categorized menu
- Uses Django ListView
- Passes MEAL_TYPE to template context

### MenuItemDetailView
- Displays individual menu item
- Uses Django DetailView

---

## 🚀 Installation

### 1️⃣ Clone the repository

git clone <your-repo-url>
cd 50_Food_Ordering_App_with_Django

### 2️⃣ Create virtual environment

python -m venv venv
source venv/bin/activate  (Mac/Linux)
venv\Scripts\activate     (Windows)

### 3️⃣ Install dependencies

pip install django

### 4️⃣ Apply migrations

python manage.py migrate

### 5️⃣ Create superuser (optional)

python manage.py createsuperuser

### 6️⃣ Run server

python manage.py runserver

Visit:
http://127.0.0.1:8000/

---

## 🎯 Future Improvements

- Add ordering/cart functionality
- Add user authentication
- Improve UI styling
- Add search and filtering
- Deploy to production (Render / Heroku)

