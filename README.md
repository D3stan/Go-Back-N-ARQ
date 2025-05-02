# UDP Packet Transmission with Go-Back-N ARQ

This project implements a **Go-Back-N Automatic Repeat reQuest (ARQ)** protocol for reliable data transmission over a **UDP** connection. It consists of two main parts: a **Client** and a **Server**. The **Client** sends packets to the **Server** and waits for acknowledgments (ACKs) for each packet. If a packet is lost, the **Client** resends the window of packets. The **Server** retrieves the **Client's ip** automatically.
Note: lost packets are **client-side emulated**

## Features
- **Reliable UDP communication** using Go-Back-N ARQ.
- Configurable packet transmission settings (port, timeout, etc.) via a **`.ini`** configuration file.
- **Automatic retransmission** of lost packets based on ACK timeout.
- Ability to simulate packet loss for testing purposes.
- **Window-based transmission** to optimize the flow of data.

---

## 💾 Installation

### Prerequisites

Ensure you have the following installed:
- **Python 3.x**: The project is developed using Python 3.x.
- **Required Libraries**: The project depends on Python's `socket` and `configparser` libraries, which are built-in.

No additional packages are required.

---

## ⚙️ Configuration

The configuration is done via a simple `.ini` file. The `client ip` is left **blank** by default to let the script use your local ip, so it needs to be changed **only** if you with to connect to a remote server.

### `config.ini` Example

```ini
# Client settings
[CLIENT]
ip =
port = 1235
timeout = 3.0

# Server settings
[SERVER]
port = 1236
timeout = 3.0
```

---

## 🏃‍♂️‍➡️ Usage

1. **Install Python 3.7+** if not already installed.

2. **Clone the repository**:  
   `git clone https://github.com/D3stan/Go-Back-N-ARQ.git`  
   `cd Go-Back-N-ARQ`

3. **Configure the `.ini` file** (optional):  
   You can edit `config.ini` to specify different ports or timeouts. If left empty, default values will be used.

4. **Run the server** in one terminal:  
   `python server.py`

5. **Run the client** in another terminal:  
   `python client.py`

6. Follow the interactive prompts in the client to send packets to the server and test Go-Back-N ARQ.

---

## ❓ How It Works

This project implements the Go-Back-N ARQ protocol over UDP using Python:

- The **client** sends a user-specified number of packets with a given window size.  
- It simulates **packet loss** randomly to mimic unreliable transmission.  
- The **server** receives packets and sends back acknowledgments (ACKs).  
- If the client doesn't receive ACKs within the configured timeout, it **retransmits the entire window** starting from the base sequence number.  
- Successful transmission is logged with stats: number of packets sent, acknowledged, and lost.

Communication occurs over two UDP sockets defined in `config.ini`, defaulting to ports `1235` (client) and `1236` (server).

---

## 🛠️ Troubleshooting

### 1. Server not receiving packets

- **Check IP configuration**:  
  Make sure the `ip` that appears in the **client console** matches your machine’s local IP address. You can find it using `ipconfig` (Windows) or `ifconfig` / `ip a` (Linux/Mac).

- **Try setting the IP manually**:  
  If automatic detection doesn’t work, set the `ip` explicitly in `config.ini`, e.g.  
  `ip = 192.168.1.42`.

- **Firewall or antivirus**:  
  Temporarily disable or configure your firewall/antivirus to allow UDP traffic on the specified ports.

---

### 2. Socket bind error (`Address already in use`)

- **Port already bound**:  
  Ensure no other instance of the script or another program is already using the port specified in `config.ini`.

- **Change port**:  
  Modify the `port` in `config.ini` to a free one (e.g. 1240 or 1300).

---

### 3. No ACKs received (client stuck in timeout)

- **Check server status**:  
  Ensure `server.py` is running before `client.py`.

- **Confirm both scripts use matching ports**:  
  The `CLIENT`'s port + 1 should match the `SERVER` port (or vice versa).

- **Packet loss simulation**:  
  The simulation randomly drops packets. This might cause timeouts — it’s part of the protocol’s expected behavior.

---

### 4. INI file not parsed correctly

- **Empty fields**:  
  Leave fields blank only if a fallback is coded. Otherwise, provide valid values.

---

### 5. Output bugs or encoding errors

- **Use UTF-8 encoding**:  
  Always save your `.py` and `.ini` files in UTF-8 encoding format.

- **Console issues**:  
  Use a terminal that properly supports UTF-8 and ANSI characters (like Windows Terminal, VSCode terminal, or any Linux shell).