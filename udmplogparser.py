from datetime import datetime

# open up the raw logfile (/var/log/ulog/syslogemu.log on the UDMP) and look for rules that are dropped
# logfile names: /var/log/ulog/syslogemu.log, .log.1, .log.2, .log.3

log_file_list = ['/var/log/ulog/syslogemu.log']

# uncomment below for debugging
# with open(r'diditrun.log', "a") as logger:
#     logger.write(f"{datetime.now()} YES - START\n")
#     logger.close()

for log_file in log_file_list:
    with open(log_file, "r", encoding='latin-1') as f:
        lines = f.readlines()
        for line in lines:
            # if we find dropped packets, write (append) those to a separate log file
            if 'LAN_IN' in line:
                line.strip()
                with open(r'/home/kali/udmplogscript/droppedtrafficfromUDMPfirewall.log', "a") as logfile:
                    logfile.write(line)
                logfile.close()
            else:
                pass
    f.close()

# uncomment below for debugging
# with open(r'diditrun.log', "a") as logger:
#     logger.write(f"{datetime.now()} YES - END\n")
#     logger.close()
    