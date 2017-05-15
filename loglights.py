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
parser.add_argument("-p", "--precision", type=int, default=2, help='Timestamp precision, sub second decimal places')

args = parser.parse_args()
logfile = open(args.logfile, 'r')

num_lines=0
num_events=0
prev =[0,0]

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
        tsend = 20 + args.precision
        ts = line[11:tsend]
        num_lines += 1
        if prev == [ts, package]:
            continue
        else:
            if ts != prev[0]:
                if text[-1:] == '\n':
                    text = text[0:-1]
                output =  [ts, package, text]
                print('{:14} {:20} {:.140}'.format(*output))
                num_events += 1               
            prev = [ts,package]        

print("NumLines :" + str(num_lines))
print("NumEvents :" + str(num_events))
