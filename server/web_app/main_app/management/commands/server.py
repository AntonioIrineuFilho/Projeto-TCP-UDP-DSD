from django.core.management.base import BaseCommand
import socket
import threading
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

HOST = "0.0.0.0" # aceitar conexões internas no container Docker, caso rodar local mudar para 127.0.0.1
TCP_PORT = 6000
UDP_PORT = 5000


class Command(BaseCommand):
    help = "Inicia servidor TCP e UDP para sensores"

    def handle(self, *args, **kwargs):
        threading.Thread(target=self.tcp_server, daemon=True).start()
        threading.Thread(target=self.udp_server, daemon=True).start()

        self.stdout.write(self.style.SUCCESS("Servidor TCP/UDP iniciado"))
        threading.Event().wait()

    def tcp_server(self):
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.bind((HOST, TCP_PORT))
        tcp_sock.listen()

        print(f"[TCP] Escutando na porta {TCP_PORT}")

        while True:
            conn, addr = tcp_sock.accept()
            print(f"[TCP] Conectado: {addr}")

            data = conn.recv(1024).decode()
            if data.startswith("REGISTER"):
                conn.sendall(b"OK")
            else:
                conn.sendall(b"ERROR")

            conn.close()

    def udp_server(self):
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock.bind((HOST, UDP_PORT))

        print(f"[UDP] Escutando na porta {UDP_PORT}")

        channel_layer = get_channel_layer()

        while True:
            data, addr = udp_sock.recvfrom(4096)
            payload = json.loads(data.decode())

            async_to_sync(channel_layer.group_send)(
                "sensors",
                {
                    "type": "sensor.message",
                    "payload": payload
                }
            )
