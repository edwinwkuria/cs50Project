# cs50Project
#### Video Demo: https://youtu.be/CIUFLk5dG7Ucls
#### Description: 

A web url shortening application. The application takes input from the user in the form of a url string. Process it to generate a nine character url which is the short version. Upon visiting the link the user is promptly redirected to the longer url link. When the user tries to access a wrong url the request is rejected and an error page is shown.

*Technology stack: Python(Flask framework), SQLITE*
- venv : Python virtual enviroment that allows users to run the application on a windows enviroment. 
    * templates (HTML pages)
        - error.html : This is the page displayes to the user when the link they try to access is broken or does not exist in the database. This alerts the user that that link is broken.
        - index.html : This is the user landing page for the application.It contains a description and a text box for the user to enter the long url link. It has a button for the user to generate the shortened url. Upon clicking the button the response is processed and the long link displayed alongside the shortened url. In a card.
        - layout.html : Application layout page. This page contains the application layout. In the event there is need to have a menu bar or consistent stying. Used it to import bootstrap and other project relevant imports
    * main : The application logic main python file. This is the application main page it contains: Flask imports, SQL imports and random number generators imports. Get DB method checks the connetion to the Database and returns an instance of thae database. Querydb and insertdb methods are helper methods for querying and inserting data to the database. while appteardown does the sql cleanup. The generate random method uses an array of characters that can show up on the link, geneates random numbers equivalent to the string required and translates them using the array. The generated string if checked if it exists in the db which if it does the process repeats until a unique string is found. The index method is the main method and returns an empty page on GET and returns a page with the shortned url and the long url upon POST. The redirecttolongurl method on the other hand takes care of redirection after the user tries to access the short url link.  


Design choices: 
### Database 
I used sqlite because it is light weight considering the application does not have a lot of tables. It only has a urls table which has the short version and the long version of the submitted url. 

### Framework 
I used Flask for practise and its ease in creating a simple web application that only had two methods and ways to connect to the database. 

### Routing
The application does not have any authentication requirements on the routes as the application does not neet any user authentication or something of the sort. 

### Random digits
The application only uses letters in the short url as use of number can be confusing in as much as it adds to the number of urls that can be hosted without changing the application url length. Use of 8 unique characters allows for the storage of around 750 million urls with their short forms on the site. 


Set up application

1. Clone the repository from github 
`git clone https://github.com/edwinwkuria/cs50Project.git`
2. Change directory to the new directory 
`cd cs50Project`
3. Activate virtual enviroment
`venv\Scripts\activate`
4. Set the main application name in flask
`set FLASK_APP=main`
5. Run the application
`flask run`

