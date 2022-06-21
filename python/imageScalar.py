import os
import sys
import cv2

# args -> rawDir exportDir sizes... (500x500xjpg)
def main():

    # initial setup
    if sys.argv == None:
        os.system("pip install opencv-python")
        print("Opencv Installed, Run with args")
        sys.exit(0)
    
    sys.argv.pop(0)

    # creating dictionary for directories
    dirs = {
        "raw" : sys.argv[0],
        "export" : sys.argv[1]
    }

    sys.argv.pop(0)
    sys.argv.pop(0)

    # storing scale data in a single array
    scaleData = []

    for i in sys.argv:
        cache = i.split("x")
        scaleData.append([int(cache[0]), int(cache[1]), cache[2]])

    sys.argv.clear()

    # loading image into memory
    RAW = cv2.imread(dirs["raw"])

    # resizing and saving scaled image
    for i in scaleData:
        cv2.imwrite(dirs["export"] + "{0}x{1}".format(i[0], i[1]) + "." + i[2], cv2.resize(RAW, (i[0], i[1]), interpolation = cv2.INTER_AREA))

if __name__ == "__main__":
    main()