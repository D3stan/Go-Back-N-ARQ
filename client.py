import time, socket as sk
import random, configparser

# Read settings from config.ini
config = configparser.ConfigParser(inline_comment_prefixes=(';'))
config.read("config.ini")

# Extract port and timeout from the NETWORK section
port = int(config.get("CLIENT", "port", fallback=1235))
timeout = float(config.get("CLIENT", "timeout", fallback=3.0))

# Set up the UDP socket
s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
host = sk.gethostname()
ip = sk.gethostbyname(host)
s.bind((ip, port))
s.settimeout(timeout)

server_ip = config.get("CLIENT", "ip", fallback="").strip() or ip # checks if the value is missing or blank
server_port = port + 1
server_addr = (server_ip, server_port)

print("\n[UDP Client Initialized]")
print(f"Preparing to send packets to Server [{server_ip}:{server_port}]\n")

while True:
    num_packets = int(input("Enter the number of packets to send: "))
    window_size = int(input("Enter the window size: "))
    base = 0
    next_seq = 0
    window_end = base + window_size
    acked = [False] * num_packets

    # Statistics
    sent_packets = 0
    recieved_packets = 0
    lost_packets = 0


    while base < num_packets:
        # Send all packets in the window
        while next_seq < window_end and next_seq < num_packets:
            packet_lost = random.randint(0, 5) == 0

            if packet_lost:
                print(f"[X] Packet #{next_seq + 1} was lost!")
                lost_packets += 1
            else:
                s.sendto(str(next_seq).encode(), server_addr)
                print(f"[→] Sent packet #{next_seq + 1}")
                sent_packets += 1

            next_seq += 1
            time.sleep(0.5)

        # Try receiving ACKs
        try:
            for i in range(base, window_end):
                ack, _ = s.recvfrom(1024)
                ack_num = int(ack.decode())
                print(f"[✓] Received ACK for packet #{ack_num + 1}")
                recieved_packets += 1
                acked[i] = True
                base += 1
                window_end = base + window_size
                time.sleep(0.5)

        except sk.timeout:
            if all(acked):
                print("\n[✔] All packets successfully sent!")
                print(f"--- Transmission Summary ---")
                print(f"✓ Sent:     {sent_packets}")
                print(f"✓ Received: {recieved_packets}")
                print(f"✗ Lost:     {lost_packets}\n")
            else:
                print(f"\n[!] Timeout! No ACK received for packet {base}. Retrying current window...\n")

            next_seq = base  # Retransmit entire window

        time.sleep(1.5)
