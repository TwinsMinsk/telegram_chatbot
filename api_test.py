import requests

BEARER = None
USER = None
COMPANY_ID = None

headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {BEARER}, User {USER}',
  'Accept': 'application/vnd.yclients.v2+json',
}

response = requests.get(f'https://api.yclients.com/api/v1/company/{COMPANY_ID}/services/', headers=headers)
for obj in response.json()["data"]:
    print(f'{obj["title"]} ({obj["price_min"]}-{obj["price_max"]})')

    for staff_obj in obj['staff'][0]:
        staff_response = requests.get(f'https://api.yclients.com/api/v1/company/{COMPANY_ID}/staff/{staff_obj["id"]}/', headers=headers).json()
        print(staff_response["data"]["name"])

    print("=" * 50)
