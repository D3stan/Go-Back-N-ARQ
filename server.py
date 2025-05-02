import socket as sk, time
import configparser

# Load configuration from config.ini
config = configparser.ConfigParser(inline_comment_prefixes=(';'))
config.read("config.ini")
port = int(config["SERVER"]["port"])

# Set up the UDP socket
s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
host = sk.gethostname()
ip = sk.gethostbyname(host)
s.bind((ip, port))  # Listening on this port

print("\n[✓] UDP Server initialized")
print(f"[i] Listening for messages on {ip}:{port}...\n")

message, client_addr = s.recvfrom(1024)
message = message.decode()

while True:
    index = int(message)
    current = index

    while True:
        if current < index:
            index = current  # Reset to beginning of current window
            
        if current == index:
            print(f"[✓] Bit {current + 1} received → Sending ACK...")
            s.sendto(f"{current}".encode(), client_addr)
            index += 1
            time.sleep(0.5)
        
        data, _ = s.recvfrom(1024)
        current = int(data.decode())
        print(f"[⇾] Received bit: {current + 1}")
            
        if current == 0:
            print("\n[•] Transmission ended\n" + "-"*48 + "\n")
            message = 0
            break
