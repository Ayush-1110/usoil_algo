
webhook_id = '23cd1e76-93ea-46c4-be39-1998f36a7959'
import requests
import json



def fetch_webhook_data():
    token_id = "23cd1e76-93ea-46c4-be39-1998f36a7959"
    headers = {"api-key": "ed286d4a-0074-4e62-9bae-a58a7eccfd00"}

    response = requests.get('https://webhook.site/token/' + token_id + '/requests?sorting=newest', headers=headers)

    if response.status_code == 200:
        requests_data = response.json()

        if requests_data:
            # print(json.dumps(requests_data['data'], indent=4))

            y = requests_data['data']
            # print(y)
            return y
        else:
            print('No requests received yet.')
    else:
        print('Error fetching webhook data:', response)

fetch_webhook_data()



