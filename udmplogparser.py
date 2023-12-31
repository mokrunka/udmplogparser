from datetime import datetime

# open up the raw logfile (/var/log/udmp/udmplogs.log on the UDMP) and look for dropped traffic
# For reference, UDMP firewall logfile location: /var/log/ulog/syslogemu.log, .log.1, .log.2, .log.3

log_file_list = ['/var/log/udmp/udmplogs.log']

# for debugging, uncomment if desired
with open(r'/home/mokrunka/Documents/diditrun.log', "a") as logger:
    logger.write(f"{datetime.now()} YES - START\n")
    logger.close()

for log_file in log_file_list:
    with open(log_file, "r", encoding='latin-1') as f:
        lines = f.readlines()
        for line in lines:
            # if we find dropped packets, write (append) those to a separate log file
            if ('LAN_IN' in line) or ('LAN_LOCAL' in line):
                line.strip()
                with open(r'/home/mokrunka/Documents/parsedUDMPlogs.log', "a") as logfile:
                    logfile.write(line)
                logfile.close()
            else:
                pass
    f.close()

# for debugging, uncomment if desired
with open(r'/home/mokrunka/Documents/diditrun.log', "a") as logger:
    logger.write(f"{datetime.now()} YES - END\n")
    logger.close()