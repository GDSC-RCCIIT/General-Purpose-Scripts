from PIL import Image

import sys
from os import path


def decode_image(image):
    try:
        pix = image.getdata()
        current_pixel = 0
        decoded = ""
        while True:
            # Get 3 pixels each time
            binary_value = ""
            p1 = pix[current_pixel]
            p2 = pix[current_pixel + 1]
            p3 = pix[current_pixel + 2]
            all_pixels = [val for val in p1 + p2 + p3]

            for i in range(0, 8):
                if all_pixels[i] % 2 == 0:
                    # add 0
                    binary_value += "0"
                elif all_pixels[i] % 2 != 0:
                    # add 1
                    binary_value += "1"

            # Convert binary value to ascii and add to string
            binary_value.strip()
            ascii_value = int(binary_value, 2)
            decoded += chr(ascii_value)
            current_pixel += 3

            if all_pixels[-1] % 2 != 0:
                # stop reading
                break

        return decoded

    except Exception as e:
        print("[*]An error occured\n%s" % e)
        sys.exit()


def encode_image(img, message, filename):
    try:
        width, height = img.size

        img_pix = img.getdata()

        curr_pixel = 0
        ch_count = 0

        x = 0
        y = 0
        for ch in message:

            ch_count = ch_count + 1

            binary_val = format(ord(ch), "08b")
            p1 = img_pix[curr_pixel]
            p2 = img_pix[curr_pixel + 1]
            p3 = img_pix[curr_pixel + 3]
            # print(f"p1:{p1},p2:{p2},p3:{p3}")
            all_pixels = [val for val in p1 + p2 + p3]
            # print(all_pixels)
            for i in range(8):
                bit = binary_val[i]

                if bit == "0":
                    if all_pixels[i] % 2 != 0:
                        all_pixels[i] = (
                            all_pixels[i] - 1
                            if all_pixels[i] == 255
                            else all_pixels[i] + 1
                        )
                elif bit == "1":
                    if all_pixels[i] % 2 == 0:
                        all_pixels[i] = (
                            all_pixels[i] - 1
                            if all_pixels[i] == 255
                            else all_pixels[i] + 1
                        )

            curr_pixel += 3

            # 1 ->stop reading
            if ch_count == len(message):
                if all_pixels[-1] % 2 == 0:
                    all_pixels[-1] = (
                        all_pixels[-1] - 1
                        if all_pixels[-1] == 255
                        else all_pixels[-1] + 1
                    )
            else:
                if all_pixels[-1] % 2 != 0:
                    all_pixels[-1] = (
                        all_pixels[-1] - 1
                        if all_pixels[-1] == 255
                        else all_pixels[-1] + 1
                    )

            all_pixels = tuple(all_pixels)
            st_pix = 0
            end_pix = 3
            for i in range(3):
                img.putpixel((x, y), all_pixels[st_pix:end_pix])
                st_pix += 3
                end_pix += 3

                if x == width - 1:
                    x = 0
                    y += 1
                else:
                    x += 1

        encoded_file = filename.split(".")[0] + "_encoded.png"
        img.save(encoded_file)

    except Exception as e:
        print(e)
        print("[*] Error Occured!!!")
        sys.exit(0)


def convertToRGB(img):
    try:
        rgba_image = img
        rgba_image.load()
        background = Image.new("RGB", rgba_image.size, (255, 255, 255))
        background.paste(rgba_image, mask=rgba_image.split()[3])
        print("[*] Converted to RGB.")
        return background
    except:
        print("[*]Couldn't convert image to RGB!")
        sys.exit(0)


def get_pixel_count(img):
    width, height = img.size
    return width * height


def main():
    try:
        op = sys.argv[1]  # operation
        file_name = sys.argv[2]  # Image name
    except:
        print("[*]Wrong Command_line arguments!")
        return

    # check if file is present
    if not path.exists(file_name):
        print("[*]file not found")
        return

    img = Image.open(file_name)

    if op in ("-e", "encode"):
        message = input("[*]Enter message:")
        print(">>>encoding....")

        # check if message can be injected
        if get_pixel_count(img) < len(message):
            print("[*]Message is too large to inject in the given image!!!")
            return

        img_mode = img.mode

        if img_mode != "RGB":
            img = convert_to_RGB(img)
        new_img = img.copy()

        encode_image(new_img, message, img.filename)
        print("[*]Encoded Successfully!")

    elif op in ("-d", "decode"):
        print(">>>decoding....")
        decode_msg = decode_image(img)
        print("[*]Decoded Message:")
        print(decode_msg)


if __name__ == "__main__":
    main()
