import socket

if __name__ == "__main__":
 host_name = "www.harvoxx.com"
 address = socket.gethostbyname(host_name)
 print(
    f"the ip address for {host_name} is {address}"
 )