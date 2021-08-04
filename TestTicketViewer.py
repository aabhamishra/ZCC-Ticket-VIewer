import unittest
import CLIUserInput as inp
import APIConnector as api
import CLIOutput as out
import requests


# test class for api connection and ticket viewing functions
class MyTestCase(unittest.TestCase):

    # checks user credentials and ascertain that when the input is as expected, the ticketList returned is not None
    def test_credentials(self):
        # trying to get response from correct request with status code 200

        tickets = api.get_tickets('zccamishra', 'aabhamishra.2002@gmail.com', 'Aabha.2002')

        self.assertIsNotNone(tickets, 'Error: on successful authentication, the tickets returned should not be None')
        self.assertEqual(len(tickets['tickets']), 101, 'Error: there should be 101 tickets')

    # checks for domain name error while authenticating
    def test_false_credentials(self):
        # Changing password so the url will result 401 or 400
        response = requests.get(
            "https://zccamishra.zendesk.com/api/v2/tickets.json", auth=(
                "aabhamishra.2002@gmail.com", "Aabha.2001"))

        self.assertEqual(response.status_code, 401 or 400)

    # test to check specific ticket when it exists
    def test_specific_ticket_present(self):
        tickets = api.get_tickets('zccamishra', 'aabhamishra.2002@gmail.com', 'Aabha.2002')
        expectedOutput = out.view_specific_ticket(tickets, '2')
        actualOutput = "Ticket ID:2 | Requester ID:1900298651524 | Subject:velit eiusmod repreh... | Priority:None | Created: Tue Aug 3 2021"

        self.assertEqual(expectedOutput, actualOutput, 'Error: specific ticket displaying method erroneous when ticket '
                                                       'exists')

    # test to check specific ticket when it does not exist
    def test_specific_ticket_not_present(self):
        tickets = api.get_tickets('zccamishra', 'aabhamishra.2002@gmail.com', 'Aabha.2002')
        expectedOutput = out.view_specific_ticket(tickets, '1111')
        actualOutput = "Error: Ticket with entered ID does not exist."

        self.assertEqual(expectedOutput, actualOutput, 'Error: specific ticket displaying method erroneous when ticket '
                                                       'does not exist')

    # test to check all tickets function when page is invalid
    def test_all_tickets(self):
        tickets = api.get_tickets('zccamishra', 'aabhamishra.2002@gmail.com', 'Aabha.2002')
        actualOutputOne = out.view_all_tickets(tickets, 7)
        expectedOutputOne = 'Error: page number invalid'

        self.assertEqual(expectedOutputOne, actualOutputOne, 'Error: all ticket displaying method erroneous for '
                                                             'invalid page')


# run all tests
if __name__ == '__main__':
    unittest.main()
