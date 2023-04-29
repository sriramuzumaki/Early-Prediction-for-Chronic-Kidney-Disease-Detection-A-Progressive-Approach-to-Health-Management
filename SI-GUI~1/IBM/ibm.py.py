import requests

import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "IUkvgY9UzjuDiNaRMhlkNAKQYvUNorPJpbnhm_3wJaWL"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [['age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar',
       'red_blood_cells', 'pus_cell', 'pus_cell_clumps', 'bacteria',
       'blood glucose random', 'blood_urea', 'serum_creatinine', 'sodium',
       'potassium', 'hemoglobin', 'packed_cell_volume',
       'white_blood_cell_count', 'red_blood_cell_count', 'hypertension',
       'diabetesmellitus', 'coronary_artery_disease', 'appetite',
       'pedal_edema', 'anemia', 'class']], "values":[[61.0	,70.0,	5,	0,	0,	1,	1,	0,	0,	100.000000,	28.0,	2.1,	137.528754,	4.627244,	12.600000,	43.000000,	8406.122449,	4.707435,	1,	1,	0,	0,	0,	0,	0]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/1edd95dc-4b1f-466b-b4f1-c173fb7b2df3/predictions?version=2023-02-09', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions=response_scoring.json()
pred=predictions['predictions'][0]['values'][0][0]

if( pred == 1):
    print("You have ckd")
else:
    print("You are healthy")
    