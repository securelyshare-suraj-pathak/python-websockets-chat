# ApiError

Response in case of error
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Attribute name that caused the error. | [optional] 
**code** | **int** | Error code | [optional] 
**debug_message** | **str** | Error detailed message for debug operations | [optional] 
**http_status** | **str** | HTTP Status | [optional] 
**message** | **str** | Error message | [optional] 
**status** | **int** | HTTP Status code | [optional] 
**sub_errors** | [**list[ApiSubError]**](ApiSubError.md) | List of nested errors | [optional] 
**timestamp** | **int** | When it happened | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


