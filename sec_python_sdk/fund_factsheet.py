import requests
import json


class FundFactsheet():
    API_ENDPOINT = 'https://api.sec.or.th/FundFactsheet'

    api_key = ''

    def __init__(self, api_key=''):
        self.api_key = api_key

    def get_asset_management_companies(self):
        result = requests.get(
            url=f'{self.API_ENDPOINT}/fund/amc',
            headers={'Ocp-Apim-Subscription-Key': self.api_key}
        )
        return json.loads(result.text)

    def get_funds(self, asset_management_companies_unique_id=''):
        result = requests.get(
            url=f'{self.API_ENDPOINT}/fund/amc/{unique_id}',
            headers={'Ocp-Apim-Subscription-Key': self.api_key}
        )
        return json.loads(result.text)
