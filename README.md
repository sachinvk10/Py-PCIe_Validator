 Py-PCIe_Validator
 =================

This framework allows non-developers to run PCIe validation tests using `.tst` scripts without touching Python code.

## Features

- List all PCIe devices
- Inspect a device’s info
- Check PCIe link speed and width
- Read AER (Advanced Error Reporting) logs
- View BAR (Base Address Registers) configuration

## Use Cases

PCIe device enumeration
Link training validation
AER error detection
Device inspection before deployment

## DSL Commands

Command							Description
-------                         -----------
ListDevices						Lists all PCIe devices
DeviceInfo device_id=			Shows detailed info for device
CheckLinkSpeed device_id=		Displays PCIe link speed/width
CheckAERStatus					Scans kernel logs for AER errors
CheckBARs device_id=			Shows memory or I/O BARs of device


## Folder Structure

pcie_test_suite/
├── README.md
├── src/
│ ├── pcie_api.py
│ └── pcie_test_runner.py
└── tests/
└── pcie_validation.tst

## Run the Test

#sudo python3 src/pcie_test_runner.py tests/pcie_validation.tst




