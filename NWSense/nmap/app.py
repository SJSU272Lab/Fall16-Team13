from NmapScan import IPScan
import datetime
import getIPAddr
import config
import json


#get registered mac addresses
registered_macs = [mac.rstrip('\n') for mac in open(config.registered_macs,'r')]

ipScan = IPScan()
online_hosts = ipScan.getOnlineHosts()

#print ('Found %s hosts up :\n' %len(online_hosts))

#output to connection_report.txt
#output = open('connection_report.txt','a')
#output.write('Scan at : %s.\n'%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#elapse = ipScan.getScanTime()
#output.write('\tTotal time scan : %d h : %d minutes : %d seconds.\n'%(elapse) )
#output.write('\tFound %s hosts up :\n' %len(online_hosts))

unregistered = []

#output.write('\t\tRegistered devices :\n')
for host in online_hosts:
#    h = host[0]
    m = host[1]
    if m not in registered_macs:
        unregistered.append(host[1])
suspiciousMacs = {}
suspiciousMacs["userId"] = "b539ab74bc9bc3e43a4b40040a66fa35"
suspiciousMacs["suspiciousMacs"] = []
for mac in unregistered:
    m = {}
    m["type"] = "unknown"
    m["addr"] = str(mac)
    suspiciousMacs["suspiciousMacs"].append(m)
    
if len(suspiciousMacs["suspiciousMacs"]) >0:
    print json.dumps(suspiciousMacs)

#        output.write('\t\t\t'+ h +  "\t:   " + m + '\n')
#        print ('\t'+ h + '\t:  ' + m + "\t:  registered")
#        print (m + "\t:  registered")
#    else:
        

#output.write('\t\tSuspicious devices :\n')
#print('\n')
#for host in unregistered:
#    h = host[0]
#    m = host[1]
#    output.write('\t\t\t'+ h +  "\t:   " + m + '\n')
#    print ('\t' + h + '\t:  ' + m + "\t:  SUSPICIOUS") 

#output.write('\n')
#output.close()

