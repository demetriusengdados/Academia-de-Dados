{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "workspaces_adb_curso_arquitetura_dados_dev_name": {
            "defaultValue": "adb_curso_arquitetura_dados_dev",
            "type": "String"
        }
    },
    "variables": {},
    "resources": [
        {
            "type": "Microsoft.Databricks/workspaces",
            "apiVersion": "2024-05-01",
            "name": "[parameters('workspaces_adb_curso_arquitetura_dados_dev_name')]",
            "location": "eastus",
            "tags": {
                "curso_arquitetura": "dev"
            },
            "sku": {
                "name": "premium"
            },
            "properties": {
                "defaultCatalog": {
                    "initialType": "UnityCatalog"
                },
                "managedResourceGroupId": "[concat('/subscriptions/5e076355-9360-4d8a-ad4b-2b821c460c5c/resourceGroups/databricks-rg-', parameters('workspaces_adb_curso_arquitetura_dados_dev_name'), '-yndkg5hkybm46')]",
                "parameters": {
                    "enableNoPublicIp": {
                        "value": false
                    },
                    "prepareEncryption": {
                        "value": false
                    },
                    "publicIpName": {
                        "value": "nat-gw-public-ip"
                    },
                    "requireInfrastructureEncryption": {
                        "value": false
                    },
                    "storageAccountName": {
                        "value": "dbstorageplxbrxkhpqro2"
                    },
                    "storageAccountSkuName": {
                        "value": "Standard_GRS"
                    },
                    "vnetAddressPrefix": {
                        "value": "10.139"
                    }
                },
                "authorizations": [
                    {
                        "principalId": "9a74af6f-d153-4348-988a-e2672920bee9",
                        "roleDefinitionId": "8e3af657-a8ff-443c-a75c-2fe8c4bcb635"
                    }
                ],
                "createdBy": {},
                "updatedBy": {}
            }
        }
    ]
}