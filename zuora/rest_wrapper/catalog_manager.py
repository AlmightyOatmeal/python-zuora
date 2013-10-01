import requests
from request_base import RequestBase

# For more information on parameters and responses, please see
# http://knowledgecenter.zuora.com/D_Zuora_APIs/REST_API/B_REST_API_reference/Catalog


class CatalogManager(RequestBase):
    
    def get_catalog(self, pageSize=10, page=1):
        fullUrl = self.zuora_config.base_url + 'catalog/products'
        params = {'pageSize': pageSize,
                  'page': page}
    
        response = requests.get(fullUrl, params=params,
                                headers=self.zuora_config.headers)
        return self..get_json(response)