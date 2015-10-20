#!/usr/bin/python3

#if request.query.get('script', '')!='' and request.query.get('module', '')!='' and request.query.get('category', '')!='':

from platform import python_version_tuple
from subprocess import Popen, PIPE
from uuid import uuid4
import argparse
import hashlib
import os
import signal 
import sys
import json

pyv=python_version_tuple()

if pyv[0]!='3':
    print('Need python 3 for execute this script')
    sys.exit(1)

parser=argparse.ArgumentParser(description='A tool for execute daemons in a server')

parser.add_argument('--category', help='The category of script', required=True)
parser.add_argument('--module', help='The module where script is located', required=True)
parser.add_argument('--script', help='The script to run', required=True)
parser.add_argument('--params', help='The arguments of called script', required=False, nargs='?', const='')
parser.add_argument('--python_command', help='The python executable used', required=False, nargs='?', const='python3')

args=parser.parse_args()

result={}

uuid=str(uuid4())

script=os.path.basename(args.category)+'/'+os.path.basename(args.module)+'/'+os.path.basename(args.script)

#arr_params=[ '--'+x+' '+y for x,y in request.query.items() ]

params=args.params

python_command=args.python_command

if python_command==None:
    python_command='/usr/bin/python3'

args=['sudo '+python_command+' daemon.py --script "'+script+'" --uuid '+uuid+' --arguments "'+params+'"']

daemon=Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=True, cwd=None, env=None, universal_newlines=True, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=True, pass_fds=())

#daemon.pid

result['ERROR']=0

result['CODE_ERROR']=0

result['UUID']=uuid

result['MESSAGE']='Executing script...'

result['PROGRESS']=0

print(json.dumps(result))
