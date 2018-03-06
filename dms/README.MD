# Cloudformation stack for DMS, with source from SQL Server, and target to S3

## Prerequisite

* This stack requires an existing SQL Server with TCP/IP connections, and login password available.
  * Take note of the following parameter to be used in the stacks
    * Server Name
    * Server Port
    * VPC where the host is in

## Overview

These stacks will create a new VPC, with a S3 bucket for the export, and a DMS task pulling data from the SQL Server

![Architecture diagram](/dms.png)

## Details

The creation of the stacks needs to run the template in sequence:

1. ml-vpc.yaml: This will create the Vpc
  1. This stack requires the VPC of the source DB, and the AWS Account ID of the VPC
2. ml-s3.yaml: This will create the S3 buckets for the dump

Optional:
3. ml-dms.yaml: This will create the DMS instance and task
  4. This stack requires the hostname, port, login and password of the source DB

## Sample runs

``` bash
$ aws cloudformation create-stack --stack-name ml-vpc --template-body file://./ml-vpc.yaml --parameters \
ParameterKey=SourceVpcOwnerParam,ParameterValue=<AWS Account of the source VPC> \
ParameterKey=SourceVPCIdParam,ParameterValue=<VPC ID of source VPC>

$ aws cloudformation create-stack --stack-name ml-s3 --template-body file://./ml-s3.yaml --capabilities CAPABILITY_IAM

$ aws cloudformation create-stack --stack-name ml-dms --template-body file://./ml-dms.yaml --capabilities CAPABILITY_IAM --parameters \
ParameterKey=SourceDBServerNameParam,ParameterValue=<Source DB hostname> \ ParameterKey=SourceDBPasswordParam,ParameterValue=<DB password> \
ParameterKey=SourceDBLoginParam,ParameterValue=<DB login> \
ParameterKey=SourceDBServerPortParam,ParameterValue=<DB host port> \
ParameterKey=SourceDBDatabaseNameParam,ParameterValue=<DB database name> \
ParameterKey=DMSSubnetParam,ParameterValue=<list of subnet ID seperated by commas> \
```
