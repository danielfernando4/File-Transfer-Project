import socket 

def create_client_sock() -> socket.socket:
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


def create_serv_sock(ip: str, port: int) -> socket.socket:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((str, int))
    return server