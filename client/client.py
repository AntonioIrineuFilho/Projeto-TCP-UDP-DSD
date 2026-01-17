import socket
import json
import time
from datetime import datetime
import zoneinfo
import random

SERVER_HOST = "server" # nome do serviço no Docker, caso rodar local mudar para 127.0.0.1
TCP_PORT = 6000
UDP_PORT = 5000
SENSOR_ID = 1


def connect_tcp():
    for i in range(5):
        try:
            tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_sock.connect((SERVER_HOST, 6000))
            return tcp_sock
        except:
            print("Tentando novamente...")
            time.sleep(2)
    return None


def send_udp_data():
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data = {
            "sensor_id": SENSOR_ID,
            "temperature": round(random.uniform(20, 30), 1),
            "humidity": round(random.uniform(40, 50), 1),
            "timestamp": datetime.now(zoneinfo.ZoneInfo('America/Sao_Paulo')).strftime("%d-%m-%Y %H:%M:%S")
        }

        udp_sock.sendto(
            json.dumps(data).encode(),
            (SERVER_HOST, UDP_PORT)
        )

        time.sleep(5)  # envio periódico


if __name__ == "__main__":
    print("[SENSOR] Tentando conectar via TCP...")

    if connect_tcp():
        print("[SENSOR] Conectado e autorizado pelo servidor")
        print("[SENSOR] Enviando dados via UDP...")
        send_udp_data()
    else:
        print("[SENSOR] Falha na autorização")
