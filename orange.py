from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class HostDiscovery(object):
    def __init__(self):
        core.openflow.addListeners(self)
        self.host_db = {} # Dictionary to store MAC -> (Switch, Port)

    def _handle_PacketIn(self, event):
        packet = event.parsed
        if not packet.parsed: return

        # Get details
        mac_addr = str(packet.src)
        port = event.port
        dpid = event.dpid

        # Discovery Logic
        if mac_addr not in self.host_db:
            self.host_db[mac_addr] = (dpid, port)
            log.info("FOUND NEW HOST: %s on Switch %s Port %s", mac_addr, dpid, port)
            self.show_table()

    def show_table(self):
        print("\n--- CURRENT DISCOVERED HOSTS ---")
        for mac, info in self.host_db.items():
            print(f"Host: {mac} | Location: Switch {info[0]}, Port {info[1]}")
        print("--------------------------------\n")

def launch():
    core.registerNew(HostDiscovery)
