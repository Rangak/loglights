# loglights


Extract Hyperledger Fabric Logfile Highlights


usage: loglights.py [-h] [-d DEP] [-n NUM] [-s | --no-sort] [-p PAK] [-r REX] logfile


![Usage](usage.png?raw=true "Usage")



Example:

Create the logfile with timestamp option 

    # docker logs -t 11164e35484e >& ordererlogfile
    # loglights ordererlogfile



![Output Screenshot](out.png?raw=true "Output Screenshot")

