# 🏡 Apex Properties

#### Deployed version: https://koprinkovapexproperties-fvamhchtcddqb0f9.italynorth-01.azurewebsites.net/

### A Django-based Web Application that allows users to view, buy and sell real-estate. Users can register, log in, browse featured content, create favourite lists, add comments and more. Moreover the application includes users with different rights, based on their permissions they have different privileges to use the site.

---

## General Requirements
- **Python**: Version 3.11.1 or higher  
- **PostgreSQL**: Database
- **pip**: For installing dependencies  
- **Browser**: Developed and tested using Microsoft Edge, Internet Explorer and Chrome. A Chromium-based browser is recommended but others probably work as well.
- **GIT**: Alternatively you can just download the source code.
- **Python Virtual Environment**: Optional, but recommended
---

## Setup Instructions

### Step 1: Clone the project
```bash
git clone https://github.com/Petar-Koprinkov/Real-Estate-Web-Application.git
```
And navigate to the root directory (`manage.py` level)
 ```bash
cd Real-Estate-Web-Application
```

### Step 2: Install Dependencies


Run the following command to install required Python libraries:
```bash
pip install -r requirements.txt
```

### Step 3: Create a `.env` File
At the root level of the project (where `manage.py` is located), create a `.env` file using this template:
```env

SECRET_KEY=your_secret_key
DEBUG=your_debug_option
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_postgres_user_password
DB_HOST=your_db_host
DB_PORT=your_db_port
CSRF_TRUSTED_ORIGINS=your_csrf_trusted_origins
ALLOWED_HOSTS=your_allowed_hosts
```

### Step 4: Database Migration
Run the following command to apply migrations:
```bash
python manage.py migrate
```

### Step 5: Run the app
Use this command to run the app:
```bash
python manage.py runserver
```

---

## Testing User Accounts

Pre-generated user accounts are provided for testing purposes:

| Role                 | Username        |  Password   |
|----------------------|-----------------|-------------|
| SuperUser            | admin           | nztiger69   |
| Investor             | investor        | nztiger69   |
| Broker               | broker          | nztiger69   |
| Seller               | seller          | nztiger69   |
| Buyer                | buyer           | nztiger69   |

---



## ✨ Features
### 🔐 Authentication
- **Register**: Users can register, providing Username, Password, Confirmation of the Password and Type of User(Buyer, Seller, Broker or Investor) - error messages are displayed if the values are not in the correct format.
- **Login**: Users can log in to their account after it has been created.
- **Logout**: Users can log out of their accounts after they have been logged in.


**Register:**

![register](https://github.com/user-attachments/assets/2e38d79d-f45c-452e-a453-681bc0a70e4e)


**Login:**

![login](https://github.com/user-attachments/assets/f6a8dbb5-27f6-4dd0-96d4-cd0198817dcb)

### 📌 Header
- **Navigation Buttons**:
  - **Create Location**: Redirects to the Form in which we create a location where the property will be located.
  - **Create Parking**: Redirects to the Form in which we create a parking space.
  - **Create Property**: Redirects to the Form in which we create a property.
  - **All Properties**: Allows users to view all properties in the website.
  - **Properties statistics**: Redirects to the `Properties statistics` page, but it is ONLY for users which user type is 'Investor'.

  - **User Authentication Buttons**:
    - **Login**: Displays a login button if the user is not logged in.
    - **Logout**: Allows users to log out.
    - **Register**: Allows users to make an registration in the website.

**Header when user is not logged in:**

![logout-nav](https://github.com/user-attachments/assets/adc6bccf-36ea-4b68-b45b-749992cf9942)


**Header when user is logged in:**

![login-nav](https://github.com/user-attachments/assets/f26cc664-50d7-41d0-96f2-59dc074241e0)



