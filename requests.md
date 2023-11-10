# Resource Group

PUT https://management.azure.com/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourcegroups/lab4?api-version=2021-04-01

```json
{
	location: "westeurope"
}
```


# Virtual Network

PUT https://management.azure.com/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/lab4/providers/Microsoft.Network/virtualNetworks/lab4-net?api-version=2023-05-01

```json
{
  "properties": {
    "addressSpace": {
      "addressPrefixes": [
        "10.0.0.0/16"
      ]
    },
    "flowTimeoutInMinutes": 10
  },
  "location": "westeurope"
}
```


# Subnet

PUT https://management.azure.com/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/lab4/providers/Microsoft.Network/virtualNetworks/lab4-net/subnets/lab4-subnet?api-version=2023-05-01

```json
{
  "properties": {
    "addressPrefix": "10.0.0.0/16"
  }
}
```


# Public IP Addresses 

PUT https://management.azure.com/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/lab4/providers/Microsoft.Network/publicIPAddresses/lab4-publicIP?api-version=2023-05-01

```json
{
  "location": "westeurope"
}
```



# Network Interfaces

https://management.azure.com/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/lab4/providers/Microsoft.Network/networkInterfaces/lab4-nic?api-version=2023-05-01

```json 
{
  "properties": {
    "ipConfigurations": [
      {
        "name": "ipconfig1",
        "properties": {
          "publicIPAddress": {
            "id": "/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/lab4/ providers/Microsoft.Network/publicIPAddresses/lab4-publicip"
          },
          "subnet": {
            "id": "/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/lab4/ providers/Microsoft.Network/virtualNetworks/lab4-net/subnets/lab4-subnet"
          }
        }
      }
    ]
  },
  "location": "westeurope"
}
```


# Virtual Machine

PUT https://management.azure.com/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/lab4/providers/Microsoft.Compute/virtualMachines/lab4-vm?api-version=2023-07-01

```json 
{
  "id": "/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/lab4/ providers/Microsoft.Compute/virtualMachines/lab4-vm",
  "type": "Microsoft.Compute/virtualMachines",
  "properties": {
    "osProfile": {
      "adminUsername": "callum",
      "secrets": [
        
      ],
      "computerName": "lab4-vm",
      "linuxConfiguration": {
        "ssh": {
          "publicKeys": [
            {
              "path": "/home/callum/.ssh/authorized_keys",
              "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDALXtd3zStLQPaYz5kar1bcPXB+sSL3wHUt1uvKxU9EQSB944fJjCHNuRzaNp6t8+vuaDYF17OTtTaQycMEz/Nt0eUDO5JPW+4GSfwptrL/dTgIzCFL3ErzSLeh44MdKPL1r+GUKhUDKAV8FM67v6pwZWoc1Rqv0rJ3H7mLPsMjZcVvvUYzVvxWDg60Z4coUK5t9jO2e5K+KdQ00L30hoAuMmTNctsnhfjAjda6tR3jgl9ubcsE2wmC5AX0BCVnmA6ag9+DVvwtOcsh7VHY6g8ndm7jcG5XoFMeNYhCCAB1GmQVfmXEHgJwHtJwuraRUoa2SBf3a5zS3m51OPY25kPoQQkbSenkDVj9oIUOZDLkqj4vNtUeGxYp4DvJBcAK9jh4OqvFDgqDoNUpJspBCBi/QUkOf/3KirRkv3wJPqm0DHz+wdyL5pwXITc5wBuz5b/3zqyCwA98BRQUMMx/XaFp33Un3rCi8h9EjxerucV/m1Gilxz3l8f/G25EIW1rOc= callumobrien@Callums-MacBook-Air.local"
            }
          ]
        },
        "disablePasswordAuthentication": true
      }
    },
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/lab4/ providers/Microsoft.Network/networkInterfaces/lab4-nic",
          "properties": {
            "primary": true
          }
        }
      ]
    },
    "storageProfile": {
      "imageReference": {
        "sku": "16.04-LTS",
        "publisher": "Canonical",
        "version": "latest",
        "offer": "UbuntuServer"
      },
      "dataDisks": [
        
      ]
    },
    "hardwareProfile": {
      "vmSize": "Standard_D1_v2"
    },
    "provisioningState": "Creating"
  },
  "name": "lab4-vm",
  "location": "westeurope"
}
```
