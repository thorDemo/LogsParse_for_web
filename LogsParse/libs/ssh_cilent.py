
import paramiko
client = paramiko.SSHClient()

client.connect(hostname, port, username, password, timeout=10)
