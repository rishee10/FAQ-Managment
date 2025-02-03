# FAQ-Managment

This project is a FAQ management system that supports multilingual FAQs, allowing users to add, edit, delete and retrieve FAQs in multiple languages. It uses Django with the `django-ckeditor` WYSIWYG editor, Google Translate API for automatic translations, Redis caching for improved performance, and a REST API to manage the FAQ entries.

## Project Overview
This Django-based FAQ management system allows users to create and manage FAQs with support for multiple languages. The FAQ entries are stored in a database and translated using Google Translate API. A caching mechanism using Redis is implemented to store translations for better performance.

### Key Features:
- **Multilingual Support:** FAQs can have language-specific translations.
- **WYSIWYG Editor:** Users can format FAQ answers using the `django-ckeditor` editor.
- **REST API:** A RESTful API to create, retrieve, update, and delete FAQs.
- **Caching with Redis:** Translations are cached to improve performance.
- **Admin Panel:** A user-friendly interface to manage FAQs.

## Installation Instructions
 Clone the project repository to your local machine:
Copy
git clone https://github.com/yourusername/projectname.git
cd projectname
