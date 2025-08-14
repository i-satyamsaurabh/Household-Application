# Household Services Hub 🏠

A robust, multi-user web application built with Flask that connects customers with skilled service professionals. This platform provides a seamless experience for managing, finding, and requesting various household services.

![Python](https://img.shields.io/badge/python-3.x-blue.svg) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-5-purple.svg?style=flat&logo=bootstrap&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=flat&logo=sqlite&logoColor=white) ![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Live Demo](#-live-demo)
- [Screenshots](#-screenshots)
- [Core Features](#-core-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Acknowledgments](#-acknowledgments)
- [License](#-license)

---

## 🌟 Project Overview

**Household Services Hub** is a full-stack web application designed to bridge the gap between customers seeking household help and professionals offering their services. Built as a part of the **Modern Application Development I (MAD1)** course at IIT, Madras, this project demonstrates a comprehensive understanding of database modeling, back-end development, and front-end design. The application supports three distinct user roles—**Admin**, **Professional**, and **Customer**—each with a dedicated dashboard and functionalities tailored to their needs.

---

## 🚀 Live Demo

> **Note**: A live demo link is not available yet. You can run the project locally by following the instructions below.

`[Link to your deployed application]`

---

## 📸 Screenshots

A quick look at the application's interface.

| **Admin Dashboard** | **Customer Service Search** |
| :---------------------------------------------------- | :-------------------------------------------------------- |
| `[Paste an image of your Admin Dashboard with charts]` | `[Paste an image of your Customer Service Search Page]`    |
| **Professional's Profile** | **Service Request Tracking** |
| `[Paste an image of a Professional's service page]`   | `[Paste an image of a Customer's service tracking status]` |

---

## ✨ Core Features

The application is built with a feature-rich, role-based access control system.

### 👑 Admin
- **Secure Login:** Dedicated and secure admin login.
- **Statistical Dashboard:** View platform analytics, including user registrations and service requests, visualized with pie and bar charts.
- **Service Management:** Add, update, or remove service categories (e.g., "Cleaning," "Plumbing").
- **Professional Vetting:** Approve or reject registrations from new service professionals.
- **User Management:** Oversee all users on the platform.

### 🛠️ Service Professional
- **Registration & Profile:** Sign up and create a detailed profile specifying skills, experience, and services offered.
- **Service Management:** Add personal service listings under predefined categories and set pricing.
- **Request Handling:** View and respond to service requests from customers.
- **Dashboard:** Track accepted jobs, earnings, and ratings.

### 👤 Customer
- **Easy Sign-up:** Quick and simple registration process.
- **Dynamic Search:** Search for services with filters based on category, location, and professional ratings.
- **Service Requests:** Send service requests directly to professionals.
- **Real-Time Tracking:** Monitor the status of service requests (e.g., "Pending," "Accepted," "Completed").
- **Profile Management:** Update personal information and view service history.

---

## ⚙️ Tech Stack

This project leverages a modern, lightweight technology stack for efficient development and deployment.

| Component           | Technology                               |
| :------------------ | :--------------------------------------- |
| **Backend Framework** | Flask                                    |
| **Database** | SQLite                                   |
| **ORM** | Flask-SQLAlchemy                         |
| **Templating Engine** | Jinja2                                   |
| **Frontend** | HTML5, CSS3, Bootstrap 5                 |
| **Database Design** | ERAlchemy                                |

---

## 🏗️ System Architecture

The application follows a modular architecture inspired by the Model-View-Controller (MVC) pattern.

-   **Model:** The data layer is managed by **SQLAlchemy**, defining the database schema for Users, Services, Requests, etc. The Entity-Relationship (ER) diagram was designed using **ERAlchemy**.
-   **View:** The presentation layer is handled by **Jinja2 templates**, rendered with dynamic data from the backend. **Bootstrap** ensures a responsive UI that works across all devices.
-   **Controller:** **Flask** acts as the controller, handling HTTP requests, processing business logic, interacting with the database, and rendering the appropriate templates.

### Database Schema
`[Paste an image of your ER Diagram]`
*The ER diagram illustrates the relationships between Users, Roles, Services, and Requests.*

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

-   Python 3.8+
-   PIP & Git

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/household-services-app.git](https://github.com/your-username/household-services-app.git)
    cd household-services-app
    ```

2.  **Create and activate a virtual environment:**
    -   **Windows:**
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    -   **macOS / Linux:**
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Initialize the database:**
    *(Add instructions here if you have a custom CLI command, e.g., `flask init-db`)*

5.  **Run the application:**
    ```sh
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

---

## 👨‍💻 Usage

Once the application is running, you can use the following dummy credentials to explore the different roles:

-   **Admin:**
    -   **Username:** `admin`
    -   **Password:** `admin123`
-   **Professional:**
    -   **Username:** `pro_user`
    -   **Password:** `pro123`
-   **Customer:**
    -   **Username:** `customer_user`
    -   **Password:** `customer123`

Feel free to register new accounts to test the full workflow.

---

## 📁 Project Structure
Of course. Here is the complete README file formatted in Markdown. You can copy and paste this directly into your README.md file on GitHub.

Markdown

# Household Services Hub 🏠

A robust, multi-user web application built with Flask that connects customers with skilled service professionals. This platform provides a seamless experience for managing, finding, and requesting various household services.

![Python](https://img.shields.io/badge/python-3.x-blue.svg) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-5-purple.svg?style=flat&logo=bootstrap&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=flat&logo=sqlite&logoColor=white) ![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Live Demo](#-live-demo)
- [Screenshots](#-screenshots)
- [Core Features](#-core-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Acknowledgments](#-acknowledgments)
- [License](#-license)

---

## 🌟 Project Overview

**Household Services Hub** is a full-stack web application designed to bridge the gap between customers seeking household help and professionals offering their services. Built as a part of the **Modern Application Development I (MAD1)** course at IIT, Madras, this project demonstrates a comprehensive understanding of database modeling, back-end development, and front-end design. The application supports three distinct user roles—**Admin**, **Professional**, and **Customer**—each with a dedicated dashboard and functionalities tailored to their needs.

---

## 🚀 Live Demo

> **Note**: A live demo link is not available yet. You can run the project locally by following the instructions below.

`[Link to your deployed application]`

---

## 📸 Screenshots

A quick look at the application's interface.

| **Admin Dashboard** | **Customer Service Search** |
| :---------------------------------------------------- | :-------------------------------------------------------- |
| `[Paste an image of your Admin Dashboard with charts]` | `[Paste an image of your Customer Service Search Page]`    |
| **Professional's Profile** | **Service Request Tracking** |
| `[Paste an image of a Professional's service page]`   | `[Paste an image of a Customer's service tracking status]` |

---

## ✨ Core Features

The application is built with a feature-rich, role-based access control system.

### 👑 Admin
- **Secure Login:** Dedicated and secure admin login.
- **Statistical Dashboard:** View platform analytics, including user registrations and service requests, visualized with pie and bar charts.
- **Service Management:** Add, update, or remove service categories (e.g., "Cleaning," "Plumbing").
- **Professional Vetting:** Approve or reject registrations from new service professionals.
- **User Management:** Oversee all users on the platform.

### 🛠️ Service Professional
- **Registration & Profile:** Sign up and create a detailed profile specifying skills, experience, and services offered.
- **Service Management:** Add personal service listings under predefined categories and set pricing.
- **Request Handling:** View and respond to service requests from customers.
- **Dashboard:** Track accepted jobs, earnings, and ratings.

### 👤 Customer
- **Easy Sign-up:** Quick and simple registration process.
- **Dynamic Search:** Search for services with filters based on category, location, and professional ratings.
- **Service Requests:** Send service requests directly to professionals.
- **Real-Time Tracking:** Monitor the status of service requests (e.g., "Pending," "Accepted," "Completed").
- **Profile Management:** Update personal information and view service history.

---

## ⚙️ Tech Stack

This project leverages a modern, lightweight technology stack for efficient development and deployment.

| Component           | Technology                               |
| :------------------ | :--------------------------------------- |
| **Backend Framework** | Flask                                    |
| **Database** | SQLite                                   |
| **ORM** | Flask-SQLAlchemy                         |
| **Templating Engine** | Jinja2                                   |
| **Frontend** | HTML5, CSS3, Bootstrap 5                 |
| **Database Design** | ERAlchemy                                |

---

## 🏗️ System Architecture

The application follows a modular architecture inspired by the Model-View-Controller (MVC) pattern.

-   **Model:** The data layer is managed by **SQLAlchemy**, defining the database schema for Users, Services, Requests, etc. The Entity-Relationship (ER) diagram was designed using **ERAlchemy**.
-   **View:** The presentation layer is handled by **Jinja2 templates**, rendered with dynamic data from the backend. **Bootstrap** ensures a responsive UI that works across all devices.
-   **Controller:** **Flask** acts as the controller, handling HTTP requests, processing business logic, interacting with the database, and rendering the appropriate templates.

### Database Schema
`[Paste an image of your ER Diagram]`
*The ER diagram illustrates the relationships between Users, Roles, Services, and Requests.*

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

-   Python 3.8+
-   PIP & Git

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/household-services-app.git](https://github.com/your-username/household-services-app.git)
    cd household-services-app
    ```

2.  **Create and activate a virtual environment:**
    -   **Windows:**
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    -   **macOS / Linux:**
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Initialize the database:**
    *(Add instructions here if you have a custom CLI command, e.g., `flask init-db`)*

5.  **Run the application:**
    ```sh
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

---

## 👨‍💻 Usage

Once the application is running, you can use the following dummy credentials to explore the different roles:

-   **Admin:**
    -   **Username:** `admin`
    -   **Password:** `admin123`
-   **Professional:**
    -   **Username:** `pro_user`
    -   **Password:** `pro123`
-   **Customer:**
    -   **Username:** `customer_user`
    -   **Password:** `customer123`

Feel free to register new accounts to test the full workflow.

---


## 📁 Project Structure

```plaintext
household-services-app/
├── app.py                  # Main Flask application file
├── models.py               # SQLAlchemy database models
├── requirements.txt        # Project dependencies
├── static/
│   ├── css/
│   └── js/
└── templates/
    ├── admin/              # Admin-specific templates
    ├── professional/       # Professional-specific templates
    ├── customer/           # Customer-specific templates
    ├── auth/               # Login, registration templates
    └── layout.html         # Base template



---

## 🙏 Acknowledgments

This project was developed as part of the Modern Application Development I (MAD1) course at the Indian Institute of Technology, Madras.  
Special thanks to the instructors and mentors for their invaluable guidance and continuous support throughout the project.

---

