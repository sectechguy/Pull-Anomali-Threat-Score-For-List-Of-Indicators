import pandas as pd
import requests
import json

url = 'https://<server>/api/v2/intelligence/?username='
username = '<username>'
api_key = '<api_key>'

test100 = test100['request'].tolist()
column1 = list()
column2 = list()
column3 = list()
column4 = list()
column5 = list()
column6 = list()
for row in test_sus_list:
  value_api = url+username+'&api_key='+api_key+'&limit=10000&value='
  responses = requests.get(value_api+row, verify=False)
  data = json.loads(responses.text)
  valuess = data['objects']
  for index in valuess:
    column1.append(index['value'])
    column2.append(index['meta']['severity'])
    column3.append(index['confidence'])
    column4.append(index['threatscore'])
    column5.append(index['source_reported_confidence'])
    column6.append(index['retina_confidence'])
test__output = pd.DataFrame(
  {'Indicator': column1,
   'Severity': column2,
   'Confidence': column3,
   'Threat Score': column4,
   'Source Reported Confidence': column5,
   'Retina Confidence': column6
  })
