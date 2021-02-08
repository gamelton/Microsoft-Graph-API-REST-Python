# Office 365 consumed license Python

This is an example task of finding Office 365 license consumption. It's a bare minimum Python script that has hardcoded SKU ID of the license of interest. It outputs just one number of consumed licenses of that SKU. It uses specific URL `https://graph.microsoft.com/v1.0/subscribedSkus/{SKU-ID}` to get information on specific license SKU. It authenticates with your own identity this will use your own identity (the app identity). This oauth flow is called `client credentials grant flow`.

Prerequesities:
1. Python 3
1. Python module requests
   On Ubuntu you could install module by running
   > apt install python3-pip
   
   > pip3 install requests
1. Azure Active Directory premium 1 (P1) license
1. Application has specific API permission

   `Organization.Read.All`, `Directory.Read.All`
1. Application has secret (password)

Preparation:
1. Get Tenant (Authority) ID that is Directory ID from Azure AD
1. Register application in [Azure Portal (App Registrations)](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
   1. Get Application (Client) ID from Application properties
   1. Switch off `Allow public client flows`
   1. Under "Certificates & secrets", generate a new client secret. Set the expiration preferably to never.
      
      Note: You should save it immediately as it won't be shown again

   1. Under Api Permissions add the application permissions for Microsoft Graph you want
      1. Organization.Read.All 
      1. Directory.Read.All

      Note: You would need to press grant admin consent button to apply for the organization.
      
1. Edit the script and supply your
   1. `TENANT-ID` for Tenant (Authority) ID
   1. `APP-ID` and `APP-SECRET` for Application (Client) ID and secret
   1. `SKU-ID` for SKU license which you would like to get the consumption
   
   You could get the list of all SKUs and look for the ID you want by listing all SKU on the tenant
   
   ```python
   skusurl = 'https://graph.microsoft.com/v1.0/subscribedSkus'
   skusrequest = requests.get(skusurl, headers=tokenheader)
   skusrequest.text
   ```

1. Make script executable
   > chmod +x get-office365-consumed-license.py

