## How to run
1. Clone the repo
   ```
   git clone git@github.com:GDSC-RCCIIT/General-Purpose-Scripts.git
   ```
2. Navigate to `QR Code Generator` directory
   ```
   cd General-Purpose-Scripts/scripts/QR\ Code\ Generator
   ```
3. Install the script requirements
   ```
   pip3 install -r requirements.txt
   ```
4. Run the script to generate QR Code for your link
   ```
   python3 qr_code_gen.py --link <link>
   ```
   Or,
   ```
   python3 qr_code_gen.py -l <link>
   ```
Replace <link> with the website URL.

The QR Code (in .png and .svg) will be generated in the `QR Code Generator` directory.

### Screenshots of the script
![CLI screen grab](https://i.imgur.com/f7YKruQ.png)