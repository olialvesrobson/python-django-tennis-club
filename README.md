# Python Django Tennis Club

This is a Django-based web application for managing a tennis club. It includes features for managing members, scheduling matches, and tracking scores.

![Tennis Club](images/home_page.png)

## Features

- Member Registration and Management
- Match Scheduling
- Score Tracking
- User Authentication

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:olialvesrobson/python-django-tennis-club.git
    cd python-django-tennis-club
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin site:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Usage

### Member Registration and Management

Members can register on the site by filling out a registration form. Admins can manage member details through the Django admin interface.

Example:

```python
from django.contrib.auth.models import User

# Create a new user
user = User.objects.create_user('john', 'john@example.com', 'johnpassword')

# Update user details
user.first_name = 'John'
user.last_name = 'Doe'
user.save()
```

### Match Scheduling

Admins can schedule matches between members. Matches are stored in the database and can be viewed and managed through the admin interface.

Example:

```python
from .models import Match

# Schedule a new match
match = Match.objects.create(player1=user1, player2=user2, date='2024-07-08', time='15:00:00')
match.save()
```

### Score Tracking

Match scores can be recorded and tracked. Scores are associated with matches and can be viewed in the member profile and admin interface.

Example:

```python
from .models import Score

# Add score to a match
score = Score.objects.create(match=match, player=user1, points=6)
score.save()
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.
```

Replace `images/tennis_club.png` with the actual path to your image file. If the image is hosted online, you can directly use the URL in place of the file path.