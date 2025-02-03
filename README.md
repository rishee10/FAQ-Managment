## FAQ-Managment

This project is a FAQ management system that supports multilingual FAQs, allowing users to add, edit, delete and retrieve FAQs in multiple languages. It uses Django with the `django-ckeditor` WYSIWYG editor, Google Translate API for automatic translations, Redis caching for improved performance, and a REST API to manage the FAQ entries.

## Project Overview
This Django-based FAQ management system allows users to create and manage FAQs with support for multiple languages. The FAQ entries are stored in a database and translated using Google Translate API. A caching mechanism using Redis is implemented to store translations for better performance.

## Key Features:
- **Multilingual Support:** FAQs can have language-specific translations.
- **WYSIWYG Editor:** Users can format FAQ answers using the `django-ckeditor` editor.
- **REST API:** A RESTful API to create, retrieve, update, and delete FAQs.
- **Caching with Redis:** Translations are cached to improve performance.
- **Admin Panel:** A user-friendly interface to manage FAQs.

## Installation Instructions
Clone the project repository to your local machine:

```git clone https://github.com/rishee10/FAQ-Managment ```

``` cd myproject ```

Create a Virtual Environment

``` python -m venv venv ```

Activate the Virtual Environment

``` venv\Scripts\activate ```

Install Dependencies

Install the required Python packages listed in the requirements.txt file:

``` pip install -r requirements.txt ```

Apply Database Migrations

Run database migrations to set up your database schema:

``` python manage.py migrate ```

Create a Superuser (Optional)

Create a superuser if you want to access the Django admin panel:

``` python manage.py createsuperuser ```

Run the Development Server
Start the development server to run the project locally:

``` python manage.py runserver ```

You can now access the application

## API Usage

### Web Interface Usage

Once the project is up and running, you can access the FAQ management through the web interface:

-**List all FAQs:** Navigate to http://127.0.0.1:8000/ to view the list of FAQs.

-**Create a new FAQ:** Visit http://127.0.0.1:8000/faqs/create/ to create a new FAQ entry.

-**View FAQ details:** Click on any FAQ to view more details at http://127.0.0.1:8000/faqs/{id}/.

-**Update an FAQ:** Visit http://127.0.0.1:8000/faqs/{id}/update/ to edit an FAQ.

-**Delete an FAQ:** Visit http://127.0.0.1:8000/faqs/{id}/delete/ to delete an FAQ.



## Contribution Guidelines

We welcome contributions! To contribute, please follow these steps:

#### Fork the Repository
   
Start by forking the repository to your own GitHub account.

#### Create a Branch

Create a new branch for your feature or bugfix:


``` git checkout -b feature-name ```

#### Make Your Changes

Make the necessary changes or additions to the codebase.

#### Commit Your Changes

Commit your changes with a descriptive commit message:


``` git commit -m "Add feature X" ```

#### Push Your Changes

Push your changes to your forked repository:

``` git push origin feature-name ```

#### Open a Pull Request

Open a pull request from your forked repository to the main repository. Be sure to explain the changes you’ve made in the pull request description.


