#Ethan Ruiz
import socket
import threading

def Connect(ip, port, _wait, output):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(_wait)
    try:
        sock.connect((ip, port))
        output[port] = 'Open'
    except:
        output[port] = 'x'

def Scan(host, _wait):
    current_threads = []
    output = {}

    for port in range(1, 65535):	# Create Thread
        t = threading.Thread(target= Connect, args=(host, port, _wait, output))
        current_threads.append(t)

    for port in range(1, 65535):	# Start Thread
        current_threads[port].start()

    for port in range(1, 65535): # Joining threads
        current_threads[port].join()

    for port in range(1, 65535): #  Output Open Ports
        if output[port] == 'Open':
            print(str(port) + ': ' + output[port])


def check_ip(host):
    a = host.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def main():
	while True:
		host = input("Enter Scanning Target: ")
		if check_ip(host) == False:
			print('Please enter a valid ip')
			host = input("Enter Scanning Target: ")
			break
		elif check_ip(host) == True:
			break

	_wait = int(input("Enter seconds before timeout: "))
	Scan(host, _wait)

if __name__ == "__main__":
    main()
