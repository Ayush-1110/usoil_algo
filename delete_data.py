import requests


def delete_data(delete_id,unique_id):
    headers = {"api-key": "ed286d4a-0074-4e62-9bae-a58a7eccfd00"}
    response = requests.delete('https://webhook.site/token/'+ unique_id +'/request/'+delete_id, headers=headers)
    print(response)

    # if response.status_code == 200:
    #     print("Request deleted successfully")
    # else:
    #     print(f"Failed to delete request: {response.status_code}")
# delete_data(delete_id,unique_id)




