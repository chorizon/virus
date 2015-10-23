#!/usr/bin/python3

from platform import python_version_tuple
from settings import config
import os
import argparse
import json

parser = argparse.ArgumentParser(description='An Simple script for obtain info of a log')

parser.add_argument('--uuid', help='The uuid of script', required=True)

args = parser.parse_args()

if not hasattr(config, 'logs_pastafari'):
    logs='./logs'
else:
    logs=config.logs_pastafari

uuid=args.uuid

result={'ERROR': 1, 'MESSAGE': '', 'CODE_ERROR' : 0}

if os.path.isfile(logs+'/log_'+uuid):
    f=open(logs+'/log_'+uuid)
    
    for line in f:
        pass
    
    f.close()
    
    try:
    
        print(line.strip())
        
    except:
        
        result['CODE_ERROR']=1
        
        result['MESSAGE']='Cannot load json message'

print(json.dumps(result))
