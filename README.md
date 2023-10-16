# internet-sonification
Python script for TCP Sonification with Max/MSP and Ableton Live

This repository contains a Python script for scraping TCP packets using Scapy and sending relevant information to Max/MSP for sonification. The sonified data can be further integrated into Ableton Live for a unique audiovisual experience.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- [Scapy](https://scapy.net/)
- [python-osc](https://pypi.org/project/python-osc/)
- [Max/MSP](https://cycling74.com/products/max)
- Ableton Live

## Setup

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/tcp-sonification.git
    ```

2. Install the required Python packages:

    ```bash
    pip install scapy python-osc
    ```

3. Open the `tcp_sonification.py` script and modify the following variables:

    - `Host_IP`: Set this to the IP address where Max/MSP is running.
    - `iFace`: Choose the network interface to capture TCP packets.

4. Customize the `filter_str` variable based on your specific needs. The provided example filters packets for host `140.82.121.4` on port `443`.

## Usage

1. Run the Python script:

    ```bash
    python tcp_sonification.py
    ```

   This will start capturing and analyzing TCP packets, sending relevant information to Max/MSP.

2. Open the Max/MSP patch provided (`tcp_sonification.maxpat`) in Max/MSP.

3. In Ableton Live, import the Max/MSP patch as a Max for Live device.

4. Configure the Max for Live device to receive data from Max/MSP and map the incoming data to sound parameters.

5. Play around with the parameters in Ableton Live to create unique sonifications based on the captured TCP packet information.

## Additional Notes

- Ensure that Max/MSP is running and configured to receive UDP messages on the specified ports (`1120` to `1125` in the provided example).

- Customize the sonification process in Max/MSP according to your preferences and creative goals.
