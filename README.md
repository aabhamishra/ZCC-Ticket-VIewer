# ZCC-Ticket-VIewer

This program caters to viewing tickets on a Zendesk account keeping the following specifications in mind:
- Connect to the Zendesk API
- Request all the tickets for your account
- Display them in a list
- Display individual ticket details
- Page through tickets when more than 25 are returned


Usage Instructions and Program Details
--------------------------------------

To run the program, all four source files need to be in the same folder along with the external libraries mentioned below. This program runs on the command line interface. Run "TicketViewer.py" in Python 3. Specifically, this program was developed and tested in Python 3.9. 

- On starting the program, a welcome message will be displayed after which do user will be prompted to enter their Zendesk subdomain, email, and password associated with their account. An API request will then be sent and any errors because of unsuccessful authentication, password access settings related to the account, or other issues will be handled and a descriptive message will be sent to the user before the program exits. However, in case of authentication issues, they will have the option to enter their credentials again for authentication.
- Upon successful authentication, the user will have the option to either view all tickets, search a ticket using the ticket ID, or exit the program. For all three options, the user can enter a case-insensitive input and have the command carried out.
- If the user decides to view their tickets, the first page of tickets will be displayed if there are more than 25. They will then have the option to traverse to the next or the previous page, whenever applicable. The sub menu also has the option to go back to the main menu when they are satisifed with the search. 
- The other option in the main menu is to search for a specific ticket. If the user selects this option, the program will ask for a ticket ID and will display the ticket associated with that given ID if it exists. If no ticket exists with the entered ID, an error message will be displayed. 
- In both the main menu and the sub menu, if the user enters an incorrect command, and error message will be displayed and they will have the option to input their choice again. 
- At any time while in the main menu, when the user wants to exit the program, they enter the required input and the program prints an exit message and ends.
- The test class developed through built in unittest included in the project checks for erroneous outputs and error handling due to API connection problems or ticket viewing


Limitations (with testing):
--------------------

-  I have implemented tests to my best current ability and have tried to check for glaring exception and important errors in the program especially during specific ticket viewing. However, most of my program functions return string values and formatted tables for displaying the menus, and viewing tickets. I have not been able to fully grasp how to check for potential erroneous outputs in cases when the data is directly printed to the console, and while I understand the theory of mock objects in testing, I have not been able to implement those to check for nested function calls especially in the case of authentication errors. 
-  Additionally, I was unable to check if the viewing function for all tickets worked as it should within page limitations as my output was in the form of a formatted table using an external module.


Overcoming limitations (with testing):
--------------------

- For future projects like this one, I would implement testing using mock objects and patches. 
- I would learn how to better test output which have been formatted with external modules e.g. prettytable


Files Written by Me:
--------------------

- TicketViewer.py
- CLIUserInput.py
- CLIOutput.py
- APIConnector.py
- TestTicketViewer.py


External Modules/Imports Used:
--------------------------------------

- requests
- getpass
- prettytable
- datetime
- calendar
- unittest
