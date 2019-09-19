#!/usr/bin/env python2
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
import boto3
import urllib3
from st2common.runners.base_action import Action

urllib3.disable_warnings()
ec2 = boto3.client('ec2')

class MyEchoAction(Action):
	def run(self,InstanceIds,action):
		action = action.upper()
		if action == 'START':
			ec2.start_instances(InstanceIds=[InstanceIds])
			print("VM started successfully......")

		elif action == 'STOP':
			ec2.stop_instances(InstanceIds=[InstanceIds])
			print("VM stopped successfully......")

		elif action == 'RESTART':
			ec2.reboot_instances(InstanceIds=[InstanceIds])
			print("VM restarted successfully......")

		else:
			print("Invalid arguments...")
