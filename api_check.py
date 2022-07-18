from __future__ import print_function

import json

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
import requests
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

client_id = "Wlg83aZykTI9P3oSpjzHN7aIPmYa"
client_secret = "KpWB1kmajGhMLaPm2AOgHZAV2c0a"


def get_access_token(url, client_id, client_secret):
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    )
    return response.json()["access_token"]


# Configure OAuth2 access token for authorization: default
configuration = openapi_client.Configuration(
    host="https://developer.dev.securely.direct/gateway/u/v1"
)
configuration.access_token = get_access_token("https://developer.dev.securely.direct/gateway/token", client_id, client_secret)


def initialize_font_id():
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.EncoderServiceApi(api_client)
        encode_request = openapi_client.EncodeRequest(
            data={
                "text": "initialize"
            },
            # scopes=[
            #     {
            #       "name": "SESSION",
            #       "value": "6QfmF0rWLiPcbu57g785FX6ZlOca"
            #     }
            # ]
        )  # EncodeRequest |


        try:
            a = api_instance.fonts_encodetext_post(encode_request)
            print(f"RESPONSE ENCRYPT = {a}")
            return f'U_{a.font_identifier}'
        except ApiException as e:
            print("Exception when calling DefaultApi->glyphs_encodetext_post: %s\n" % e)


def get_encrypted(text):
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.EncoderServiceApi(api_client)
        encode_request = openapi_client.EncodeRequest(
            data={
                "text": text
            },
            # scopes=[
            #     {
            #       "name": "SESSION",
            #       "value": "6QfmF0rWLiPcbu57g785FX6ZlOca"
            #     }
            # ]
        )  # EncodeRequest |


        try:
            a = api_instance.fonts_encodetext_post(encode_request)
            print(f"RESPONSE ENCRYPT = {a}")
            return a.data["text"]
        except ApiException as e:
            print("Exception when calling DefaultApi->glyphs_encodetext_post: %s\n" % e)

if __name__ == "__main__":
    print(get_encrypted("Hello World"))