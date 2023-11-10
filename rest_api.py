import requests, sys
from time import sleep

headers = {"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE2OTk2MzA4MDUsIm5iZiI6MTY5OTYzMDgwNSwiZXhwIjoxNjk5NjM0ODA0LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFZBQUFBTjJvMlczR24rdVQ0YWcxSkpSbVN4ZjlFbCt6bGRmNnExZnROQUJMc1lLVXQzUGhDRURzd0NOZGsyQllSek90UDBqb3duR2JYaEp2NEs4ekc5U1VSbkNkOUFGWE5lNHhiMnFjWWhDcGJiWHc9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiTyBCcmllbiIsImdpdmVuX25hbWUiOiJDYWxsdW0iLCJncm91cHMiOlsiODEwOGM1MDMtZDY1Ni00MmNmLThlZTQtODk0NGFlZjBmYWRlIiwiOTdhZjgxMmQtOTZlOS00ZjAxLThhMTEtNzU4MDMzNzYyMTdhIiwiODdmNjAwM2QtOTQ3MC00MzhmLWJmZWYtODEzYjM3ZmMyYjY4IiwiM2U4NDgwOTgtYjRhMS00MTdkLWExYmEtYzljZjNmY2U5ZjUxIiwiODM4YTI4OWEtODRhNC00Y2E4LWFlZWMtYjMxZWMxZDcxZDRhIiwiNGRjMDNiOWYtMWI2Yy00NDE1LWFjMDUtODI0MjcxM2M3NTIwIiwiNWFkN2Q2YjQtYWRhZi00YjlkLTk1N2YtMGYzYjYxNGJlZTYwIiwiOGFjMTU0ZGQtZDQ1Zi00YzQ2LTk0ZTUtYmI3OGZlZmEzYWVmIiwiOGM4MTg2ZWEtNDJhNC00NGFmLThhNzgtYWU5MTQwMTFlNmI0IiwiZDJhNmE4ZWYtNGQyNi00ZDk1LWJkMTEtYWExZWM2MTlmODE4Il0sImlkdHlwIjoidXNlciIsImlwYWRkciI6IjIwMDE6YmI2OjYzMzplMjAwOmI0YmM6MzExMDoxNzZlOjhiYjkiLCJuYW1lIjoiQzIxMzA2NTAzIENhbGx1bSBPIEJyaWVuIiwib2lkIjoiMzY5ZmZiYzktZjQzMi00MDY5LTllOGQtMGNiM2QzOTMyNWQ1Iiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTQwMjI5ODg0OS0xNzM0NzA1MTMxLTMxMjAwMjQwMDEtNDQyNzYiLCJwdWlkIjoiMTAwMzIwMDE3REEzQTBGMiIsInJoIjoiMC5BVEVBeXhkamRranBYMDZNN05xOGppX1Yya1pJZjNrQXV0ZFB1a1Bhd2ZqMk1CTXhBSUkuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiODZEQTFUUTFEVHMtLTRseU9rLWhwN0ktMU92ZURPOEFSNjBaTFNxcFh2QSIsInRpZCI6Ijc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYSIsInVuaXF1ZV9uYW1lIjoiQzIxMzA2NTAzQG15dHVkdWJsaW4uaWUiLCJ1cG4iOiJDMjEzMDY1MDNAbXl0dWR1Ymxpbi5pZSIsInV0aSI6Ii1TVm56cmpRRGsyTm9TSGtrNExfQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfY2FlIjoiMSIsInhtc190Y2R0IjoxNTI1MzM4OTQxfQ.q05cdA42JHxuabcnIWNsnLCW7JfvvsYpyJtTdpD3pA9-NxS6LyRumwG7ej2Bkwi7haT4kcWh3F-_Qbi6UdTgWeIYIYB2iVDVqWm27W7MZycRCX5oiJqqUdcLulPZwKB5dGPImcTsbiYBsAwyoE_P6AfAsSX2WCQ3xjt23pcyGoa1RuGIMrIu6pooEXWd1rYx_hZbnPSTZ-CGsZJ0v4Puj77YsklUmz7y8fDoeRYmz0Xfl5K8xBEj-rEA7fxBVwg97sFwVgGNbMVYCzTSaMczwovGC_Bb3hnnfkvKVe4Ixx5IQkC6ROv3hKAuTcydF04gHGVOTmdlBTpVN2sJ1stZpA",
        "Content-Type" : "application/json"}


