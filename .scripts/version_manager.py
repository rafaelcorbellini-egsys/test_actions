#!/usr/bin/env python

import yaml
import sys

client = sys.argv[1]
print('trabalhando no client: '+client)
environment = sys.argv[2]
print('no ambiente: '+environment)
kind = sys.argv[3]
print('subindo um: '+kind)
kind = sys.argv[3]
print('subindo um: '+kind)

file_name = "version_control.yml"


def magic(*args):
    with open(file_name) as f:
        conf = yaml.safe_load(f) 

    # get section
    section = args[0]

    # check if Config file has Section
    if not conf.has_key(section):
        print "key missing"
        quit()

    # get values
    argList = list(args) # convert tuple to list
    argList.pop(0) # remove Section from list

    # create lookup path
    parsepath = "conf['" + section + "']"

    for arg in argList:
        parsepath = parsepath + "['" + arg + "']"   

    vcodeKey = 'vcode'
    vnameKey = 'vname'

    env = conf['client'][client][environment]
    currVCode = env[vcodeKey]
    currVName = env[vnameKey]

    #incrementando vcode
    env[vcodeKey] = currVCode+1
    print 'vcode atual:',currVCode
    print 'vcode novo:', env[vcodeKey] 


    print 'vname atual:',currVName
    separator = '.'
    vnamedSplited = currVName.split('.')
    if kind == 'fix':
        indexKind = 2
    if kind == 'feat':
        indexKind = 1
    if kind == 'breaking_change':
        indexKind = 0


    vnamedSplited[indexKind] = str(int(vnamedSplited[indexKind])+1)
    env[vnameKey] = separator.join(vnamedSplited)

    with open(file_name, 'w') as f:
        yaml.safe_dump(conf, f, default_flow_style=False)    

    #incrementando vname
    print 'vname novo:', env[vnameKey] 

    return eval(parsepath)
    f.close()


scans = magic('client',client,environment,'vname')
