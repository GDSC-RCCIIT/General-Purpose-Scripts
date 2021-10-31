from tkinter.filedialog import *
import cv2


# ---------------saving the converted image-------------
def save_image(filename, sketch_type):
    file_prefix = filename.split(".")
    cv2.imwrite(f"{file_prefix[0]}_converted.jpg", sketch_type)


# -----------------image to pencil sketch-------------
def sketch_image(filename):
    image = cv2.imread(filename)
    image = cv2.resize(image, (300, 300))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image

    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    save_image(filename, pencil_sketch)


# -----------------image to cartoon sketch-------------
def cartoon_image(filename):
    img_rgb = cv2.imread(filename)
    img_rgb = cv2.resize(img_rgb, (300, 300))
    numDownSamples = 2  # number of downscaling steps
    numBilateralFilters = 50  # number of bilateral filtering steps

    # -----------downscale image using Gaussian pyramid-------
    img_color = img_rgb
    for _ in range(numDownSamples):
        img_color = cv2.pyrDown(img_color)

    # -------repeatedly apply small bilateral filter instead of applying one large filter------
    for _ in range(numBilateralFilters):
        img_color = cv2.bilateralFilter(img_color, 9, 9, 7)

    # ------------upscale image to original size------------------
    for _ in range(numDownSamples):
        img_color = cv2.pyrUp(img_color)

    # -----------convert to grayscale and apply median blur---------
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 3)

    # -------detect and enhance edges--------------
    img_edge = cv2.adaptiveThreshold(
        img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2
    )

    # ------convert back to color so that it can be bit-ANDed with color image------
    (x, y, z) = img_color.shape
    img_edge = cv2.resize(img_edge, (y, x))
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

    # ---------print img_edge.shape, img_color.shape----------
    res = cv2.bitwise_and(img_color, img_edge)

    save_image(filename, res)


if __name__ == "__main__":
    try:
        img_path = askopenfilename()

        while not img_path:
            img_path = askopenfilename()

        # -----option to choose between pencil sketch or cartoon sketch-------
        pref = int(
            input(
                """Press 1 or 2 
        1. pencil sketch
        2. cartoon sketch
        input -->  """
            )
        )

        if pref == 1:
            sketch_image(img_path)
        elif pref == 2:
            cartoon_image(img_path)

        print(
            """
        ****************************************************************
        Image created (check the {original_filename}_converted.jpg file)
        ****************************************************************"""
        )

    except Exception as e:
        print("Error occurred: ", e)
