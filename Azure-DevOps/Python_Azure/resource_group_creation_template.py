import os
import json
from azure_package_master import azure_config_manager
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import DeploymentMode
from azure_creds_master import azure_creds


credential = AzureCliCredential()
subscription_id = azure_creds['subscription_id']

resource_client = ResourceManagementClient(credential, subscription_id)

rg_result = resource_client.resource_groups.create_or_update(
    azure_config_manager.resource_name['rName'],
    {
        "location": azure_config_manager.resource_group['rgLocation']
    }
)

print(f"Provisioned resource group with ID: {rg_result.id}")
