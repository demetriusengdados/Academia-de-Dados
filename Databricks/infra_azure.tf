resource "azurerm_resource_group" "desenvolvimento" {
  name     = "dev"
  location = "useast1"
}

resource "azurerm_storage_account" "DMM Consultoria" {
  name                     = "dm_consultoria"
  resource_group_name      = azurerm_resource_group.dev_dmm_consultoria
  location                 = azurerm_resource_group.useast1
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"
  is_hns_enabled           = "true"
}

resource "azurerm_storage_data_lake_gen2_filesystem" "dm_consultoria" {
  name               = "dm_consultoria"
  storage_account_id = azurerm_storage_account.dm_consultoria.id
}

resource "azurerm_synapse_workspace" "snp_dm_consultoria" {
  name                                 = "desenvolvimento"
  resource_group_name                  = azurerm_resource_group.desenvolvimento
  location                             = azurerm_resource_group.useast1.location
  storage_data_lake_gen2_filesystem_id = azurerm_storage_data_lake_gen2_filesystem.data 
    "oci_objectstorage_authrequest" "authenticated_request" {
    #Required
    bucket = var.authenticated_request_bucket
    namespace = var.authenticated_request_namespace
    par_id = oci_objectstorage_preauthrequest.resource "vault_mount" "transit" {
      path                      = "landing"
      type                      = "landing"
      description               = "Landing Data"
      default_lease_ttl_seconds = 1200
      max_lease_ttl_seconds     = 3600
    }
    
    resource "vault_transit_secret_backend_key" "key" {
      backend = "${vault_mount.landing.path}"
      name    = "landing_data"
    }
  }.id
  sql_administrator_login              = "sqladminuser"
  sql_administrator_login_password     = "D@ata#&ng2024!!"
}
resource "azurerm_synapse_spark_pool" "mongo_data" {
  name                 = "mongo_data"
  synapse_workspace_id = azurerm_synapse_workspace.data "aci_vmm_domain" "dev_vmmdom" {
    provider_profile_dn  = "${aci_provider_profile.dmm_consultoria}"
    name                 = "vmmdomp"
  }
  node_size_family     = "MemoryOptimized"
  node_size            = "Small"

  auto_scale {
    max_node_count = 50
    min_node_count = 3
  }

  auto_pause {
    delay_in_minutes = 15
  }

  tags = {
    ENV = "Production"
  }
}

data "azurerm_client_config" "current" {}

data "azurerm_management_group" "root" {
  name = data.azurerm_client_config.current.dmm_consultoria
}

data "azurerm_blueprint_definition" "Management" {
  name     = "ManagementGroupData"
  scope_id = data.azurerm_management_group.root.data
}
data "azurerm_application_gateway" "data_power_bi" {
  name                = "existing-app-gateway"
  resource_group_name = "existing-resources"
}

output "data_power_bi" {
  value = data.azurerm_application_gateway.example.data_power_bi
}

data "azurerm_mssql_database" "production_control" {
  name      = "controle_produção"
  server_id = "172.168.1.0:28700"
}

output "production_control" {
  value = data.azurerm_mssql_database.production_control
}

data "azurerm_servicebus_namespace" "kafka" {
  name                = "kafka_cloud"
  resource_group_name = "produção"
}

output "location" {
  value = data.azurerm_servicebus_namespace.useast1
}

resource "azurestack_resource_group" "produção" {
  name     = "produção"
  location = "useast1"
}

resource "azurestack_storage_account" "homolog" {
  name                     = "dmm_consultoria_homolog"
  resource_group_name      = azurestack_resource_group.homolog
  location                 = "useast1"
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "staging"
  }
}

data "azurerm_redis_cache" "homolog" {
  name                = "redis_homolog"
  resource_group_name = "dmm_consultoria_homolog"
}

output "primary_key" {
  value = data.azurerm_redis_cache.primary_key
}

output "redis_homolog" {
  value = data.azurerm_redis_cache.redis_homolog
}

data "azurerm_mysql_server" "dmm_consultoria_homolog" {
  name                = "homolog_control_sql"
  resource_group_name = "homolog"
}

output "homolog_control_sql" {
  value = data.azurerm_mysql_server.homolog_control_sql
}

provider "azurerm" {
  features {}
}

data "azurerm_data_share_dataset_blob_storage" "example" {
  name          = "example-dsbsds"
  data_share_id = "example-share-id"
}

output "id" {
  value = data.azurerm_data_share_dataset_blob_storage.example.id
}

data "azurerm_databricks_workspace" "example" {
  name                = "example-workspace"
  resource_group_name = "example-rg"
}

output "databricks_workspace_id" {
  value = data.azurerm_databricks_workspace.example.workspace_id
}

