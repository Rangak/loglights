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
parser.add_argument("-d", "--dep", type=int, default=1, help='Number of event lines shown')
parser.add_argument("-n", "--num", type=int, default=2, help='Number of decimal places matched in timestamp')
feature_parser = parser.add_mutually_exclusive_group(required=False)
feature_parser.add_argument('-s', '--sort', dest='sort', action='store_true', help='Sort by package')
feature_parser.add_argument('--no-sort', dest='sort', action='store_false',help='Sort by timestamp. This is the default')
parser.set_defaults(sort=False)
parser.add_argument('-p', '--pak', help='Filter to this list of comma separated packages', type=str, default='all')
parser.add_argument('-r', '--rex', help='Match text to case-insensitive python re ', type=str, default='^')

args = parser.parse_args()
logfile = open(args.logfile, 'r')

num_lines=0
num_events=0
prev = 0
depthcount = 0

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
        if prev == ts and depthcount == 0:
            continue
        else:
            if text[-1:] == '\n':
                text = text[0:-1]

            if depthcount == 0:
                if re.match(args.rex, text, re.I):
                    output.append([ts, package, text])            
                    depthcount = args.dep - 1
                    num_events += 1               
                    prev = ts                
            else:
                output.append([ts, package, text])            
                depthcount -= 1
      

if args.sort:
    output.sort(key=lambda x: x[1])


if args.pak == 'all':
    package_filter = list(set([item[1] for item in output]))
else:
    package_filter = args.pak.split(',')

for line in output:
    if line[1] in package_filter:
        print('{:14} {:20} {:.140}'.format(*line))

print("NumLines :" + str(num_lines))
print("NumEvents :" + str(num_events))
