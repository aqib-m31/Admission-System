# Admission-System
__A simple program that__:
* Tells user to install mysql server. And creates a database and defines the table structure in the database.
	> dbinit.py
* Provides four functions to user to manipulate student data in the database.
	* **enroll function** -- to insert student data into the database.
	* **view function** -- to view student data stored on the database.
	* **delete function** -- to delete details of a particular student from the database.
	* **update function** -- to update details of a particular student in the database.
	> admsys.py
##### dbinit.py:
1. *Tells user to install mysql server and setup the user account.*
2. *Asks user if mysql server is installed or not.*
3. *Determines whether user has installed mysql server or not - based on user input.*
4. *If installed, it asks for username and password to connect to the server.*
5. *On connecting successfully, it creates a database and defines the table structure in the database.*
6. *If this program doesn't generate any error message, **admsys.py** is ready to use.*
##### admsys.py
1. *Asks for username and password to connect to the server to get access to the database.*
2. *On connecting successfully, it provides the above mentioned functions viz. **enroll()**, **view()**, **delete()** and **update()** to the user to manipulate student data in the database.*
> Note: If you use this for the first time - firstly run dbinit.py and on successful execution you're ready to run admsys.py
