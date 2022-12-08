# Deploying and Testing AWS Lambda Functions with SAM
# ensure docker is running

# sam build -t template_no_auth.yaml
# sam local start-api
# Locally invoke the function at http://127.0.0.1:5000/predict

import requests
import json
import numpy as np

bucket_name = 'lh-lambda-buckets-202222'
key =  'validation/test_features.joblib'

data = {
    'bucket':bucket_name,
    'key':key,
}

headers = {
    'Content-type': "application/json"
}

# Main code for post HTTP request
url = "http://127.0.0.1:5000/predict"
response = requests.request("POST", url, headers=headers, data=json.dumps(data))
lambda_predictions = np.array(response.json())
show_cm(test_target, lambda_predictions, range(10))

# deploy sam using the command below and then use the url at the link
# sam deploy --guided

import matplotlib.pyplot as plt

def show_digits(pixel_vals):

    some_digit_image = (
        pixel_vals
        .values
        .reshape(28,28)
        .astype('float32')
    )
    plt.imshow(some_digit_image, cmap = "binary")
    plt.axis("off")

fours = train_features[train_target == 4]
nines = train_features[train_target == 9]
eights = train_features[train_target == 8]
fives = train_features[train_target == 5]

plt.figure(figsize=(8,8))
plt.subplot(221); show_digits(fours.iloc[0])
plt.subplot(222); show_digits(nines.iloc[0])
plt.subplot(223); show_digits(eights.iloc[1])
plt.subplot(224); show_digits(fives.iloc[1])


bucket_name = 'lambda-buckets-202222'
key =  'validation/test_features.joblib'

data = {
    'bucket':bucket_name,
    'key':key,
}

headers = {
    'Content-type': "application/json"
}

# Main code for post HTTP request
url = "https://qjiim4z1db.execute-api.us-west-2.amazonaws.com/dev/predict"
response = requests.request("POST", url, headers=headers, json=data)
lambda_predictions = np.array(response.json())
show_cm(test_target, lambda_predictions, range(10))
