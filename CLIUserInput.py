import getpass
import re

import CLIOutput as out
import APIConnector as api


def get_domain():
    return input("Please enter the subdomain for your Zendesk Account ")


def get_email():
    email = input("Please enter the email address associated with your Zendesk Account ")
    flag = False
    while not flag:
        if email is not None and email.find(".") != -1 and email.find("@") != -1:
            return email

        else:
            email = input("Error: Incorrect email format. Please re-enter email ")


def get_password():
    return getpass.getpass("Please enter the password associated with your Zendesk Account ")


def password_access_error():
    print("Error: 403 - please check that the password access is enabled under channels "
          "-> API for your zendesk account.")
    print("Exiting program.")
    exit()


def domain_error():
    answer = input("Error: 404 - subdomain entered is incorrect. Would you like to try authentication again?\nEnter "
                   "'Y' for yes, any other key to exit ")

    auth_process(answer)


def other_error(code):
    print("Error:", code, '- problem with api connection.\nExiting program.')
    exit()


def authentication_error():
    answer = input("Error: 401 - authentication unsuccessful. Would you like to try authentication again?\nEnter 'Y' "
                   "for yes, any other key to exit ")

    auth_process(answer)


def auth_process(answer):
    if answer == 'Y' or answer == 'y':
        domain = get_domain()
        email = get_email()
        password = get_password()

        main_menu(api.get_tickets(domain, email, password))
        return

    else:
        print("Exiting program.")
        exit()


def sub_menu(ticket_list, curr_page):
    option_sub = input("Press N for next page, P for previous, M to go back to main menu")

    if option_sub != 'M' or option_sub != 'm':
        if option_sub == 'N' or option_sub == 'n':
            if curr_page < len(ticket_list['tickets']) // 25 + 1:
                curr_page += 1
                out.view_all_tickets(ticket_list, curr_page)
                sub_menu(ticket_list, curr_page)

            else:
                print("You are on the last page, you can't go forward any further.")
                sub_menu(ticket_list, curr_page)

        elif option_sub == 'P' or option_sub == 'p':
            if curr_page > 1:
                curr_page -= 1
                out.view_all_tickets(ticket_list, curr_page)
                sub_menu(ticket_list, curr_page)

            else:
                print("You are on the first page, you can't go back any further")
                sub_menu(ticket_list, curr_page)
    elif option_sub == 'M' or option_sub == 'N':
        main_menu(ticket_list)
    else:
        print("Error: Incorrect option.")
        sub_menu(ticket_list, curr_page)


def main_menu(ticket_list):
    curr_page = 1

    flag = 0
    while flag == 0:
        option = input(
            "What would you like to do?\n  A. View all tickets \n  B. Search for specific ticket \n  C. Quit ")

        if option == 'A' or option == 'a':
            out.view_all_tickets(ticket_list, curr_page)
            sub_menu(ticket_list, curr_page)

        elif option == 'B' or option == 'b':
            ticket_id = input("Please enter ticket ID ")
            out.view_specific_ticket(ticket_list, ticket_id)

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
