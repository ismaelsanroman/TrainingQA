import requests
import json
import jsonpath


class api_test:
    def __init__(self):
        self.api_flow()

    def weather(self):
        url = "https://www.metaweather.com/api/location/766273/2022/04/06"
        # url2 = data_api['url'] + data_api['argument'] + data_api['city']
        response = requests.get(url)
        json_response = json.loads(response.text)
        pages = jsonpath.jsonpath(json_response, 'weather_state_name')
        print(pages)

    def check_status(self):
        url = "https://www.metaweather.com/api/location/search/?query=Madrid"
        # url2 = data_api['url'] + data_api['argument'] + data_api['city']
        response = requests.get(url)
        print("- Código de respuesta:", response.status_code)
        assert response.status_code == 200

    def view_content(self):
        url = "https://www.metaweather.com/api/location/search/?query=Madrid"
        # url2 = data_api['url'] + data_api['argument'] + data_api['city']
        response = requests.get(url)
        print("- Texto:", response.text)
        assert len(response.text) >= 1

    def api_flow(self):
        print("--- Automatic API Rest Testing ---")
        print("----------------------------------")
        self.check_status()
        self.view_content()
        self.weather()

    def api_json(self):
        with open('./DataApi.json') as dataJson:
            data_api = json.load(dataJson)
        return data_api
