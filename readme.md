Songaniser is a full stack Python application built using the flask framework, this project was completed in one week as a solo project during the python module of the CodeClan bootcamp course.

Technologies used during this project:

Python
Flask
Git
Postico
Jinja
Psycopg2
SQL
HTML
CSS
TDD

![plot](./../../../pda_work/project%20information/App%20Home%20Page.png)

The intent of this application was to allow me to better organise the songs I need to learn for the band I am in, we gig regularly and often learn new songs but keeping on top of this can be challenging, as there is no easy way to keep track of each song. 

With this intent in mind, the application allows users to add songs, add bands and add setlists. And thus there are four different tables in the database: songs, bands, setlists, and setlist songs. This was something that became more complex than I expected as I was building the project, the need for a many to many relationship between songs and setlists required a whole new model and repository to be built, something I had not foreseen.

The aspect of this project I was the proudest of is the search bar. I had an initial idea in my head of how I could go about implementing this, but which I was not entirely sure that it would work out. Through trial and error I eventually managed to make it work, and of course this was very satisfying in the end. It does have a few issues and could be implemented more effectively, but for a first attempt at implementing a search bar, I was happy with how I did.

