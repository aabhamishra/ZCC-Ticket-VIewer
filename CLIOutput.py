import datetime
import calendar
from prettytable import PrettyTable


def view_all_tickets(tickets, page):
    print('PAGE ', str(page), ' OF ', str(len(tickets['tickets']) // 25 + 1) + ':\n')

    ticket_table = PrettyTable()

    ticket_table.field_names = ["Ticket ID", "Requester ID", "Subject", "Priority", "Created At"]

    for t in tickets['tickets'][(page - 1) * 25:page * 25]:
        created = datetime.date(int(t['created_at'][:4]), int(t['created_at'][5:7]), int(t['created_at'][8:10]))

        ticket_table.add_row(
            [t['id'], t['requester_id'], t['subject'][:20].rstrip() + ('...' if len(t['subject']) > 20 else ''),
             t['priority'],
             calendar.day_abbr[created.weekday()] + ", " + calendar.month_abbr[created.month] + " " + str(created.day) + " " +
             str(created.year)])
    print()
    print(ticket_table)
    return


def view_specific_ticket(tickets, ticket_id):

    for t in tickets['tickets']:
        if t['id'] == int(ticket_id):
            created = datetime.date(int(t['created_at'][:4]), int(t['created_at'][5:7]), int(t['created_at'][8:10]))
            print()
            print('Ticket ID:', str(t['id']), '| Requester ID:', str(t['requester_id']), '| Subject:', t['subject'][:20].rstrip() + ('...' if len(t['subject']) > 20 else ''), '| Priority:', t['priority'],
                  '| Created:', calendar.day_abbr[created.weekday()], calendar.month_abbr[created.month], str(created.day),
                  str(created.year))

            return

    print("Error: Ticket with entered ID does not exist.")
