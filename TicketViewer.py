# Main file for executing the program
# dependencies - CLIUserInput.py
# author - Aabha Mishra

import CLIUserInput as inp
import APIConnector as api

# Welcome message printed to console
print("~~~~~ Welcome to the Zendesk Ticket Viewer ~~~~~")

# authentication process
inp.auth_process('Y')
