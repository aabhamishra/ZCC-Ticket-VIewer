import requests
from requests.auth import HTTPBasicAuth
import CLIUserInput as inp


# api connection class for sending http requests to zendesk and recieve response
def get_tickets(domain, email, password):
    # Set the request parameters
    global data
    url = 'https://' + domain + '.zendesk.com/api/v2/tickets.json'

    # Do the HTTP get request
    response = requests.get(url, auth=(email, password))

    # Check for HTTP codes other than 200 as successful response for GET and PUT is 200
    if response.status_code == 403:
        data = None
        inp.password_access_error()

    if response.status_code == 401:
        data = None
        inp.authentication_error()
        return
    if response.status_code == 404:
        data = None
        inp.domain_error()
        return
    if response.status_code != 200:
        data = None
        inp.other_error(response.status_code)

    if response.status_code == 200:

        # Decode the JSON response into a dictionary and use the data
        data = response.json()

        # to get all tickets
        while data['next_page'] is not None:
            url = data['next_page']
            response = requests.get(url, auth=(email, password))
            data_next = response.json()
            data['tickets'] += data_next['tickets']
            data['next_page'] = data_next['next_page']

        return data

