Udacity Item Catalog

A simple web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users have the ability to post, edit, and delete their own items.
Set Up

 

Skills used for this project :

Python
HTML
CSS
Bootstrap
Flask
Jinja2
SQLAchemy
OAuth
Facebook / Google Login



Run "For ubuntu users" :

- clone my repo into directory named catalog
- open your terminal and "cd" to where you clone or download the project -> cd [file]
- from the main directory run pip install -r requirements.txt
- Need to setup python3 and sublime or pycharm or any code tool use the "PEP8" style
- in terminal to run the main application  $python3 App.py
- Access and test your application by visiting http://localhost:5000 locally

*if first time running, you must add a category before adding an item


After the last command you are able to browse the application at this URL:

http://localhost:5000/

JSON endpoints

Returns JSON of all categories
/restaurants/JSON



Returns JSON of item
/restaurants/<int:restaurant_id>/menu/JSON


