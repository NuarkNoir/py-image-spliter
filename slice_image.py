import os
import argparse
from PIL import Image


def main(image_path: str, fmt: str):
    if not os.path.exists(image_path):
        raise Exception("Image path should refer to existing image")
    try:
        img: Image.Image = Image.open(image_path) 
        cW, cH = map(int, fmt.split("x"))
        iW, iH = img.size
        sW, sH = iW // cW, iH // cH
        img_orig_name, img_ext = os.path.basename(image_path).rsplit(".", 1)
        img_root = os.path.dirname(image_path)
        for i in range(cW):
            for j in range(cH):
                print(f"Piece {i}x{j}...")
                area = (sW*i, sH*j, sW*(i+1), sH*(j+1))
                c_img = img.crop(area)
                c_img.save(f"{img_orig_name}_{i}x{j}.{img_ext}")        
    except:
        raise Exception("Invalid image or format passed")
    else:
        print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split image into pieces")
    parser.add_argument("image", type=str, help="image, to be split")
    parser.add_argument("-f", "--form", dest="fmt", help="split format (WxH; default: 1x1)", default="1x1")

    args = parser.parse_args()
    full_image_path = os.path.abspath(args.image)
    main(full_image_path, args.fmt)
