# openapi_client.EncoderServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fonts_encodetext_post**](EncoderServiceApi.md#fonts_encodetext_post) | **POST** /fonts/encodetext | API endpoint to encode content


# **fonts_encodetext_post**
> EncodeResponse fonts_encodetext_post(encode_request)

API endpoint to encode content

Endpoint accepts text along with it's identifier from calling application, so that post encoding the text can be replaced. The 'data'  is a map of identifiers and text.

### Example

* OAuth Authentication (default):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: default
configuration = openapi_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EncoderServiceApi(api_client)
    encode_request = openapi_client.EncodeRequest() # EncodeRequest | 

    try:
        # API endpoint to encode content
        api_response = api_instance.fonts_encodetext_post(encode_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EncoderServiceApi->fonts_encodetext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encode_request** | [**EncodeRequest**](EncodeRequest.md)|  | 

### Return type

[**EncodeResponse**](EncodeResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

