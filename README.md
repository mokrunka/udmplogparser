# udmplogparser
To parse firewall logs on UDMP

This file parses UDMP logs, which are setup previously to be pulled to a remote syslog server (I used rsyslog)

As stated, first set up a syslog server in your UDMP network settings. Once this is set up, you can then configure
the syslog server using rsyslog. You will need to configure /etc/rsyslog.conf on the remote server, as well as /etc/rsyslog.d/[yourconfname.conf].

This version assumes that logs are pulled on an hourly basis from /var/log/messages on the UDMP, and dumped into /var/log/udmplogfile.log, which this
code then parses for any dropped traffic internal to the LAN ('LAN-IN').