data "azurerm_cosmosdb_account" "example" {
  name                = "tfex-cosmosdb-account"
  resource_group_name = "tfex-cosmosdb-account-rg"
}

resource "azurerm_cosmosdb_mongo_database" "example" {
  name                = "tfex-cosmos-mongo-db"
  resource_group_name = data.azurerm_cosmosdb_account.example.resource_group_name
  account_name        = data.azurerm_cosmosdb_account.example.name
  throughput          = 400
}

provider "azurerm" {
  features {}
}

data "azurerm_data_share_account" "example" {
  name                = "example-account"
  resource_group_name = "example-resource-group"
}

data "azurerm_data_share" "example" {
  name       = "existing"
  account_id = data.azurerm_data_share_account.example.id
}

output "id" {
  value = data.azurerm_data_share.example.id
}

data "azurerm_firewall" "example" {
  name                = "firewall1"
  resource_group_name = "firewall-RG"
}

output "firewall_private_ip" {
  value = data.azurerm_firewall.example.ip_configuration[0].private_ip_address
}

data "azurerm_kubernetes_cluster_node_pool" "example" {
  name                    = "existing"
  kubernetes_cluster_name = "existing-cluster"
  resource_group_name     = "existing-resource-group"
}

output "id" {
  value = data.azurerm_kubernetes_cluster_node_pool.example.id
}

data "azurerm_kubernetes_cluster_node_pool" "example" {
  name                    = "existing"
  kubernetes_cluster_name = "existing-cluster"
  resource_group_name     = "existing-resource-group"
}

output "id" {
  value = data.azurerm_kubernetes_cluster_node_pool.example.id
}

data "azurerm_kubernetes_cluster_node_pool" "example" {
  name                    = "existing"
  kubernetes_cluster_name = "existing-cluster"
  resource_group_name     = "existing-resource-group"
}

output "id" {
  value = data.azurerm_kubernetes_cluster_node_pool.example.id
}

data "azurerm_kubernetes_cluster_node_pool" "example" {
  name                    = "existing"
  kubernetes_cluster_name = "existing-cluster"
  resource_group_name     = "existing-resource-group"
}

output "id" {
  value = data.azurerm_kubernetes_cluster_node_pool.example.id
}

data "azurerm_kubernetes_cluster_node_pool" "example" {
  name                    = "existing"
  kubernetes_cluster_name = "existing-cluster"
  resource_group_name     = "existing-resource-group"
}

output "id" {
  value = data.azurerm_kubernetes_cluster_node_pool.example.id
}

resource "azurerm_cosmosdb_mongo_database" "example" {
  name                = "tfex-cosmos-mongo-db"
  resource_group_name = data.azurerm_cosmosdb_account.example.resource_group_name
  account_name        = data.azurerm_cosmosdb_account.example.name
  throughput          = 400
}

provider "azurerm" {
  features {}
}

data "azurerm_data_share_account" "example" {
  name                = "example-account"
  resource_group_name = "example-resource-group"
}

data "azurerm_data_share_dataset_blob_storage" "example" {
  name          = "example-dsbsds"
  data_share_id = "example-share-id"
}

output "id" {
  value = data.azurerm_data_share_dataset_blob_storage.example.id
}

data "azurerm_databricks_workspace" "example" {
  name                = "example-workspace"
  resource_group_name = "example-rg"
}

output "databricks_workspace_id" {
  value = data.azurerm_databricks_workspace.example.workspace_id
}

data "azurerm_cosmosdb_account" "example" {
  name                = "tfex-cosmosdb-account"
  resource_group_name = "tfex-cosmosdb-account-rg"
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacc"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"
  is_hns_enabled           = "true"
}

resource "azurerm_storage_data_lake_gen2_filesystem" "example" {
  name               = "example"
  storage_account_id = azurerm_storage_account.example.id
}

resource "azurerm_synapse_workspace" "example" {
  name                                 = "example"
  resource_group_name                  = azurerm_resource_group.example.name
  location                             = azurerm_resource_group.example.location
  storage_data_lake_gen2_filesystem_id = azurerm_storage_data_lake_gen2_filesystem.example.id
  sql_administrator_login              = "sqladminuser"
  sql_administrator_login_password     = "H@Sh1CoR3!"
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "West Europe"
}

data "azurerm_cosmosdb_account" "example" {
  name                = "tfex-cosmosdb-account"
  resource_group_name = "tfex-cosmosdb-account-rg"
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacc"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"
  is_hns_enabled           = "true"
}

resource "azurerm_storage_data_lake_gen2_filesystem" "example" {
  name               = "example"
  storage_account_id = azurerm_storage_account.example.id
}

