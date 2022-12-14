import os
from requests import Session
import logging
import curlify
import allure


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    @allure.step('{method} {url}')
    def request(self, method, url, **kwargs):
        response = super().request(method, url=f'{self.base_url}{url}', **kwargs)
        message = curlify.to_curl(response.request)
        logging.info(f'cURL: {message}\n')
        logging.info(f'Response: {response.json()}\n')
        allure.attach(
            body=message.encode('utf8'),
            name=f'Request {method}',
            attachment_type=allure.attachment_type.TEXT,
            extension='txt'
        )
        allure.attach(
            body=str(response.json()).encode('utf-8'),
            name='Response',
            attachment_type=allure.attachment_type.TEXT,
            extension='txt'
        )
        return response


def req_session() -> BaseSession:
    api_url = os.getenv('APIURL')
    return BaseSession(base_url=api_url)



