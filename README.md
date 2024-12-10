# 🏡 Apex Properties

#### Deployed version: https://koprinkovapexproperties-fvamhchtcddqb0f9.italynorth-01.azurewebsites.net/

### A Django-based Web Application that allows users to view, buy and sell real-estate. Users can register, log in, browse featured content, create favourite lists, add comments and more. Moreover the application includes users with different rights, based on their permissions they have different privileges to use the site.
### Recommended resolution on computer: 1920x1080
### Recommended resolution on phone: <600px

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



**Header when user is logged in:**


