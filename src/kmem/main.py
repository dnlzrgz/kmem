import socket


def main():
    server_socket = socket.create_server(
        ("localhost", 6379),
        reuse_port=True,
    )

    while True:
        conn, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                message = data.decode().strip()
                print(f"Received: {message}")

                if message.upper() == "PING":
                    response = "PONG\r\n"
                    conn.sendall(response.encode())
                    print("Sent: PONG")


if __name__ == "__main__":
    main()
