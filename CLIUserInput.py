import getpass
import re

import CLIOutput as out
import APIConnector as api
from prettytable import PrettyTable


# function to get subdomain name from user
def get_domain():
    return input("Please enter the subdomain for your Zendesk Account ")


# function to get email from user and verifying if the input format of the email is correct
def get_email():
    email = input("Please enter the email address associated with your Zendesk Account ")
    flag = False
    while not flag:
        if email is not None and email.find(".") != -1 and email.find("@") != -1:
            return email

        else:
            email = input("Error: Incorrect email format. Please re-enter email ")


# function to get the password related to the zendesk account
def get_password():
    return getpass.getpass("Please enter the password associated with your Zendesk Account ")


# function executed during a 403 error
def password_access_error():
    print("Error: 403 - please check that the password access is enabled under channels "
          "-> API for your zendesk account.")
    print("Exiting program.")
    exit()


# function executed during a 404 error
def domain_error():
    answer = input("Error: 404 - subdomain entered is incorrect. Would you like to try authentication again?\nEnter "
                   "'Y' for yes, any other key to exit ")

    auth_process(answer)


# function executed during a 401 error
def authentication_error():
    answer = input("Error: 401 - authentication unsuccessful. Would you like to try authentication again?\nEnter 'Y' "
                   "for yes, any other key to exit ")

    auth_process(answer)


# function executed for any other response from api which is not okay
def other_error(code):
    print("Error:", code, '- problem with api connection.\nExiting program.')
    exit()


# function executed to initiate authentication
def auth_process(answer):
    if answer == 'Y' or answer == 'y':
        domain = get_domain()
        email = get_email()
        password = get_password()

        tickets = api.get_tickets(domain, email, password)
        print("~~~~~ Welcome to the Zendesk Ticket Viewer ~~~~~")
        main_menu(tickets)
        return

    else:
        print("Exiting program.")
        exit()


# sub menu when user wants to view all tickets with options to go forward or back across pages, and handling
# circumstances where the user is on the first or last page
def sub_menu(ticket_list, curr_page):
    option_sub = input("Press N for next page, P for previous, M to go back to main menu")

    if option_sub != 'M' or option_sub != 'm':
        if option_sub == 'N' or option_sub == 'n':
            if curr_page < len(ticket_list['tickets']) // 25 + 1:
                curr_page += 1
                print(out.view_all_tickets(ticket_list, curr_page))
                sub_menu(ticket_list, curr_page)

            else:
                print("You are on the last page, you can't go forward any further.")
                sub_menu(ticket_list, curr_page)

        elif option_sub == 'P' or option_sub == 'p':
            if curr_page > 1:
                curr_page -= 1
                print(out.view_all_tickets(ticket_list, curr_page))
                sub_menu(ticket_list, curr_page)

            else:
                print("You are on the first page, you can't go back any further")
                sub_menu(ticket_list, curr_page)
    elif option_sub == 'M' or option_sub == 'N':
        main_menu(ticket_list)
    else:
        print("Error: Incorrect option.")
        sub_menu(ticket_list, curr_page)


# main menu with options to view all tickets, view specific tickets, and quit the program
def main_menu(ticket_list):
    curr_page = 1
    flag = 0
    while flag == 0:
        option = input(
            "What would you like to do?\n  A. View all tickets \n  B. Search for specific ticket \n  C. Quit ")

        if option == 'A' or option == 'a':
            print(out.view_all_tickets(ticket_list, curr_page))
            sub_menu(ticket_list, curr_page)

        elif option == 'B' or option == 'b':
            ticket_id = input("Please enter ticket ID ")
            print(out.view_specific_ticket(ticket_list, ticket_id))

            option_sub = input("Would you like to do something else? \nEnter 'Y' for yes, any other key to exit ")

            if option_sub == 'Y' or option_sub == 'y':
                main_menu(ticket_list)

            else:
                flag = 1

        elif option == 'C' or option == 'c':
            flag = 1

        else:
            print("Error: Incorrect option. Please re-enter command - A, B, or C ")

        if flag == 1:
            print("\n~~~~~ Thank you for using this program ~~~~~")
            exit()
