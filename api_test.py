from yclients.api import YClients

BEARER = None
USER = None
COMPANY_ID = None
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {BEARER}, User {USER}',
  'Accept': 'application/vnd.yclients.v2+json',
}

yclients = YClients(bearer=BEARER, user=USER, company_id=COMPANY_ID)

for obj in yclients.get_services():
    print(f'{obj["title"]} ({obj["price_min"]}-{obj["price_max"]})')

    for staff_obj in obj['staff'][0]:
        staff_response = yclients.get_staff_info(staff_obj["id"])
        print(staff_response["name"])

    print("=" * 50)
