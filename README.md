# hardware_details
get_hardware_details.py will give all the hardware details of the machine

## Prerequisites

1. Python >= 3.6
2. Passwordless ssh connection is needed to all servers where we are going to get
   the hardware details.

## How to run

```console
$python get_hardware_details.py -f servers -c cmds.yaml
```

### Help options:

```console
$ python get_hardware_details.py -h
Usage: 
    get_hardware_details.py -f <server_file> -c <commands_file>
    

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -f SERVER_FILE, --file=SERVER_FILE
                        file which contains server names/ips
  -c CMDS_FILE, --cmds_file=CMDS_FILE
                        file which contains commands in yaml format
$
```

### Sample server file:

```console
$ cat servers 
server1
server2
$ 
```

### Sample commands file

```console
$ cat cmds.yaml 
---
TOTAL_RAM_SLOTS: "dmidecode --type 17 | grep 'Memory Device' --count"
FLASH_SLOTS: "dmidecode --type 17 | grep 'Flash' | wc -l"
DIMM SIZES: "dmidecode --type 17 | egrep 'Type|Size|Locator: D' | grep -i size | grep -v 'No Module Installed' | cut -d':' -f2 | tr '\n' ','| sed 's/.$//'"
TYPE: "dmidecode --type 17 | egrep 'Type|Size|Locator: D' | grep -i type: | egrep -v 'Unknown|Flash' | sort -u | awk '{ print $NF }'"
CURRENT_DISKS_POPULATED: "lsblk | grep -i disk | wc -l"
DISK_SIZES: "lsblk | grep -i disk | awk '{ print $4 '} | tr '\n' ','| sed 's/.$//'"
DISK_TYPE: "lsblk -d -o name,rota | egrep -v 'sr0|ROTA' | sed 's/1/-----> HD/' | sed 's/0/-----> SSD/' | tr '\n' ',' | sed 's/.$//'"
DISK_MODEL: "cat /sys/class/block/sd*/device/model  | sed 's/LOGICAL VOLUME/NA/' | sed 's/Flash Reader/NA/' | tr '\n' ', ' | sed 's/.$//'"
MAKE: "dmidecode | grep -A3 '^System Information' | grep -i Manufacturer | awk '{ print $NF }'"
MODEL: "dmidecode -s system-product-name"
SERIAL_NUMBER: "dmidecode -s system-serial-number"
```
