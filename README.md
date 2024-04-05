# ipv4-subnet-search
Method 1 - command line
search for minimum subnets which can accommodate give number os host machines
Usage: find_subnet.py IP_ADDRESS/SUBNET_MASK_LEN HOST1 HOST2 HOST3
Required libraries: ipaddress, tabulate
Tested under:
    macos Monterey 12.7
    python 3.11.3

Example:
![image](https://github.com/megatronComing/ipv4-subnet-search/assets/114308295/9a7b6e96-793c-4466-8a45-418e2ab92ca1)

Method 2 - URL
Start the web server by running find_subnet_web.py
Access the server by URL http://your.ip.addr/findsubnets/net:IP_ADDR/masklen:SUBNET_MASK_LEN/hosts:HOST_NUM1&HOST_NUM2&HOST_NUM2

e.g. http://your.ip.addr/findsubnets/net:192.168.0.1/masklen:24/hosts:30&5&28&7
