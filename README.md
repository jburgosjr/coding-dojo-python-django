# Coding Dojo Python (Django)
### Using python in a robust MTV (Model, Template, View) Framework

#### In this section we covered how python can be used to create full-scale web applications with the help of the Django.
#### Main concepts were:
* ##### What is an MVC framework?
* ##### What benefits would we gain by using an MVC or MTV framework?
* ##### Redirect to other routes
* ##### Render specific templates
* ##### Invoke methods attached to other pieces of our app that we characterize as models
* ##### Build database tables
* ##### Handle logic related to database operations, including validation


# Projects

* ##### Django App
  >- Familiarity with setting up a new Django project
  >- Familiarity with setting up a new Django app
  >- Familiarity with routing
  >- Familiarity with views and how to render a simple Http Response

* ##### Time Display
  > Create a Django app called time_display where the current time and date displays on localhost:3000
  >- Practice setting up a Django project
  >- Familiarity with passing data to a template
  
* ##### Random Word Generator
  > Create a new Django app called 'random_word'. Your template will show a random word with 14 characters in length.  
  > The first time you use this app, it should say 'attempt #1'. Each time you generate a new random keyword, it should increment the attempt figure. The purpose of this assignment is to reinforce your use of session  
  
  >- Practice setting up a Django project
  >- Familiarity with passing data to a template
  >- Familiarity with using Django session 
  
* ##### Survey Form
  > Build a Django application that accepts a form submission and presents the submitted data on a results page
  > Do NOT have a single URL handle BOTH the POST submission as well as the rendering of the html. In other words, never render on a post.  
  
  >- Start Django app from scratch
  >- Reinforce the important concepts you want to master
  >- Get you to build things a lot faster as each iteration will help you optimize your workflow
  
* #####  Session Words
  >- Create a new app called 'session_words'.
  >- Allow the user to add any new word to the session.  The user should be able to specify the color to display the word and whether the word should appear in bigger fonts.  The user should be able to clear the session as well.
  >- Show the words stored in the session on the right.
 
* ##### Ninja Gold
  >- Recreate the Ninja Gold game from Flask, but this time with Django.  Create this from scratch so that you can practice how to set up a new Django project
  
* ##### Dojo Ninjas/ Books Authors / Likes Books
  >- practice queries to Create, Read, Update, and Delete data
  >- practice one to one, one to many, and many to many relationships

* ##### Semi-restful Users
  > Create an app that can handle all of the CRUD operations (create, read, update and destroy) for a table.  Ensure that you add validation rules before saving the records in the database  
  >Have 7 routes
  >- GET request to /users - calls the index method to display all the users. This will need a template.
  >- GET request to /users/new - calls the new method to display a form allowing users to create a new user. This will need a template.
  >- GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template.
  >- GET /users/<id> - calls the show method to display the info for a particular user with given id. This will need a template.
  >- POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.
  >- GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.
  >- POST /users/update - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated. 
  
* ##### Amadon
  > You've decided to build your own e-commerce site called Amadon as a Django app.  Have your app store, in the database, all the items customers have ordered.  
  > Once your customer bought the item, Make sure your app doesn't charge the card again when the customer reloads the 'checkout' page ('checkout' page defined as localhost/amadon/checkout where they see a thank you message).
  
  >- Session and Post Handling
  >- Mixing post handling with html render - why this should be avoided
  >- Basic security - why you should be careful about what you put inside form tags
  
* ##### Login and Registration
  > Rebuild the Login and Registration assignment from the flask chapter, this time using Django.

  
  
