from pcie_api import PCIeAPI
import sys

def parse_command(line):
    tokens = line.strip().split()
    if not tokens or tokens[0].startswith("#"):
        return None, {}

    cmd = tokens[0]
    args = {}
    for token in tokens[1:]:
        if '=' in token:
            k, v = token.split('=', 1)
            args[k] = v
    return cmd, args

def run_test(file):
    with open(file, 'r') as f:
        for line in f:
            cmd, args = parse_command(line)
            if not cmd:
                continue

            try:
                if cmd == "ListDevices":
                    PCIeAPI.ListDevices()
                elif cmd == "DeviceInfo":
                    PCIeAPI.DeviceInfo(args["device_id"])
                elif cmd == "CheckLinkSpeed":
                    PCIeAPI.CheckLinkSpeed(args["device_id"])
                elif cmd == "CheckAERStatus":
                    PCIeAPI.CheckAERStatus()
                elif cmd == "CheckBARs":
                    PCIeAPI.CheckBARs(args["device_id"])
                else:
                    print(f"[ERROR] Unknown command: {cmd}")
            except Exception as e:
                print(f"[ERROR] {cmd} failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sudo python3 pcie_test_runner.py tests/pcie_validation.tst")
        sys.exit(1)

    run_test(sys.argv[1])
