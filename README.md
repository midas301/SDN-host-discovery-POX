SDN Host Discovery Service

## Problem Statement
In traditional networking, host discovery is often decentralized. In Software-Defined Networking (SDN), we can centralize this by using the controller to monitor network traffic. This project implements a **Host Discovery Service** using the **POX Controller** and **Mininet**. The goal is to dynamically identify and maintain a database of all active hosts (MAC addresses) and their physical locations (Switch ID and Port) as they join the network.

## Objectives
- Demonstrate Controller-Switch interaction via OpenFlow.
- Handle `packet_in` events to extract host metadata.
- Maintain a dynamic, real-time host-to-port mapping database.
- Validate network behavior using Mininet and Wireshark.

## Prerequisites & Setup
### Environment
- **OS:** Debian (UTM Virtual Machine on macOS)
- **SDN Controller:** POX (Dart branch)
- **Network Emulator:** Mininet 2.3.0
- **Protocol:** OpenFlow 1.0

### Installation
1. **Clone POX:**
   ```bash
   git clone [https://github.com/noxrepo/pox](https://github.com/noxrepo/pox)
