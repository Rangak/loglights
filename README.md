# loglights
Cleanup and highlight events in Fabric peer and orderer logs



usage: loglights.py [-h] [-d DEPTH] [-p PRECISION] logfile

Extract Hyperledger Fabric Logfile Highlights

positional arguments:

  logfile               Name of Fabric logfile

optional arguments:

  -h, --help                            show this help message and exit
  -d DEPTH, --depth DEPTH               Number of lines of event to show
  -p PRECISION, --precision PRECISION   Timestamp precision, sub second decimal places


Example:

Create the logfile with timestamp option 

    # docker logs -t 11164e35484e >& ordererlogfile
    # loglights ordererlogfile




![Output Screenshot](out.png?raw=true "Output Screenshot")

