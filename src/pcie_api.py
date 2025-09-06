import subprocess
import re

class PCIeAPI:

    @staticmethod
    def ListDevices():
        print("[ListDevices] Listing all PCIe devices...")
        output = subprocess.getoutput("lspci")
        print(output)
        return output

    @staticmethod
    def DeviceInfo(device_id):
        print(f"[DeviceInfo] Getting details for PCIe device: {device_id}")
        output = subprocess.getoutput(f"lspci -v -s {device_id}")
        print(output)

    @staticmethod
    def CheckLinkSpeed(device_id):
        print(f"[CheckLinkSpeed] Checking link speed and width for device {device_id}...")
        try:
            output = subprocess.getoutput(f"lspci -vv -s {device_id}")
            speed = re.search(r"LnkSta:.*Speed (\S+), Width x(\d+)", output)
            if speed:
                print(f"  Link Speed: {speed.group(1)}")
                print(f"  Link Width: x{speed.group(2)}")
            else:
                print("  Could not determine link speed or width.")
        except Exception as e:
            print(f"[CheckLinkSpeed] Error: {e}")

    @staticmethod
    def CheckAERStatus():
        print("[CheckAERStatus] Checking AER (Advanced Error Reporting) status...")
        try:
            output = subprocess.getoutput("dmesg | grep -i aer")
            if output:
                print("  AER Errors Found:\n", output)
            else:
                print("  No AER errors found.")
        except Exception as e:
            print(f"[CheckAERStatus] Error: {e}")

    @staticmethod
    def CheckBARs(device_id):
        print(f"[CheckBARs] Checking Base Address Registers (BARs) for {device_id}...")
        output = subprocess.getoutput(f"lspci -vv -s {device_id}")
        bar_lines = [line for line in output.split('\n') if 'Memory at' in line or 'I/O ports at' in line]
        if bar_lines:
            print("\n".join(bar_lines))
        else:
            print("  No BARs found or device not found.")
