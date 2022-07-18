# EncodeRequest

Request body for encode operation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **dict(str, str)** | [Required] Content to encode in KEY:VALUE format. Key is the content  identifier from caller application which is returned in the response as it is so that the encoded value can be used, while Value is the  content that need to be encoded. | 
**scopes** | [**list[Scope]**](Scope.md) | [Optional] List of scopes along with its values to create different  font. e.g. unique fonts are required per &#39;session per user&#39; then key can be SESSION, USER. The order of scopes in the list should be  retained to get the same text/font. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


