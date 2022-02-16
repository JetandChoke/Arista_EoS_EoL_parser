# Arista_EoS_EoL_parser
Automate Analysis of Arista End of Life/End of Sale information

This script will fetch data from 'https://www.arista.com/custom_data/bug-alert/alertBaseDownloadApi.php' and get yourself a pleasant JSON with EoS and EoL for Arista products.
Get the portal access token from https://www.arista.com/en/users/profile and you are good to go.
Output in a format:

{
    "endOfHardwareRMARequests": "2022-06-19",
    "endOfLife": "2022-06-19",
    "endOfSale": "2019-06-20",
    "endOfTACSupport": "2022-06-19",
    "modelName": "7500E-36Q-LC"
},
{
    "endOfHardwareRMARequests": "2018-04-15",
    "endOfLife": "2018-04-15",
    "endOfSale": "2015-04-15",
    "endOfTACSupport": "2018-04-15",
    "modelName": "DCS-7050T-64-SSD"
}
