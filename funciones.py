import logging
import getpass
import re
import datetime
import sys

try:
    import netmiko
except:
    print("Error Netmiko not installed - https://github.com/ktbyers/netmiko")
    sys.exit()

ips = ["172.17.64.130"]
un = "LAMCDCORP\AD124271"
pw = "Vd_6474874"
devices = []

for ip in ips:
    # device definition
    cisco_wlc = {
        'device_type': 'cisco_wlc',
        'ip': ip,
        'username': un,
        'password': pw,
    }
    devices.append(cisco_wlc)

for device in devices:
    logger.info("Connecting to %s", device['ip'])
    # connect to the device w/ netmiko
    try:
        net_connect = netmiko.ConnectHandler(**device)
    except:
        logger.error("Failed to connect to %s", device['ip'])
        logger.debug("Exception: %s", sys.exc_info()[0])
        continue

    # get the prompt as a string
    prompt = net_connect.find_prompt()

    logger.debug("prompt: %s", prompt)

    regex = r'^\((.*)\)[\s]>'

    regmatch = re.match(regex, prompt)
    if regmatch:
        hostname = regmatch.group(1)
        logger.info("Working on %s", hostname)
    else:
        logger.error("Hostname Not Found!")
        logger.debug(regmatch)

    filetime = datetime.datetime.now().strftime("%y%m%d-%H%M%S") # File timestamp
    config_filename = hostname + "_" + filetime + ".txt" # Filname with hostname
    files.append(config_filename)
    logger.info("Filename: %s", config_filename)

    commands = ['show ap sumary','show client state summary'] # commands to run

    for cmd in commands:
        logger.info("Sending cmd: %s", cmd)
        this_cmd = net_connect.send_command(cmd)
        config_filename_f = open(config_filename, 'a')
        config_filename_f.write(this_cmd)
        config_filename_f.write('\n')
        config_filename_f.close()

print("Finished:")
for fname in files:
    print(" %s " % fname)
