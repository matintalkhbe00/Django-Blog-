

# Django Blog

A Django project for a news website where users can post articles in various categories.

## Features

- User registration and login
- Users can post news articles
- Categorized posts
- List of posts displayed by category

## Prerequisites

- Python 3.x
- Django 3.x
- Other required packages are listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Django-Blog.git
   cd Django-Blog
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Migrate the database:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Open your web browser and go to `http://127.0.0.1:8000/`.
- You can register as a new user and, after logging in, post articles in various categories.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Brief description of changes"
   ```
4. Push your branch to your forked repository:
   ```bash
   git push origin feature-name
   ```
5. Create a Pull Request.


