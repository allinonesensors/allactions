#!/usr/bin/env python
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
import boto3
import urllib3
from st2common.runners.base_action import Action

urllib3.disable_warnings()
ec2 = boto3.client('ec2')


class MyEchoAction(Action):
	def run(self,InstanceIds):
		ec2.terminate_instances(InstanceIds=[InstanceIds])
                print("VM terminated successfully......")
