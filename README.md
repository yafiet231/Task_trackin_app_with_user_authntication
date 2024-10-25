# Webstack - Portfolio Project

## task_tracking_with_user_authentication_app
### Table of Content

* [Project inspiration](#Project-inspiration)
* [Live Demo](#Live-Demo)
* [Technologies](#Technologies)
* [Install Dependencies](#install dependencies)
 [How to Use](#How-to-Use)
* [Contributing](#Contributing)
* [Project Blog](#Project-Blog)
* [Authors](#Authors)
* [Licensing](#Licensing)
* [Future Development](#Future-Development)
* [Screenshots](#Screenshots)
* [features](#features)

### Project Inspiration

-    Personal Productivity: The need for a reliable tool to manage daily tasks and maintain organization.
-    Open-Source Community: Contributing to a growing ecosystem of productivity apps and sharing knowledge.

### Live Demo
* [Live Demo](https://www.youtube.com/watch?v=GWKPiIitjeE)

Introduction
This README outlines the To-Do List application, a web-based tool designed to help users organize and manage their tasks efficiently. 
Built using the Django web framework, the application provides a user-friendly interface for creating, editing, and deleting tasks.

**Installation**

Clone the Repository:
https://github.com/yafiet231/Task_trackin_app_with_user_authntication

Create a Virtual Environment (Optional):
   python -m venv venv
**source venv/bin/activate**
**On Windows: venv\Scripts\activate**

3. **Install Dependencies:**

pip install django   
pip install -r requirements.txt   

**Run Database Migrations:**
python manage.py makemigrations
python manage.py migrate

**Start the Development Server:**
python manage.py runserver   

**Usage**

-    Access the Application: Open your web browser and navigate to http://127.0.0.1:8000/.
-    Create an Account: Click the "Register" button and provide your login credentials.
-    Log In: Enter your username and password to access your account.
-    Add a Task: Click the "Add Task" button and enter the task title and description.
-    Delete a Task: Click the "Delete" button next to the task you want to remove.
-    Log Out: Click the "Logout" button to end your session.

**Technologies**

-    Backend: Django
-    Database: SQLite
-    Frontend: HTML, CSS

**Authentication:**

-    Register and Login
-    Register and log in as a user.

Create a superuser account (for admin access)
   ```bash
     python manage.py createsuperuser
   
-    Start the development server:
   ```bash
     python manage.py runserver
   
-   Open your web browser and go to http://localhost:8000 to access the Todo_List Django Web App.

![](https://github.com/yafiet231/Task_trackin_app_with_user_authntication/blob/master/images/Capture1.PNG)
![](https://github.com/yafiet231/Task_trackin_app_with_user_authntication/blob/master/images/Capture2.PNG)

![](https://github.com/yafiet231/Task_trackin_app_with_user_authntication/blob/master/images/Capture3.PNG)
![](https://github.com/yafiet231/Task_trackin_app_with_user_authntication/blob/master/images/Capture4.PNG)
![](https://github.com/yafiet231/Task_trackin_app_with_user_authntication/blob/master/images/capture5.PNG)

## Features

The Todo_List Django Web App offers the following features:

- **Task Management**: Easily add, edit, and delete tasks.
- **Task Prioritization**: Assign priority levels to tasks.
- **Task Categorization**: Divide tasks in different categories.
- **Task Reminder**: Send Email to user for specific tasks.
- **User Authentication**: Secure account management (signin,signup,forgot password).
- **Admin Dashboard**: Access admin dashboard [http://localhost:8000/todo-admin/](http://localhost:8000/todo-admin/) 
to manage users and tasks.
- **Profile Managemet**: View/Change user details.
- **Export Task Details**: export file to csv if needed.
- **Dark Mode**: Trigger Dark theme for awesome experience.

## Contributing

We welcome contributions to improve the Todo_List Django Web App. If you'd like to contribute, please follow these guidelines:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and test them thoroughly.

4. Submit a pull request with a clear description of your changes.

5. Ensure your code follows best practices and includes necessary tests if applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
