# MentorMate FastAPI Cookiecutter Template

This FastAPI Cookiecutter template provides a predefined project structure based
on the company's perspective. It is designed to kickstart FastAPI projects with
a well-organized layout and includes common functionality that aligns with the
company's development practices. This template requires Python >=3.11 and
installed cookiecutter package to streamline the project setup process.

## Requirements

Before using this template, make sure you have the following requirements met:

1. **Python 3.11**: Ensure that you have Python 3.11 installed on your
   development machine. You can download the latest version from the official
   Python website: [python.org](https://www.python.org/downloads/)

2. **Cookiecutter**: Install Cookiecutter globally on your system. Cookiecutter
   is a command-line utility that creates projects from project templates. To
   install Cookiecutter, run the following command:

   ```shell
   pip install cookiecutter
   ```

## Usage

To generate a new Django project using this Cookiecutter template, follow these
steps:

1. Open a terminal or command prompt.

2. Change to the directory where you want to create your project.

3. Run the following command, replacing `project-name` with the desired name of
   your project:

   ```shell
   cookiecutter https://github.com/gp-mentormate/django-cookiecutter-template
   ```

   This command will initiate the project generation process.

4. You will be prompted to enter some details such as project name, author
   name, and other relevant information. Fill in the required information as
   prompted.

5. Once you've provided all the required information, Cookiecutter will create
   the project structure based on the template and generate the necessary
   files.

6. Navigate to the newly created project directory:

   ```shell
   cd project-name
   ```

   **Note:** Cookiecutter has automatically created a virtual environment for
   your project and installed the necessary dependencies. You don't need to
   create a separate virtual environment or install dependencies manually.

   You can choose to run the project using either Docker Compose or as a
   standard Django application from the terminal.

    - To start the project with Docker Compose, ensure that Docker is installed
      on your machine. Then, run the following command:

      ```shell
      docker-compose up
      ```

      This will build the Docker containers and start the project.

    - Alternatively, if you prefer to run the project as a standard Django
      application from the terminal, use the following command:

      ```shell
      python manage.py runserver
      ```

      This command will start the Django development server, and you can access
      the application by
      visiting [http://localhost:8000/](http://localhost:8000/) in your web
      browser.

   Choose the method that best fits your development environment and
   requirements.