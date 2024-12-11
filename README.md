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


### 🏠 Home Page

![home page](https://github.com/user-attachments/assets/ac73e949-250f-41d1-9569-93b8dbcfc4f9)

- **Browse Listings**: View all properties.
- **Exclusive Properties**: View the three most expensive properties, which is exclusive.

### 🌐 All Properites Page

![all properties](https://github.com/user-attachments/assets/10199297-b2c5-4e23-bd72-c42f75e4c796)

- **Search Form**: You can search property by name.
- **List of Properties**: View all properties.
- **Pagination**: On one page there are only three properties.

### 📝 Details Property Page

![detail 1](https://github.com/user-attachments/assets/83ae434d-5ef9-484a-99f5-f874e7a6a2c0)
![detail 2](https://github.com/user-attachments/assets/09f8f8b8-a02e-40a6-a4d0-3aada29d1dd3)


- **Property Details**: You can see every detail of property - image, name, price, type, exposure, owner, floor, location, desription and is there parking.
- **Comment Section**: You can view all comments of other users in this section.
- **Comment Form**: Only if you are buyer or broker then you can comment the property.


### 📊 Properties Statistics Page

![properties statistics](https://github.com/user-attachments/assets/fcd83e0a-b247-4633-9dc9-ad135a07ea8a)

- **Statistic Table**: Only users which are Investors have permission to access this page

### 👤 Profile Page

![profile](https://github.com/user-attachments/assets/555d3869-3644-4f0f-aaea-ace34a04eb20)

- **Favourites**: The user can see which properties he has marked as favorites

### ☎️ Contact us (Footer)

![footer](https://github.com/user-attachments/assets/608fc795-452b-4843-b0ee-9d7cc225105a)


## ➕ API Endpoints

Swagger UI - **`/properties-api/`**

- **`api/properites/location_api`**: Fetch and filter all locations.  
- **`api/properites/parking-api`**: Fetch and filter all parkings.  
- **`api/properites/real_estate_api/`**: Fetch and filter all properties. 
- **`api/properites/profile_api`**: Fetch and filter all profiles. 




