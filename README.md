[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hLqvXyMi)


# UVA Textbook Rental App

## Overview

Welcome to the UVA Textbook Rental App – a student-friendly platform designed for UVA students to rent, buy, and sell used textbooks. This app provides a cost-effective way to access course materials while integrating features tailored to student needs.

## Example Login Accounts (for Grading)

- **Nemo Kim (Librarian)**
  - Username: Nemo_Kim
  - Password: clownfish2004

- **Nathan Kim (Patron)**
  - Username: Nathan_Kim
  - Password: clownfish2004

- **Steve (Patron)**
  - Username: Steve
  - Password: clownfish2004

## Features

### User Management
- **User Registration and Authentication:** 
  - Register with email/password or Google OAuth
  - Role-based access control (librarian/patron)
  - Profile management with customizable profile pictures
  - Password change functionality
  - Secure authentication system

### Book Management
- **Comprehensive Book Catalog:**
  - Detailed book information (title, author, ISBN, description)
  - Cover image and PDF file support
  - Book condition tracking (new, excellent, good, fair, poor)
  - Rental pricing and duration management

### Library Features
- **Librarian Dashboard:**
  - Add and edit books
  - Manage book inventory
  - Approve rental requests
  - User role management
  - Monitor library activity

- **Patron Features:**
  - Personal library management
  - Book rental system
  - Collection creation and management
  - Rating and review system
  - Rental history tracking

### Collections
- **Collection Management:**
  - Create personal book collections
  - Public and private collection options
  - Share collections with specific users
  - Add/remove books from collections
  - Browse other users' public collections

### Rental System
- **Smart Rental Management:**
  - Flexible rental durations
  - Automated rental expiration
  - Payment processing system
  - Rental status tracking (pending, active, expired)
  - Rental request approval workflow

### UI/UX Features
- **Modern Interface:**
  - Responsive design
  - User-friendly navigation
  - Real-time notifications
  - Search and filter functionality
  - Mobile-friendly layout

## Technical Stack

- **Backend:**
  - Django 4.2.19
  - Python 3.x
  - PostgreSQL (production) / SQLite (development)

- **Frontend:**
  - HTML5/CSS3
  - JavaScript
  - Bootstrap components
  - Custom responsive design

- **Authentication:**
  - Django Authentication System
  - Google OAuth integration
  - Custom user model with profiles

- **Storage:**
  - AWS S3 for media files (production)
  - Local storage (development)

- **Additional Tools:**
  - Django Allauth for social authentication
  - Pillow for image processing
  - Whitenoise for static files
  - Python dotenv for environment management

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

### Environment Setup

1. Clone the repository:
```bash
git clone [repository-url]
cd [project-directory]
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Create a `.env` file in the root directory with the following variables:
```
# Django Settings
SECRET_KEY=your_secret_key_here
DEBUG=True

# AWS Credentials (if using S3)
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name

# Google OAuth (if using social login)
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Initialize the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Start the development server:
```bash
python manage.py runserver
```

### Testing
Run the test suite:
```bash
python manage.py test
```

## Usage Guide

### For Librarians
1. Log in with librarian credentials
2. Access the Librarian Dashboard
3. Add new books with details and files
4. Manage rental requests and user roles
5. Monitor library activity

### For Patrons
1. Register or log in
2. Browse available books
3. Create collections
4. Rent books using the mock payment system
5. Manage rentals and view history

## Security Notes
- Mock payment system: Card numbers ending in odd digits (1,3,5,7,9) will fail
- Secure file handling for PDFs and images
- Role-based access control
- Protected API endpoints

## Contributions
- Haolin: Testing Manager
- Alden: Requirements Manger
- Nehemiah: Scrum Master
- Jayden: DevOps