def createResourceGroup(rg_name, headers): 
    """ Uses REST API to create an Azure resource group. """
    api_url = f"https://management.azure.com/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourcegroups/{rg_name}?api-version=2021-04-01"
    json_args = {
        "location": "westeurope"
        }

    response = requests.put(api_url, json=json_args, headers=headers)

    if response.status_code == 200 or response.status_code == 201: 
        print(f"Resource Group '{rg_name}' Created Successfully: {response.status_code}")
    else: 
        print(f"Error Creating Resource Group: {response.status_code}\n{response.reason}\n\nThe program will now exit.")
        sys.exit()


def createVirtualNetwork(rg_name, net_name, headers):
    """ Uses REST API to create an Azure Virtual Network. """
    api_url = f"https://management.azure.com/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/{rg_name}/providers/Microsoft.Network/virtualNetworks/{net_name}?api-version=2023-05-01"
    json_args = {
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
    
    response = requests.put(api_url, json=json_args, headers=headers)

    if response.status_code == 200 or response.status_code == 201: 
        print(f"Virtual Network '{net_name}' Created Successfully: {response.status_code}")
    else: 
        print(f"Error Creating Virtual Network: {response.status_code}\n{response.reason}\n\nThe program will now exit.")
        sys.exit()


def createSubnet(rg_name, net_name, subnet_name, headers):
    """ Uses REST API to create an Azure subnet. """
    api_url = f"https://management.azure.com/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/{rg_name}/providers/Microsoft.Network/virtualNetworks/{net_name}/subnets/{subnet_name}?api-version=2023-05-01"
    json_args = {
        "properties": {
            "addressPrefix": "10.0.0.0/16"
        }
    }

    response = requests.put(api_url, json=json_args, headers=headers)

    if response.status_code == 200 or response.status_code == 201: 
        print(f"Subnet '{subnet_name}' Created Successfully: {response.status_code}")
    else: 
        print(f"Error Creating Subnet: {response.status_code}\n{response.reason}\n\nThe program will now exit.")
        sys.exit()


def createPublicIP(rg_name, ip_name, headers):
    """ Uses REST API to create an Azure Public IP. """
    api_url = f"https://management.azure.com/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/{rg_name}/providers/Microsoft.Network/publicIPAddresses/{ip_name}?api-version=2023-05-01"
    json_args = {
        "location": "westeurope"
    }

    response = requests.put(api_url, json=json_args, headers=headers)

    if response.status_code == 200 or response.status_code == 201: 
        print(f"Public IP '{ip_name}' Created Successfully: {response.status_code}")
    else: 
        print(f"Error Creating Public IP: {response.status_code}\n{response.reason}\n\nThe program will now exit.")
        sys.exit()


def createNetworkInterface(rg_name, ip_name, net_name, subnet_name, nic_name, headers):
    """ Uses REST API to create an Azure Network Interface. """
    api_url = f"https://management.azure.com/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/{rg_name}/providers/Microsoft.Network/networkInterfaces/{nic_name}?api-version=2023-05-01"
    json_args = {
        "properties": {
            "ipConfigurations": [
            {
                "name": "ipconfig1",
                "properties": {
                "publicIPAddress": {
                    "id": f"/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/{rg_name}/ providers/Microsoft.Network/publicIPAddresses/{ip_name}"
                },
                "subnet": {
                    "id": f"/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/{rg_name}/ providers/Microsoft.Network/virtualNetworks/{net_name}/subnets/{subnet_name}"
                }
                }
            }
            ]
        },
        "location": "westeurope"
    }

    response = requests.put(api_url, json=json_args, headers=headers)

    if response.status_code == 200 or response.status_code == 201: 
        print(f"Network Interface '{nic_name}' Created Successfully: {response.status_code}")
    else: 
        print(f"Error Creating Network Interface: {response.status_code}\n{response.reason}\n\nThe program will now exit.")
        sys.exit()


def createVirtualMachine(rg_name, vm_name, nic_name, headers):
    """ Uses REST API to create an Azure Virtual Machine. """
    api_url = f"https://management.azure.com/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/{rg_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}?api-version=2023-07-01"
    json_args = {
        "id": f"/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/{rg_name}/ providers/Microsoft.Compute/virtualMachines/{vm_name}",
        "type": "Microsoft.Compute/virtualMachines",
        "properties": {
            "osProfile": {
            "adminUsername": "callum",
            "secrets": [
                
            ],
            "computerName": f"{vm_name}",
            "linuxConfiguration": {
                "ssh": {
                "publicKeys": [
                    {
                    "path": "/home/callum/.ssh/authorized_keys",
                    "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDALXtd3zStLQPaYz5kar1bcPXB+sSL3wHUt1uvKxU9EQSB944fJjCHNuRzaNp6t8+vuaDYF17OTtTaQycMEz/Nt0eUDO5JPW+4GSfwptrL/dTgIzCFL3ErzSLeh44MdKPL1r+GUKhUDKAV8FM67v6pwZWoc1Rqv0rJ3H7mLPsMjZcVvvUYzVvxWDg60Z4coUK5t9jO2e5K+KdQ00L30hoAuMmTNctsnhfjAjda6tR3jgl9ubcsE2wmC5AX0BCVnmA6ag9+DVvwtOcsh7VHY6g8ndm7jcG5XoFMeNYhCCAB1GmQVfmXEHgJwHtJwuraRUoa2SBf3a5zS3m51OPY25kPoQQkbSenkDVj9oIUOZDLkqj4vNtUeGxYp4DvJBcAK9jh4OqvFDgqDoNUpJspBCBi/QUkOf/3KirRkv3wJPqm0DHz+wdyL5pwXITc5wBuz5b/3zqyCwA98BRQUMMx/XaFp33Un3rCi8h9EjxerucV/m1Gilxz3l8f/G25EIW1rOc= callumobrien@Callums-MacBook-Air.local"
                    }
                ]
                },
                "disablePasswordAuthentication": "true"
            }
            },
            "networkProfile": {
            "networkInterfaces": [
                {
                "id": f"/subscriptions/301e0856-bba6-41f3-a8b4-6dcdee9206b4/resourceGroups/{rg_name}/ providers/Microsoft.Network/networkInterfaces/{nic_name}",
                "properties": {
                    "primary": "true"
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
        "name": f"{vm_name}",
        "location": "westeurope"
    }

    response = requests.put(api_url, json=json_args, headers=headers)

    if response.status_code == 200 or response.status_code == 201: 
        print(f"Virtual Machine '{vm_name}' Created Successfully: {response.status_code}")
    else: 
        print(f"Error Creating Virtual Machine: {response.status_code}\n{response.reason}\n\nThe program will now exit.")
        sys.exit()


# Main Program
rg_name = input("Please enter the name of the Resource Group.\t")
net_name = input("Please enter the name of the Virtual Network.\t")
subnet_name = input("Please enter the name of the subnet.\t")
ip_name = input("Please enter the name of the Public IP.\t")
nic_name = input("Please enter the name of the Network Interface.\t")
vm_name = input("Please enter the name of the Virtual Machine.\t")

print("\n")

# Sleep is used so I don't get blocked for too many requests.
createResourceGroup(rg_name, headers)
sleep(5)
createVirtualNetwork(rg_name, net_name, headers)
sleep(5)
createSubnet(rg_name, net_name, subnet_name, headers)
sleep(5)
createPublicIP(rg_name, ip_name, headers)
sleep(5)
createNetworkInterface(rg_name, ip_name, net_name, subnet_name, nic_name, headers)
sleep(5)
createVirtualMachine(rg_name, vm_name, nic_name, headers)