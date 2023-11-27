from pcpi import session_loader
import csv
import json

session_managers = session_loader.load_config('creds.json')
session = session_managers[0].create_cspm_session()

res = session.request('GET', '/cloud')

with open('status.csv', 'w') as outfile:

    writer = csv.writer(outfile)

    writer.writerow(['Account_Type', 'Account_Name', 'Account_ID','Message','Status','Remediation'])

    for cld in res.json():
        account_type = cld['deploymentType']
        account_name = cld['name']
        account_id = cld['accountId']


        res2 = session.request('GET', f'/account/{account_id}/config/status')

        message = res2.json()[0]['message']
        status = res2.json()[0]['status']
        remediation = res2.json()[0]['remediation']

        writer.writerow([account_type,account_name, account_id, message, status, remediation])