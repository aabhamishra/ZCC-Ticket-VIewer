import datetime
import calendar
from typing import Union, Any

from prettytable import PrettyTable


# function to view all tickets
def view_all_tickets(tickets, page):
    if page > len(tickets['tickets']) // 25 + 1:
        return 'Error: page number invalid'

    # if there are no ticket
    if len(tickets['tickets']) == 0 or tickets == {}:
        return "Error: No tickets exist with given account"

    # print details of 25 tickets according to page number through a PrettyTable
    else:
        print('PAGE ', str(page), ' OF ', str(len(tickets['tickets']) // 25 + 1) + ':\n')

        ticket_table = PrettyTable()

        ticket_table.field_names = ["Ticket ID", "Requester ID", "Subject", "Priority", "Created At"]

        for t in tickets['tickets'][(page - 1) * 25:page * 25]:
            created = datetime.date(int(t['created_at'][:4]), int(t['created_at'][5:7]), int(t['created_at'][8:10]))

            ticket_table.add_row(
                [t['id'], t['requester_id'], t['subject'][:20].rstrip() + ('...' if len(t['subject']) > 20 else ''),
                 t['priority'],
                 calendar.day_abbr[created.weekday()] + ", " + calendar.month_abbr[created.month] + " " + str(
                     created.day) + " " +
                 str(created.year)])

        return ticket_table


# view ticket given the ID of the ticket. Display error if no ticket is found with that ID.
def view_specific_ticket(tickets, ticket_id):
    for t in tickets['tickets']:
        if t['id'] == int(ticket_id):
            created = datetime.date(int(t['created_at'][:4]), int(t['created_at'][5:7]), int(t['created_at'][8:10]))
            subject = t['subject'][:20].rstrip()
            if len(t['subject']) > 20:
                subject = subject + '...'

            str_var: Union[str, Any] = 'Ticket ID:' + str(t['id']) + ' | Requester ID:' + str(
                t['requester_id']) + ' | Subject:' + subject + ' | Priority:' + str(
                t['priority']) + ' | Created: ' + str(calendar.day_abbr[created.weekday()]) + " " + str(
                calendar.month_abbr[created.month]) + " " + str(created.day) + " " + str(created.year)

            return str_var

    return "Error: Ticket with entered ID does not exist."

