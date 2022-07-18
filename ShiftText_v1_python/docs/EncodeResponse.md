# EncodeResponse

Response body of encode operation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **dict(str, str)** | Encoded content in KEY:VALUE format. Key is the content identifier  as passed in the request while value is encoded text. | [optional] 
**scopes** | [**list[Scope]**](Scope.md) | List of scopes and values as passed in request. | [optional] 
**font_identifier** | **str** | Unique identifier required to get the associated font file for this operation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


