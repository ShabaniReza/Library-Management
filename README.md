# 📚 Online Library Management System

This project implements a comprehensive online library management system using Django and Django REST Framework. It provides functionalities for managing books, members, and borrowing records, along with a RESTful API for interaction.


## ✨ Features

* **Comprehensive Book Management:** Add, edit, delete, and view detailed information about books (including title, author, publisher, publication year, genres, total copies, available copies).
* **Member Management:** Register, edit, delete, and view member details (including name, membership ID, address, contact informations).
* **Borrowing & Return System:** Record book borrowing and return events, complete with dates.
* **Powerful RESTful API:** Access all data and operations through a well-defined API built with Django REST Framework, featuring:
    * **Built-in Permissions:** Utilizes Django REST Framework's permission classes to control access to API endpoints.
    * **Pagination:** Implements pagination for efficient handling and display of large datasets.
    * **Filtering:** Supports flexible data filtering based on various criteria.
    * **Searching:** Enables powerful search capabilities across specific fields.
* **Django Admin Panel:** A robust administrative interface for managing project data by library administrators.
* **Authentication system:** Authentication system built with Djoser library(JWT authentication backends).
* **Docker Integration:** Complete project packaging (including Django and MySQL) for easy setup and deployment in any environment.
* **MySQL Database:** Utilizes MySQL for data storage and management.
* **Git Version Control:** Tracks and manages code changes effectively using Git and GitHub.


## 🛠️ Technologies Used

* **Backend:**
    * Python
    * Django
    * Django REST Framework (DRF)
    * Django-filter
    * Djoser
    * Redis(Cache Backend, Message broker)
    * pytest
    * Locust(Performance testing)
* **Database:**
    * MySQL (using `mysqlclient`)
    * SQL
* **Containerization:**
    * Docker
    * Docker Compose
* **Version Control:**
    * Git


## 🚀 Installation & Setup

Follow these steps to get your project up and running:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/ShabaniReza/Library-Management.git
    cd Library-Management
    ```

3.  **Launch with Docker Compose:**
    ```bash
    docker-compose up
    ```
    This command builds and runs the Django and MySQL containers. It might take some time for the first build.

    This project uses MySQL image from docker hub . you have to setting up your MySQL image .

4.  **Project is Ready!**
    * **Django Admin Panel:** Access it at `http://localhost:8000/admin/`
    * **API Browsable Interface:** Explore the API at `http://localhost:8000/library/`