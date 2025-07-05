# Blog Project

## Overview
This is a simple Django-based blog application that allows users to view posts, explore post details, and see posts by specific authors. The project uses Django's ORM to manage blog posts and authors, with templates for rendering content dynamically.

## Features
- **Post Listing**: Displays a list of all blog posts with their titles and publication dates.
- **Post Details**: Shows detailed information about a specific post, including its title, content, author, and publication date.
- **Author Posts**: Displays all posts written by a specific author.
- **Admin Interface**: Allows administrators to manage posts and authors via Django's admin panel.

## Project Structure
- **models.py**: Defines the `Author` and `Post` models.
  - `Author`: Stores author information (name and bio).
  - `Post`: Stores post details (title, content, publication date, and a foreign key to `Author`).
- **views.py**: Contains view functions to handle requests:
  - `post_list`: Displays all posts and authors.
  - `get_post_by_id`: Shows details for a specific post.
  - `get_posts_by_author_id`: Lists all posts by a specific author.
- **admin.py**: Registers the `Post` and `Author` models for management in the Django admin interface.
- **Templates**:
  - `post_list.html`: Renders the list of posts and authors.
  - `post_details.html`: Displays detailed information for a single post.
  - `authors_post.html`: Shows all posts by a specific author.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd blog_project
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000`.

## Usage
- **View Posts**: Navigate to `/` to see a list of all posts and authors.
- **View Post Details**: Access a specific post at `/post/<post_id>/`.
- **View Posts by Author**: See all posts by an author at `/author/<author_id>/`.
- **Admin Panel**: Log in at `/admin/` to manage posts and authors (create a superuser with `python manage.py createsuperuser`).

## Notes
- Ensure Django is installed and configured properly.
- The templates use Django's template language for rendering dynamic content.
- The `published_recently` method in the `Post` model checks if a post was published within the last 7 days.

## Future Improvements
- Add user authentication for post creation/editing.
- Implement pagination for post and author lists.
- Enhance templates with CSS styling and JavaScript for better user experience.
