# Django is a Python framework that makes it easier to create web sites using Python.

* Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and CRUD operations (Create Read Update Delete).


*  How does Django Work?
# Django works on MVT (Model - view- Template)
1. Model = Database (Data): Data from the database
    🔴store and manage data
    🔴Communicate with databse ( Mysql, PostgreSQ: , etc)
    <!-- In Django, the data is delivered as an Object Relational Mapping (ORM), which is a technique designed to make it easier to work with databases. -->
    <!-- The most common way to extract data from a database is SQL. One problem with SQL is that you have to have a pretty good understanding of the database structure to be able to work with it.

   <!-- Django, with ORM, makes it easier to communicate with the database, without having to write complex SQL statements. --> -->
   🔴 SQL: You go into the kitchen and cook the food yourself.
   🔴ORM: You tell the waiter what you want, and the waiter brings the food.

2. View = Middleman (Request Handler + Logic)
    🔴Receives the request (request)
    🔴Gets data from the Model
    🔴Sends data to the Template

3. Template = HTML page (UI) that shows the data
   🔴 The template displays the data received from the View.


# Django MVT Architecture
  User
   │
   ▼
 URL (urls.py) {Decides which View should run when a user visits a URL.}
   │
   ▼
 View (views.py)
   │
   ▼
 Model (models.py)
   │
 Database
   │
   ▼
  View
   │
   ▼
 Template (HTML)
   │
   ▼
Browser



# My First Project
* django-admin startproject Project_name
# Run the Django Project
* python manage.py runserver













