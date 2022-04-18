# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

Param(
    [Parameter(
        Mandatory=$True,
        HelpMessage='Which Azure region do you willing to deploy?'
    )]
    [ValidateScript({$_ -in (az account list-locations --query '[*].name' -o tsv)})]
    [string] $AzureRegion
)

$UserObjectID =  (Get-AzADUser -SignedIn ).Id 

New-AzDeployment `
   -Name feathrDeployment `
   -location $AzureRegion `
   -principalId $UserObjectID `
   -TemplateUri https://raw.githubusercontent.com/Dongbumlee/feathr/main/docs/how-to-guides/deploy.json `
   -DeploymentDebugLogLevel All

# az deployment sub create 
# --location $AzureRegion 
# --principalId $UserObjectID 
# -u https://raw.githubusercontent.com/Dongbumlee/feathr/main/docs/how-to-guides/deploy.json 
# --debug


