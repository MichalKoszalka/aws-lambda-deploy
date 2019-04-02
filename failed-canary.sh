#!/bin/bash
aws lambda update-function-code --function-name Redirect --zip-file fileb://build/redirect_v3.zip --publish

export STATE_MACHINE_ARN=`aws cloudformation describe-stack-resources --stack-name aws-lambda-deploy-stack --logical-resource-id DeployStateMachine --output text | cut  -d$'\t' -f3`
aws stepfunctions start-execution --state-machine-arn $STATE_MACHINE_ARN --input '{
"function-name": "Redirect",
"alias-name": "LIVE",
"new-version": "38",
"steps": 5,
"interval": 120,
"type": "linear"}'