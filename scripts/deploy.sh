#!/bin/bash

# Package Lambda function
zip -j app/lambda_function.zip app/lambda_function.py

# Upload Lambda function to S3
aws s3 cp app/lambda_function.zip s3://serverless-app-bucket/

# Deploy CloudFormation stack
aws cloudformation deploy \
    --template-file templates/cloudformation.yaml \
    --stack-name serverless-app-stack \
    --capabilities CAPABILITY_NAMED_IAM
