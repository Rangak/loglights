#!/usr/local/bin/python3

import sys
import argparse
import re
import datetime

def valid_date(datestring):
    try:
        datetime.datetime.strptime(datestring, '%Y-%m-%d')
        return True
    except ValueError:
        return False

parser = argparse.ArgumentParser(description='Extract Hyperledger Fabric Logfile Highlights')
parser.add_argument('logfile', help='Name of Fabric logfile')
parser.add_argument("-d", "--depth", type=int, default=1, help='Number of lines of event to show')
parser.add_argument("-n", "--num", type=int, default=2, help='Number of sub second decimal places in timestamp')
feature_parser = parser.add_mutually_exclusive_group(required=False)
feature_parser.add_argument('-s', '--sort', dest='sort', action='store_true', help='Sort by package')
feature_parser.add_argument('--no-sort', dest='sort', action='store_false',help='Sort by timestamp. This is the default')
parser.set_defaults(sort=False)
parser.add_argument('-p', '--packages', help='Filter to this list of comma separated packages', type=str, default='all')

args = parser.parse_args()
logfile = open(args.logfile, 'r')

num_lines=0
num_events=0
prev =[0,0]

output = []

for line in logfile:
    if valid_date(line[:10]):
        body = line[31:]
        if valid_date(body[:10]):
            text = body[re.search("]", body).start()+1:]
            package = body.split(']')[0].split('[')[1]
        elif valid_date(body[5:15]):
            text = body[:5] + body[re.search("]", body).start()+1:]
            package = body.split(']')[0].split('[')[2]
        else:
            continue
        tsend = 20 + args.num
        ts = line[11:tsend]
        num_lines += 1
        if prev == [ts, package]:
            continue
        else:
            if ts != prev[0]:
                if text[-1:] == '\n':
                    text = text[0:-1]
                output.append([ts, package, text])
                num_events += 1               
            prev = [ts,package]        

if args.sort:
    output.sort(key=lambda x: x[1])

if args.packages!='all':
    package_filter = args.packages.split(',')
    for line in output:
        if line[1] in package_filter:
            print('{:14} {:20} {:.140}'.format(*line))
else:
    for line in output:
        print('{:14} {:20} {:.140}'.format(*line))

print("NumLines :" + str(num_lines))
print("NumEvents :" + str(num_events))
