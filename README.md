# udmplogparser
Ubiquiti (Unifi Dream Machine Pro)

This program parses UDMP logfiles. It is recommended to setup a syslog server, so that the program can be run on the syslog server
against the log files, but this is not required. If you do not use a syslog server, you'll have to run the code locally to your Unifi
network application, and it may not be persistent across reboots.

As stated, first set up a syslog server in your UDMP network settings. Once this is set up, you can then configure
your syslog server using rsyslog. You will need to configure /etc/rsyslog.conf on the remote server. An example of the file I
used is in this repository. There are also numerous examples of rsyslog.conf files online.

This version assumes a log file is made available by rsyslog in '/var/log/udmp/udmplogs.log', then parses for any
dropped traffic subject to the firewall rules 'LAN-IN' or 'LAN-LOCAL' in the UDMP. If you wish to parse a log file in a
different location, you'll have to update the program with a new directory.

The reason for this script is mainly because the unifi device logs many items in the syslogs, and the browser-based tool
which notifies the user when firewall rules are triggered does not provide sufficient information to understand what is
being blocked. This program will provide the timestamp, the rule matched, source and destination IP, and MAC address of 
the devices in question. They can be viewed more easily in a file which parses out all unnecessary information.

NOTE: At some point, Ubiquiti moved the UDMP log files from /var/log/messages to /var/log/ulog/syslogemu.log.