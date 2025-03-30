import socket 
from fileclient import FileClient
print("this is the client!!")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "192.168.100.14"
port = 8789

client.connect((ip, port))

f = FileClient()


#f.send_file("ethernet.png", client)
#f.download_file("image_server.jpg", client)

files =  f.list_files("", client)

print(files)
print(type(files))


client.close()