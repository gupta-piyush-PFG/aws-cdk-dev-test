#!/usr/bin/env python3

from aws_cdk import core

from awscdktest.awscdktest_stack import AwscdktestStack


app = core.App()
AwscdktestStack(app, "awscdktest")

app.synth()
