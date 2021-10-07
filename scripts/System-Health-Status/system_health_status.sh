#!/bin/bash

function sysstat {
  S="\n******************************************************************************************************************"
  D="----------------------------------------------------------------------------------------------------------------"
  COLOR="y"

  MOUNT=$(mount | egrep -iw "ext4|ext3|xfs|gfs|gfs2|btrfs" | grep -v "loop" | sort -u -t' ' -k1,2)
  FS_USAGE=$(df -PThl -x tmpfs -x iso9660 -x devtmpfs -x squashfs | awk '!seen[$1]++' | sort -k6n | tail -n +2)
  IUSAGE=$(df -iPThl -x tmpfs -x iso9660 -x devtmpfs -x squashfs | awk '!seen[$1]++' | sort -k6n | tail -n +2)

  if [ $COLOR == y ]; then
    {
      GCOLOR="\e[47;32m ------ OK/HEALTHY \e[0m"
      WCOLOR="\e[43;31m ------ WARNING \e[0m"
      CCOLOR="\e[47;31m ------ CRITICAL \e[0m"
    }
  else
    {
      GCOLOR=" ------ OK/HEALTHY "
      WCOLOR=" ------ WARNING "
      CCOLOR=" ------ CRITICAL "
    }
  fi

  echo -e "$S"
  echo -e "\n \t\t\t\t\t\tSystem Health Status"
  echo -e "$S"

  #--------Print Operating System Details--------#
  echo -e "\n Operating System Details"
  hostname -f &>/dev/null && printf "\n Hostname : $(hostname -f)" || printf "Hostname : $(hostname -s)"

  echo -en "\n Operating System : "
  [ -f /etc/os-release ] && echo $(egrep -w "NAME|VERSION" /etc/os-release | awk -F= '{ print $2 }' | sed 's/"//g') || cat /etc/system-release

  echo -e " Kernel Version :" $(uname -r)
  printf " OS Architecture :" $(arch | grep x86_64 &>/dev/null) && printf " 64 Bit OS\n" || printf " 32 Bit OS\n"

  #--------Print system uptime-------#
  UPTIME=$(uptime)
  echo -en " System Uptime : "
  echo $UPTIME | grep day &>/dev/null
  if [ $? != 0 ]; then
    echo $UPTIME | grep -w min &>/dev/null && echo -en " $(echo $UPTIME | awk '{print $2" by "$3}' | sed -e 's/,.*//g') minutes" ||
      echo -en " $(echo $UPTIME | awk '{print $2" by "$3" "$4}' | sed -e 's/,.*//g') hours"
  else
    echo -en $(echo $UPTIME | awk '{print $2" by "$3" "$4" "$5" hours"}' | sed -e 's/,//g')
  fi
  echo -e "\n Current System Date & Time : "$(date +%c)
  echo -e "$S"

  #--------Check for any read-only file systems--------#
  echo -e "\n Checking For Read-only File System[s]\n"
  #echo -e "$D"
  echo " $MOUNT" | grep -w \(ro\) && echo -e "\n .....Read Only file system[s] found" || echo -e " .....No read-only file system[s] found. "
  echo -e "$S"

  #--------Check for currently mounted file systems--------#
  echo -e "\n Checking For Currently Mounted File System[s]\n"
  #echo -e "$D"
  echo " $MOUNT" | column -t
  echo -e "$S"

  #--------Check disk usage on all mounted file systems--------#
  echo -e "\n Checking For Disk Usage On Mounted File System[s]\n"
  echo -e "$D"
  echo -e " \t\t( 0-85% = OK/HEALTHY,  85-95% = WARNING,  95-100% = CRITICAL )"
  echo -e "$D"
  echo -e "\n Mounted File System[s] Utilization (Percentage Used):"

  COL1=$(echo "$FS_USAGE" | awk '{print $1 " "$7}')
  COL2=$(echo "$FS_USAGE" | awk '{print $6}' | sed -e 's/%//g')

  for i in $(echo "$COL2"); do
    {
      if [ $i -ge 95 ]; then
        COL3=" $(echo -e $i"% $CCOLOR\n$COL3")"
      elif [[ $i -ge 85 && $i -lt 95 ]]; then
        COL3=" $(echo -e $i"% $WCOLOR\n$COL3")"
      else
        COL3=" $(echo -e $i"% $GCOLOR\n$COL3")"
      fi
    }
  done

  COL3=$(echo "$COL3" | sort -k1n)
  paste <(echo "$COL1") <(echo "$COL3") -d' ' | column -t
  echo -e "$S"

  #--------Check for any zombie processes--------#
  echo -e " \n Checking For Zombie Processes\n"
  #echo -e "$D"
  ps -eo stat | grep -w Z 1>&2 >/dev/null
  if [ $? == 0 ]; then
    echo -e " Number of zombie process on the system are :" $(ps -eo stat | grep -w Z | wc -l)
    echo -e "\n  Details of each zombie processes found   "
    echo -e "  $D"
    ZPROC=$(ps -eo stat,pid | grep -w Z | awk '{print $2}')
    for i in $(echo "$ZPROC"); do
      ps -o pid,ppid,user,stat,args -p $i
    done
  else
    echo -e " No zombie processes found on the system."
  fi
  echo -e "$S"

  #--------Check Inode usage--------#
  echo -e "\n Checking For Inode Usage\n"
  echo -e "$D"
  echo -e " \t\t( 0-85% = OK/HEALTHY,  85-95% = WARNING,  95-100% = CRITICAL )"
  echo -e "$D"
  echo -e "\n Inode Utilization (Percentage Used) : \n"

  COL11=$(echo " $IUSAGE" | awk '{print $1" "$7}')
  COL22=$(echo " $IUSAGE" | awk '{print $6}' | sed -e 's/%//g')

  for i in $(echo "$COL22"); do
    {
      if [[ $i = *[[:digit:]]* ]]; then
        {
          if [ $i -ge 95 ]; then
            COL33=" $(echo -e $i"% $CCOLOR\n$COL33")"
          elif [[ $i -ge 85 && $i -lt 95 ]]; then
            COL33=" $(echo -e $i"% $WCOLOR\n$COL33")"
          else
            COL33=" $(echo -e $i"% $GCOLOR\n$COL33")"
          fi
        }
      else
        COL33=" $(echo -e $i"% (Inode Percentage details not available)\n$COL33")"
      fi
    }
  done

  COL33=$(echo "$COL33" | sort -k1n)
  paste <(echo "$COL11") <(echo "$COL33") -d' ' | column -t
  echo -e "$S"

  #--------Check for SWAP Utilization--------#
  echo -e "\n Checking SWAP Details\n"
  #echo -e "$D"
  echo -e " Total Swap Memory in MiB : " $(grep -w SwapTotal /proc/meminfo | awk '{print $2/1024}')", in GiB : " \
  $(grep -w SwapTotal /proc/meminfo | awk '{print $2/1024/1024}')
  echo -e " Swap Free Memory in MiB : " $(grep -w SwapFree /proc/meminfo | awk '{print $2/1024}')", in GiB : " \
  $(grep -w SwapFree /proc/meminfo | awk '{print $2/1024/1024}')
  echo -e "$S"

  #--------Check for Processor Utilization (current data)--------#
  echo -e "\n Checking For Processor Utilization"
  #echo -e "$D"
  echo -e "\n Current Processor Utilization Summary :\n"
  mpstat | tail -2
  echo -e "$S"

  #--------Check for load average (current data)--------#
  echo -e "\n Checking For Load Average\n"
  #echo -e "$D"
  echo -e " Current Load Average : $(uptime | grep -o "load average.*" | awk '{print $3" " $4" " $5}')"
  echo -e "$S"

  #------Print most recent 3 reboot events if available----#
  echo -e "\n Most Recent 3 Reboot Events\n"
  #echo -e "$D"
  last -x 2>/dev/null | grep reboot 1>/dev/null && /usr/bin/last -x 2>/dev/null | grep reboot | head -3 ||
    echo -e "\n No reboot events are recorded."
  echo -e "$S"

  #------Print most recent 3 shutdown events if available-----#
  echo -e "\n Most Recent 3 Shutdown Events\n"
  #echo -e "$D"
  last -x 2>/dev/null | grep shutdown 1>/dev/null && /usr/bin/last -x 2>/dev/null | grep shutdown | head -3 ||
    echo -e " No shutdown events are recorded."
  echo -e "$S"

  #--------Print top 5 Memory & CPU consumed process threads---------#
  #--------excludes current running program which is hwlist----------#
  echo -e "\n Top 5 Memory Resource Hog Processes\n"
  #echo -e "$D"
  ps -eo pmem,pid,ppid,user,stat,args --sort=-pmem | grep -v $$ | head -6 | sed 's/$/\n/'
  echo -e "$S"

  echo -e "\n Top 5 CPU Resource Hog Processes\n"
  #echo -e "$D"
  ps -eo pcpu,pid,ppid,user,stat,args --sort=-pcpu | grep -v $$ | head -6 | sed 's/$/\n/'
  echo -e "$S"

  echo -e "\n NOTE:- If any of the above fields are marked as \"blank\" or \"NONE\" or \"UNKNOWN\" or \"Not Available\" or \"Not Specified\"
that means either there is no value present in the system for these fields, otherwise that value may not be available,
or suppressed since there was an error in fetching details."
}

FILENAME="health-$(hostname)-$(date +%y%m%d)-$(date +%H%M).txt"
GLOBAL=$(sysstat)

echo "$GLOBAL"

sysstat >$FILENAME
echo -e "$S"
echo -e "\n Reported file $FILENAME generated in current directory." $RESULT
echo -e "$S"

echo -e "\n Do you want to mail the health report of your system ? [ Y / N ] "
read ans

if [ $ans == 'Y' ] || [ $ans == 'y' ]; then
  echo -e " Enter your email : "
  read EMAIL
  #		EMAIL='crce.8960.ce@gmail.com'

  if [ "$EMAIL" != '' ]; then
    STATUS=$(which mail)
    if [ "$?" != 0 ]; then
      echo -e "\n The program 'mail' is currently not installed."
    else
      cat $FILENAME | mail -s "$FILENAME" $EMAIL
      echo -e "\n The System Health Report is mailed to $EMAIL"
    fi
  fi

fi
echo -e "$S"

