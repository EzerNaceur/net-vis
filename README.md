# Network Visualizer

## Project Description

The Network Visualizer project provides a way to visualize network flows using Google Maps. It processes network traffic data captured using Wireshark, extracts source and destination IP addresses, and generates a KML file that can be viewed in Google Maps. This visualization helps in understanding network traffic patterns and identifying the geographical location of IP addresses involved in the network flow.

## Components

- **net-vis.py**: The main script that processes the network data and generates the KML file.
- **GeoLiteCity-data**: A submodule containing the GeoLiteCity database used for IP geolocation.

## Prerequisites

- Python 3.x
- Wireshark (for capturing network traffic)
- Git (for cloning the repository and submodules)
- Internet connection (for accessing IP geolocation data)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/network-visualizer.git
   cd network-visualizer
   ```
2. **Initialize and Update Submodule**

The project uses the GeoLiteCity-data submodule for IP geolocation. Initialize and update the submodule using the following commands:

```bash
git submodule init
git submodule update
```
3. **Install Required Python Packages**

Make sure to install the required Python packages. You can use pip for this:

```bash
    pip install -r requirements.txt
```
## Usage

1. **Capture Network Traffic**

Use Wireshark to capture network traffic and save the capture file as tcpdump.pcap.

2. **Run the Script**

Run the net-vis.py script with your IP address as an argument. Replace your_ip_address with your actual IP address.

```bash
    python net-vis.py your_ip_address
```

The script will process the tcpdump.pcap file and generate a network_visualization.kml file.

3. **View the KML File**

    Open the generated result.kml file with [Google Maps](https://www.google.com/mymaps) to visualize the network flow.

## Example

```bash
python net-vis.py 192.168.1.1
```

## Contributing

Fork the repository.
Create a new branch: git checkout -b feature-branch.
Make your changes and commit them: git commit -m 'Add some feature'.
Push to the branch: git push origin feature-branch.
Submit a pull request.

## License

This project is licensed under the GNU License. See the LICENSE file for details.

## Acknowledgements

The project uses the GeoLiteCity database for IP geolocation.
Thanks to the developers of Wireshark for providing a powerful network traffic analyzer.

## Contact

For any questions or suggestions, please contact [ezernaceur@gmail.com].
