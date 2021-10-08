# SYSTEM HEALTH STATUS

<br>



## ABSTRACT

* The project aims for checking the Linux system health with a shell script.

* This is a short, lightweight script that gets the necessary information and status like hostname, kernel version, CPU, Uptime, memory/ disk usage using native Linux utilities
and doesn't take up much room.

* The Script uses hostname, uname, arch, uptime, cat, mpstat, ps, df, free, head commands to get system information and cut, grep, awk and sed for text processing.

* The output of the script is a text file that will be generated in the current directory.

* A variable is set to provide an email address to which the script can send the report file.

* Apart from system status, the script will check a predefined threshold for CPU load and filesystem size.
<br>

## RUN USING
### For Linux
* `chmod +x system_health_status.sh`
* `./system_health_status.sh`

### For Windows 
* `system_health_status.sh`
 
<br>

## RESULTS

<p align="center">
  <br>
  <kbd><img src="/scripts/System-Health-Status/images/output.png"></kbd>
</p>

 ## REFERENCES
 
 https://github.com/SimplyLinuxFAQ/health-check-script/
 https://www.tecmint.com/using-shell-script-to-automate-linux-system-maintenance-tasks/
 https://arief-jr.blogspot.com/2016/01/shell-script-for-check-linux-system_19.html