resource "azurerm_synapse_workspace" "example" {
  name                                 = "example"
  resource_group_name                  = azurerm_resource_group.example.name
  location                             = azurerm_resource_group.example.location
  storage_data_lake_gen2_filesystem_id = azurerm_storage_data_lake_gen2_filesystem.example.id
  sql_administrator_login              = "sqladminuser"
  sql_administrator_login_password     = "H@Sh1CoR3!"
}

data "azurerm_kubernetes_cluster_node_pool" "example" {
  name                    = "existing"
  kubernetes_cluster_name = "existing-cluster"
  resource_group_name     = "existing-resource-group"
}

output "id" {
  value = data.azurerm_kubernetes_cluster_node_pool.example.id
}

resource "azurerm_cosmosdb_mongo_database" "example" {
  name                = "tfex-cosmos-mongo-db"
  resource_group_name = data.azurerm_cosmosdb_account.example.resource_group_name
  account_name        = data.azurerm_cosmosdb_account.example.name
  throughput          = 400
}

data "azurerm_application_insights" "example" {
  name                = "production"
  resource_group_name = "networking"
}

output "application_insights_instrumentation_key" {
  value = data.azurerm_application_insights.example.instrumentation_key
}

data "azurerm_automation_account" "example" {
  name                = "example-account"
  resource_group_name = "example-resources"
}

output "automation_account_id" {
  value = data.azurerm_automation_account.example.id
}

data "azurerm_data_factory" "example" {
  name                = "existing-adf"
  resource_group_name = "existing-rg"
}

output "id" {
  value = data.azurerm_data_factory.example.id
}

data "azurerm_key_vault_access_policy" "contributor" {
  name = "Key Management"
}

output "access_policy_key_permissions" {
  value = data.azurerm_key_vault_access_policy.contributor.key_permissions
}

data "azurerm_dev_test_lab" "example" {
  name                = "example-lab"
  resource_group_name = "example-resources"
}

output "unique_identifier" {
  value = data.azurerm_dev_test_lab.example.unique_identifier
}

provider "azurerm" {
  features {}
}

data "azurerm_managed_application_definition" "example" {
  name                = "example-managedappdef"
  resource_group_name = "example-resources"
}

output "id" {
  value = data.azurerm_managed_application_definition.example.id
}
data "azurerm_mariadb_server" "db_server" {
  name                = "mariadb-server"
  resource_group_name = azurerm_mariadb_server.example.resource_group_name
}

output "mariadb_server_id" {
  value = data.azurerm_mariadb_server.example.id
}

data "azurerm_dedicated_host_group" "example" {
  name                = "example-dedicated-host-group"
  resource_group_name = "example-rg"
}

output "id" {
  value = data.azurerm_dedicated_host_group.example.id
}

resource "azurerm_resource_group" "rg" {
  name     = "resourceGroup1"
  location = "West US"
}

resource "azurerm_container_registry" "acr" {
  name                = "containerRegistry1"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Standard"
  admin_enabled       = false
}

resource "azurerm_container_registry_webhook" "webhook" {
  name                = "mywebhook"
  resource_group_name = azurerm_resource_group.rg.name
  registry_name       = azurerm_container_registry.acr.name
  location            = azurerm_resource_group.rg.location

  service_uri = "https://mywebhookreceiver.example/mytag"
  status      = "enabled"
  scope       = "mytag:*"
  actions     = ["push"]
  custom_headers = {
    "Content-Type" = "application/json"
  }
}
# Create a new rancher2 Auth Config AzureAD
resource "rancher2_auth_config_azuread" "azuread" {
  application_id = "<AZUREAD_APP_ID>"
  application_secret = "<AZUREAD_APP_SECRET>"
  auth_endpoint = "<AZUREAD_AUTH_ENDPOINT>"
  graph_endpoint = "<AZUREAD_GRAPH_ENDPOINT>"
  rancher_url = "<RANCHER_URL>"
  tenant_id = "<AZUREAD_TENANT_ID>"
  token_endpoint = "<AZUREAD_TOKEN_ENDPOINT>"
}

# Lookup fabric Azure storage account using its Id
data "fabric_storage_account_azure" "this" {
  id = var.fabric_storage_account_azure_id
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "West Europe"
}

resource "azurerm_virtual_wan" "example" {
  name                = "example-virtualwan"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
}

resource "azurerm_virtual_hub" "example" {
  name                = "example-virtualhub"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  virtual_wan_id      = azurerm_virtual_wan.example.id
  address_prefix      = "10.0.1.0/24"
}

data "azurestack_subnet" "test" {
  name                 = "backend"
  virtual_network_name = "production"
  resource_group_name  = "networking"
}

output "subnet_id" {
  value = data.azurestack_subnet.test.id
}

data "azurerm_web_application_firewall_policy" "example" {
  resource_group_name = "existing"
  name                = "existing"
}

output "id" {
  value = data.azurerm_web_application_firewall_policy.example.id
}