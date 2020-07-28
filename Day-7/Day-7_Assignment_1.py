port1= {21:"ftp",22:"ssh",23:"telnet",80:"http"} 
port2 = {value:key for key,value in port1.items()}
print(port2)
