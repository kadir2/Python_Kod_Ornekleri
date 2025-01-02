import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "Merhaba UDP!"
print("Mesaj göanderildi!")
for i in range(5):
    message = f"Merhaba UDP! {i*10} "
    client_socket.sendto(message.encode(), ('127.0.0.1', 54235))
    time.sleep(2)
client_socket.close()
