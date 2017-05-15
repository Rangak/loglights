# loglights
Cleanup and highlight events in Fabric peer and orderer logs



usage: loglights.py [-h] [-d DEPTH] [-p PRECISION] logfile

Extract Hyperledger Fabric Logfile Highlights

positional arguments:
  logfile               Name of Fabric logfile

optional arguments:
  -h, --help            show this help message and exit
  -d DEPTH, --depth DEPTH
                        Number of lines of event to show
  -p PRECISION, --precision PRECISION
                        Timestamp precision, sub second decimal places


Example:

    Create the logfile with timestamp option 

    # docker logs -t 11164e35484e >& ordererlogfile

Process through loglights

    # loglights ordererlogfile



Output:

19:11:44.06    orderer/main          main -> INFO 001 Starting orderer with TLS enabled
19:11:44.10    bccsp_sw              openKeyStore -> DEBU 002 KeyStore opened at [/var/hyperledger/orderer/msp/keystore]...done
19:11:44.11    orderer/main          createLedgerFactory -> DEBU 019 Ledger dir: /var/hyperledger/production/orderer
19:11:44.12    fsblkstorage          indexBlock -> DEBU 027 Indexing block [blockNum=0, blockHash=[]byte{0x69, 0x3f, 0x6e, 0x70, 0x7c, 0x18, 0x9a, 0xaf, 0x58, 0x94, 0x
19:11:44.13    policies              CommitProposals -> DEBU 098 In commit adding relative sub-policy Org2MSP/Readers to SampleConsortium
19:30:53.85    orderer/main          Deliver -> DEBU 0df Starting new Deliver handler
19:30:53.86    policies              ProposePolicy -> DEBU 11d Proposed new policy ChannelCreationPolicy for Application
19:30:53.87    msp/identity          newIdentity -> DEBU 1ef Creating identity instance for ID &{Org2MSP 450a72805c31162509087a15b86e64e1a99837cb52d918a510d2f697005a88
19:30:53.88    msp/identity          newIdentity -> DEBU 27a Creating identity instance for ID &{Org2MSP 7c6e21f4b51123c830927119c3ef6f43fc5e90b9a4e0d5888f4f2e6dbda9bc
19:30:53.89    policies              ProposePolicy -> DEBU 358 Proposed new policy Admins for Org1MSP
19:30:53.90    policies              CommitProposals -> DEBU 436 In commit adding relative sub-policy Org2MSP/Admins to Application
19:30:53.91    common/configtx       addToMap -> DEBU 49e Adding to config map: [Values] /Channel/Orderer/BatchTimeout
19:30:53.92    common/config         validateMSP -> DEBU 58b Setting up MSP for org OrdererOrg
19:30:53.93    policies              CommitProposals -> DEBU 647 As expected, current configuration has policy '/Channel/Application/Writers'
19:30:53.94    common/config         NewStandardValues -> DEBU 709 Initializing protos for *config.ChannelProtos
19:30:53.95    msp/identity          Sign -> DEBU 7db Sign: digest: F9B709A62F8E8F15FA9EBD4A2936C1329E69A1090A7F3A7EF0D206AC27D20333 
19:30:54.11    policies              GetPolicy -> DEBU 7e6 Returning policy Readers for evaluation
19:31:00.18    orderer/main          Deliver -> DEBU 7fe Starting new Deliver handler
19:31:02.45    orderer/main          Deliver -> DEBU 814 Starting new Deliver handler
19:31:02.46    msp/identity          newIdentity -> DEBU 871 Creating identity instance for ID &{OrdererMSP 863cb587854cbc20881fd8c36279b6e2091882dc64985f7c1d2ac5cc0b2
19:31:02.47    common/configtx       processConfig -> DEBU 8ad Beginning new config for channel mychannel
19:31:02.48    cauthdsl              func2 -> DEBU 910 Principal matched by identity: (&{0}) for [10 7 79 114 103 49 77 83 80 18 152 6 45 45 45 45 45 66 69 71 73 78 32
19:31:02.50    common/configtx       processConfig -> DEBU 938 Beginning new config for channel mychannel
19:31:02.51    policies              GetPolicy -> DEBU a24 Returning policy Orderer/BlockValidation for evaluation
19:31:02.57    orderer/main          Deliver -> DEBU a47 Starting new Deliver handler
19:31:02.58    orderer/main          Broadcast -> DEBU a4a Starting new Broadcast handler
19:31:02.59    msp/identity          newIdentity -> DEBU aa5 Creating identity instance for ID &{OrdererMSP 9e89a19cd98d4b216c87df2acf0f6889eb77bff9a18e61b0862ae8c3172
19:31:02.60    cauthdsl              func1 -> DEBU ad7 Gate evaluation starts: (&{n:1 policies:<signed_by:0 > })
19:31:02.61    msp/identity          newIdentity -> DEBU b1e Creating identity instance for ID &{OrdererMSP 9e89a19cd98d4b216c87df2acf0f6889eb77bff9a18e61b0862ae8c3172
19:31:02.63    msp/identity          Verify -> DEBU b6c Verify: digest = 00000000  ab 59 c5 c1 4e f4 72 21  e6 64 e5 58 19 bf fb ff  |.Y..N.r!.d.X....|
19:31:02.64    msp                   Setup -> DEBU c0e Setting up the MSP manager (3 msps)
19:31:04.33    orderer/main          Deliver -> DEBU c7a Starting new Deliver handler
19:31:04.34    cauthdsl              func2 -> DEBU c8f Principal matched by identity: (&{0}) for [10 7 79 114 103 50 77 83 80 18 213 6 45 45 45 45 45 66 69 71 73 78 32
19:31:06.40    orderer/main          Deliver -> DEBU ca0 Starting new Deliver handler
19:31:06.41    cauthdsl              func1 -> DEBU ca9 Gate evaluation fails: (&{n:1 policies:<signed_by:0 > })
19:31:07.91    orderer/main          Broadcast -> DEBU cc6 Starting new Broadcast handler
19:31:24.18    orderer/common/broadcast  Handle -> DEBU cc8 Broadcast is filtering message of type ENDORSER_TRANSACTION for channel mychannel
19:31:24.19    cauthdsl              func2 -> DEBU cd1 Principal evaluation starts: (&{0}) (used [false])
19:31:26.19    orderer/solo          main -> DEBU cef Batch timer expired, creating block
19:31:43.71    orderer/main          Broadcast -> DEBU d15 Starting new Broadcast handler
19:31:43.72    orderer/common/broadcast  Handle -> DEBU d17 Broadcast is filtering message of type ENDORSER_TRANSACTION for channel mychannel
19:31:45.72    orderer/solo          main -> DEBU d32 Batch timer expired, creating block
19:31:45.73    msp                   GetDefaultSigningIdentity -> DEBU d3a Obtaining default signing identity
19:38:44.39    orderer/main          Deliver -> DEBU d53 Starting new Deliver handler
19:38:45.21    orderer/main          Deliver -> DEBU d6f Starting new Deliver handler
19:38:45.22    msp                   Validate -> DEBU d7d MSP Org1MSP validating identity
NumLines :3460
NumEvents :46


