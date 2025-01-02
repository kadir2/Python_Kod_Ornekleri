import socket

# Sunucu Ayarları
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 54235))  # IP ve Port

print("Sunucu dinleniyor...")
while True:
    data, addr = server_socket.recvfrom(1024)  # 1024 byte'lık veri al
    print(f"Gelen veri: {data.decode()} Kaynak: {addr}")
