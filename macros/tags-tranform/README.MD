## Cloudformation custom transform

This stack creates a Cloudformation transform that convert string of tags, such as `a=1,b=2`, into tags array.

## Contents
* lambda/tag-transform.py - the macro that takes in a string and returns array of tags
* templates/macros.yml - Cloudformation template that creates the tags tranform macro. 

## Steps
1. Zip up the `tag-transform.py` with command `$ zip lambda/tag-transform.zip lambda/tag-transform.py`
1. Create a S3 bucket and upload the Lambda code, e.g. s3://<s3 bucket>/lambda/tag-tranform.zip
1. Create the stack with command `aws cloudformation create-stack --stack-name <stack name> --template-body file://templates/macros.yml --parameters ParameterKey=resourcesBucket,ParameterValue=<s3 bucket> ParameterKey=lambdaBucketKey,ParameterValue=lambda/tag-transform.zip ParameterKey=prefix,ParameterValue=macros --capabilities CAPABILITY_NAMED_IAM`
