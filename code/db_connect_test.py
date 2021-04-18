import psycopg2
from sshtunnel import SSHTunnelForwarder

def connect(ssh_user, ssh_pass, db, db_user, db_pass):
	"""
		Establish connection to csh server through sshtunnelforwarder,
		then connect to db with psycopg2 
	"""
	try:
			tunnel = SSHTunnelForwarder(
					('shell.csh.rit.edu', 22),
					ssh_username = ssh_user,  
					ssh_password = ssh_pass, 
					remote_bind_address = ('localhost', 8080)) 

			tunnel.start()
			print("Server connected")

			conn = psycopg2.connect(
					dbname = db,
					user = db_user,
					password = db_pass,
					host = '127.0.0.1',
					port = tunnel.local_bind_port)

			curs = conn.cursor()
			print("Database connected")
	except : 
		print("failed bruh")

def main():
	# Load in ssh and db creds
	config = open("creds.txt")
	ssh_user = ""
	ssh_pass = ""
	db = ""
	db_user = ""
	db_pass = ""
	i = 0
	for line in config:
		line = line.strip()
		if i == 0:
			ssh_user = line
		elif i == 1:
			ssh_pass = line
		elif i == 2:
			db = line
		elif i == 3:
			db_user = line
		elif i == 4:
			db_pass = line
		i += 1

	connect(ssh_user, ssh_pass, db, db_user, db_pass)

main()
