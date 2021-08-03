# Main file for executing the program
# dependencies - CLIUserInput.py
# author - Aabha Mishra

import CLIUserInput as inp
import APIConnector as api

# Welcome message printed to console
print("~~~~~ Welcome to the Zendesk Ticket Viewer ~~~~~")

domain = inp.get_domain()
email = inp.get_email()
password = inp.get_password()
tickets = api.get_tickets(domain, email, password)
inp.main_menu(tickets)