import requests


class YClientsApiError(Exception):
    pass


class YClients:
    @staticmethod
    def _get_data_or_error(response):
        # TODO: read more about exceptions
        if not response["success"]:
            raise YClientsApiError(response["meta"]["message"])
        else:
            return response["data"]

    def __init__(self, bearer: str, user: str, company_id: int):
        self.bearer = bearer
        self.user = user
        self.company_id = company_id
        self._headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.bearer}, User {self.user}',
            'Accept': 'application/vnd.yclients.v2+json',
        }

    def get_services(self):
        response = requests.get(f'https://api.yclients.com/api/v1/company/{self.company_id}/services/', headers=self._headers).json()
        return self._get_data_or_error(response)

    def get_staff_info(self, staff_id: int):
        response = requests.get(f'https://api.yclients.com/api/v1/company/{self.company_id}/staff/{staff_id}/', headers=self._headers).json()
        return self._get_data_or_error(response)
