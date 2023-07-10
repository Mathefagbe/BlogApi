**Blog API - Readme**
This repository contains a Django REST Framework-based API for managing blog posts. The API allows authenticated users to create, read, update, and delete blog post, as well as perform various operations related to user authentication and authorization.

## **Features**
* User Authentication: The API supports user registration, login, and logout using Knox token-based authentication.
* Blog Post CRUD: Users can create, retrieve, update, and delete blog posts.
* Pagination: The API supports paginated responses to efficiently handle large numbers of blog posts.
* searching post: Users can search posts based on the post title.
* Commenting: Users can add comments to blog posts.
* Permissions and Authorization: The API includes role-based permissions to control access to certain actions and resources.
* follower system: A users can follow eachother
## **Installation**
To run the Blog API locally, follow these steps:
* Clone the repository:
  `git clone https://github.com/your-username/blog-api.git`
* Navigate to the project directory:
  `cd blog-api`
* Create and activate a virtual environment:
  * for mac `python3 -m venv env source env/bin/activate`
  * for windows `python3 -m venv env env/scripts/activate`
* Install the project dependencies:
  `pip install -r requirement.txt`
* Apply database migrations:
  `python manage.py migrate`
* Create a super admin:
  `python manage.py createsuperuser`
  
## **API Documentation**
To explore and interact with the API endpoints, you can use the API documentation provided by the swagger. Once the server is running, visit `http://localhost:8000` or `http://localhost:8000/redoc/` in your web browser to access the documentation. Here, you can view the available endpoints, their request/response formats, and even test them interactively.




