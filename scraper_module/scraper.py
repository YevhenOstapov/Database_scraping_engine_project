import re

import requests

from config import HEADERS


class Scraper:

    def __init__(self, url_addr):
        self.url_addr = url_addr
        self.regular_expression = [r".*?minute.+", r".*?hour.+", "yesterday"]
        self.page_counter = 10

    @property
    def all_data(self) -> list:
        list_data = []
        while True:
            url_ = self.url_addr.format(str(self.page_counter))
            response = requests.request("GET", url_, headers=HEADERS).json()
            if not response:
                break
            list_data.extend(response)
            self.page_counter += 10
        return list_data

    @property
    def current_data(self) -> list:
        self.page_counter = 10
        list_data = []
        while True:
            url_ = self.url_addr.format(str(self.page_counter))
            response = requests.request("GET", url_, headers=HEADERS).json()
            if not response:
                return list_data
            else:
                for element in response:
                    if self.get_recent_date(element.get("time_ago")):
                        list_data.append(element)
                    else:
                        return list_data
                self.page_counter += 10

    def get_recent_date(self, element):
        for match in self.regular_expression:
            if re.search(match, element):
                return True
