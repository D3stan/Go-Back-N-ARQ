# UDP Packet Transmission with Go-Back-N ARQ

This project implements a **Go-Back-N Automatic Repeat reQuest (ARQ)** protocol for reliable data transmission over a **UDP** connection. It consists of two main parts: a **Client** and a **Server**. The **Client** sends packets to the **Server** and waits for acknowledgments (ACKs) for each packet. If a packet is lost, the **Client** resends the window of packets.

## Features
- **Reliable UDP communication** using Go-Back-N ARQ.
- Configurable packet transmission settings (port, timeout, etc.) via a **`.ini`** configuration file.
- **Automatic retransmission** of lost packets based on ACK timeout.
- Ability to simulate packet loss for testing purposes.
- **Window-based transmission** to optimize the flow of data.
  
## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Installation

### Prerequisites

Ensure you have the following installed:
- **Python 3.x**: The project is developed using Python 3.x.
- **Required Libraries**: The project depends on Python's `socket` and `configparser` libraries, which are built-in.

No additional packages are required.

---

## Configuration

Before running the scripts, you need to set the **IP** and **Port** values for both the **Client** and **Server** in the configuration file. The configuration is done via a simple `.ini` file.

### `config.ini` Example

```ini
[CLIENT]
# Client settings
ip = 127.0.0.1
port = 1235
timeout = 3.0

[SERVER]
# Server settings
port = 1236
timeout = 3.0
