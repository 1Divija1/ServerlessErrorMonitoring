from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import pandas as pd

# Load data
mnist = fetch_openml("mnist_784", version=1)

# Randomly sample 20000 rows from the original dataset
mnist_data = (
    mnist
    .data
    .sample(n=20000, random_state=42, axis=0, replace=False)
)

# Slice target by the same row sampling
target = (
    mnist
    .target
    .loc[mnist_data.index].astype('uint8')
)

# Reshape values to be 28x28
some_digit_image = (
    mnist_data
    .iloc[0]
    .values
    .reshape(28,28)
    .astype('float32')
)
plt.imshow(some_digit_image, cmap = "binary")
plt.axis("off")

# train the K-Nearest Neighbors Classifier


from sklearn.model_selection import train_test_split
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# Function to train KNN Classifier and show scores
def train_knn_model(features:np.array, target:np.array):

    # Train KNN Classifier
    knnclf = KNeighborsClassifier(weights='distance', n_neighbors=4)
    knnclf.fit(features, target)
    scores = cross_val_score(
        knnclf, features, target, scoring='accuracy', cv=10
    )
    print(f'Cross Validation Scores: {scores}')
    print(f'Average accuracy: {np.mean(scores)}')
    return knnclf, scores

# Split data to training and test set
train_features, test_features, train_target, test_target = train_test_split(
        mnist_data, target, test_size = 0.2, random_state = 42
)
knnclf, scores = train_knn_model(train_features, train_target)

# Metrics

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score

def show_cm(y_true, y_pred, labels):

    # Display Confusion matrix and show accuracy scores
    conf_mat = confusion_matrix(y_true, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=conf_mat, display_labels=labels)
    score = accuracy_score(y_true, y_pred)
    print(f'Accuracy: {score}')
    disp.plot();

# Make predictions
test_target_pred = knnclf.predict(test_features)
# Show confusion matrix
show_cm(test_target, test_target_pred, range(10))

# Print numbers

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

# saving the model locally to be containerised as part of the lambda function using Docker
import joblib

joblib.dump(knnclf, 'app/knnclf.joblib')

# initialising S3 Bucket

import boto3

def create_bucket(region:str, bucket_name:str) -> dict:

    s3 = boto3.client('s3')
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint':region
        }
    )
    return response

region = 'us-west-2'
bucket_name = 'lambda-buckets-2022'
create_bucket(region, bucket_name)

# Upload Test data to S3

from io import BytesIO
import joblib
import boto3

def UploadToS3(data, bucket:str, key:str):

    with BytesIO() as f:
        joblib.dump(data, f)
        f.seek(0)
        (
            boto3
            .client('s3')
            .upload_fileobj(Bucket=bucket, Key=key, Fileobj=f)
        )

bucket_name = 'lambda-buckets-202222'
key =  'validation/test_features.joblib'
UploadToS3(test_features, bucket_name, key)

# List all objects in S3 bucket

import boto3

def listS3Objects(bucket:str) -> list:

     # Connect to s3 resource
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket)

    # List all object keys in s3 bucket
    obj_list = [object_summary.key for object_summary in my_bucket.objects.all()]
    return obj_list
  
listS3Objects('lh-lambda-buckets-2022')
