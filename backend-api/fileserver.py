import socket
import os
import traceback

class FileServer():

    def __init__(self):
        pass


    def recv_file_to_clien(self, server: socket.socket):
        try:
            file_size = int(server.recv(1024).decode())
            file_name = server.recv(1024).decode()

            size_rcv = 0
            with open(file_name, "wb") as file:
                while size_rcv < file_size:
                    chunk = server.recv(1024)
                    if not chunk:
                        break
                 
                    file.write(chunk)
                    size_rcv += len(chunk)
            print("file received")
        except Exception:
            print("receiving file error!!")


    

    def send_file_to_clien(self, file_name: str, server: socket.socket):
        try:
            file_size = os.path.getsize(file_name)
            file_size = str(file_size)
            server.sendall(file_size.encode())

            with open(file_name, "rb") as file: 
                while True:
                    chunk = file.read(1024)
                    if not chunk:
                        break
                    server.send(chunk)
            print("file sending to the client!!")

        except:
            print("server sending error")
            traceback.print_exc()



    def send_files(self, server: socket.socket):
        try:
            #list_files = server
            pass
        except Exception:
            print("server list files error")