import cv2


def sketchImage(filename):
    """
    :param filename: pass the filename as parameter (Example: if file name is "example.jpg" then pass "example.jpg"
                     in the function
    :return:
    """
    image = cv2.imread(filename)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image

    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    file_prefix = filename.split(".")
    cv2.imwrite(f"{file_prefix[0]}_converted.jpg", pencil_sketch)


if __name__ == "__main__":
    sketchImage("example.jpg")
