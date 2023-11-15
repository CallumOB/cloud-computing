import requests, sys, subprocess, json
from time import sleep

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


def getAuthToken():
    command = "az account get-access-token"

    try:
        result = subprocess.run(command, check=True, text=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Parse the JSON output
        json_output = json.loads(result.stdout)

        # Access the accessToken element
        access_token = json_output.get('accessToken', '')
        return access_token
    except:
        print("Error getting auth token, exiting program.")
        sys.exit()

# Main Program


headers = {"Authorization" : f"Bearer {getAuthToken()}",
        "Content-Type" : "application/json"}
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