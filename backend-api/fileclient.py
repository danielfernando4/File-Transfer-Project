import socket 
import os
import traceback

class FileClient():

    def __init__(self):
        pass

    def send_file(self, file_name: str, client: socket.socket):
        try:
            file_size = os.path.getsize(file_name)
            file_size = str(file_size)
            client.sendall(file_size.encode())
            client.recv(1024)
            client.sendall(file_name.encode())
            client.recv(1024)

            with open(file_name, "rb") as file:
                while True:
                    chunk = file.read(1024)
                    if not chunk:
                        break
                    client.sendall(chunk)
            print("file send to the server!!")
        except Exception as e:
            print("error sending file")
            print(e)
            traceback.print_exc()



    def download_file(self, file_name: str,  client: socket.socket):  
        try:
            file_size = int(client.recv(1024).decode())
            client.send("OK DOWNLOAD!!".encode())
            file_recv = 0
            with open(file_name, "wb") as file: 
                while(file_recv < file_size):
                    chunk = client.recv(1024)
                    if not chunk:
                        break
                    file.write(chunk)
                    file_recv += len(chunk)
            print("file downloaded!!")
        except Exception as e:
            print("download error!!")
            print(e)
            traceback.print_exc()



    def list_files(self, directory_name: str, client: socket.socket) -> list:
        try:
            list_files = b''

            while True:
                chunk = client.recv(1024)
                if not chunk:
                    break

                list_files += chunk
            
            return list_files.decode().split(",")
            
        except Exception:
            print("list error")
            return "error"