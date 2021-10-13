# <b>Steganography<b>

## <ins>Installation</ins>
  1. Clone the repository to your local system
  2. Naviagate to the folder and run
  `pip install -r requirements.txt`  

## <ins>Usage</ins>
   Syntax: `python main.py [-m] [file_name]`<br>
   -m -> -e or encode to Encode, -d or decode to Decode<br>
    file_name -> Name of the image you wish to encode or decode
    <br><br>
1. <ins>To Encode<br></ins>
        Eg : `python main.py -e sample_pic.jpg`<br><br>
        After this you will be asked to enter the message:<br>
        `[*]Enter your Message: `<br><br>
        After successful completion of encoding, a file with syntax `file_name_encode.png` will be created.<br><br>
        Eg : `sample_pic_encoded.png`<br>
        This image file conatins the message.
    <br><br>
2. <ins>To decode<br></ins>
    Eg:`python main.py -d sample_pic_encoded.png`<br><br>
    After successful completion of decoding,The Decoded message will be visible on the terminal.

## <ins>DEMO</ins>
![image info](./resources/s1.jpg)
![image info](./resources/s2.jpg)