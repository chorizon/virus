#!/usr/bin/python3

from platform import python_version_tuple
from settings import config
import os
import argparse
import json

parser = argparse.ArgumentParser(description='An Simple script for obtain info of a log')

parser.add_argument('--uuid', help='The uuid of script', required=True)
parser.add_argument('--num_line', help='The line to read', required=False)

args = parser.parse_args()

workdir=os.path.dirname(os.path.abspath(__file__))

os.chdir(workdir)

if not hasattr(config, 'logs_pastafari'):
    logs=workdir+'/logs'
else:
    logs=config.logs_pastafari

uuid=args.uuid

result={'ERROR': 1, 'MESSAGE': '', 'CODE_ERROR' : 0, 'PROGRESS': 0}

if os.path.isfile(logs+'/log_'+uuid):
    f=open(logs+'/log_'+uuid)
    
    arr_line=[]
    
    for line in f:
        if line != "":
            arr_line.append(line)
    
    f.close()
    
    if args.num_line==None:
        num_line=len(arr_line)-1
    else:
        num_line=int(args.num_line)
        
        if num_line>=len(arr_line):
            num_line=len(arr_line)-1

    line=arr_line[num_line]
    
    try:
    
        print(line.strip())
        
    except:
        
        result['CODE_ERROR']=1
        
        result['PROGRESS']=100
        
        result['MESSAGE']='Cannot load json message'
        
        print(json.dumps(result))
else:
    
    result['PROGRESS']=100
    
    result['CODE_ERROR']=1
        
    result['MESSAGE']='Cannot load json message, executed a task with this uuid?'

    print(json.dumps(result))
