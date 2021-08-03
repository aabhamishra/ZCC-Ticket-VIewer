# ZCC-Ticket-VIewer

This program caters to viewing tickets on a Zendesk account keeping the following specifications in mind:
- Connect to the Zendesk API
- Request all the tickets for your account
- Display them in a list
- Display individual ticket details
- Page through tickets when more than 25 are returned


Usage Instructions
--------------------------------------

To run the program, all four source files need to be in the same folder along with the external libraries mentioned below. This program runs on the command line interface. Run "TicketViewer.py" in Python 3. Specifically, this program was developed and tested in Python 3.9. 

- On starting the program, a welcome message will be displayed after which do user will be prompted to enter their Zendesk subdomain, email, and password associated with their account. An API request will then be sent and any errors because of unsuccessful authentication, password access settings related to the account, or other issues will be handled and a descriptive message will be sent to the user before the program exits. However, in case of authentication issues, they will have the option to enter their credentials again for authentication.
- Upon successful authentication, the user will have the option to either view all tickets, search a ticket using the ticket ID, or exit the program. For all three options, the user can enter a case-insensitive input and have the command carried out.
- If the user decides to view their tickets, the first page of tickets will be displayed if there are more than 25. They will then have the option to traverse to the next or the previous page, whenever applicable. The sub menu also has the option to go back to the main menu when they are satisifed with the search. 
- The other option in the main menu is to search for a specific ticket. If the user selects this option, the program will ask for a ticket ID and will display the ticket associated with that given ID if it exists. If no ticket exists with the entered ID, an error message will be displayed. 
- In both the main menu and the sub menu, if the user enters an incorrect command, and error message will be displayed and they will have the option to input their choice again. 
- At any time while in the main menu, when the user wants to exit the program, they enter the required input and the program prints an exit message and ends.


Files Written by Me:
--------------------

- TicketViewer.py
- CLIUserInput.py
- CLIOutput.py
- APIConnector.py


External Libraries/Packages Used:
--------------------------------------

- requests
- getpass
- prettytable
