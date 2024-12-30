# Quora-like Web Application

A Quora-like web application where users can ask questions, provide answers, follow spaces, and engage with the community.

## Features

- **User Authentication**: Sign up, log in, and log out functionality.
- **Question Management**: Users can ask questions with optional images.
- **Answer Management**: Users can answer questions and view answers.
- **Spaces**: Users can create and join spaces, which categorize questions.
- **Notifications**: Users receive notifications for new questions and answers.
- **Profile Management**: Users can view and edit their profile, see their questions and answers.
- **Responsive Design**: Mobile-friendly UI with icons for actions on smaller screens.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (for development), PostgreSQL/MySQL (for production)
- **Other**: Django REST Framework (if applicable), AWS S3 for media storage

## Setup

### Prerequisites

- Python 3.x
- Django
- Virtualenv (recommended)
- Node.js and npm (for frontend dependencies if any)
- PostgreSQL/MySQL (for production)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Setup the database:**

    - For SQLite (development):

        ```bash
        python manage.py migrate
        ```

    - For PostgreSQL/MySQL (production):
        - Update `DATABASES` in `settings.py`
        - Run migrations:

        ```bash
        python manage.py migrate
        ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Collect static files:**

    ```bash
    python manage.py collectstatic
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application:**
    Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- **Asking Questions**: Navigate to the "Ask a Question" section, fill out the form, and submit.
- **Answering Questions**: Navigate to a question and provide your answer in the answer form.
- **Managing Spaces**: Create and join spaces to categorize and find questions easily.
- **Notifications**: Stay updated with the latest questions and answers via notifications.
- **Profile Management**: View and edit your profile, including your questions and answers.

## Contact

- **Name**: Rahul Swami
- **Email**: rahull.in01@gmail.com
- **GitHub**: [rahullswami](https://github.com/rahullswami)

