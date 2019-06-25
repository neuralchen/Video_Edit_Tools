import os
import cv2
from tqdm import tqdm
import argparse
import imageio
import PIL
from PIL import Image

parser = argparse.ArgumentParser(description='translation images to video')

parser.add_argument('--imagePath', type=str, default="e:\\gif", help='path to your images')#, required=True)
parser.add_argument('--duration', type=float, default=0.1, help='gif duration')
parser.add_argument('--outputPath', type=str, default="./result.gif", help='path to the output gif file')
parser.add_argument('--sampleScale', type=float, default=0.8, help='sampling sale of your images')

args = parser.parse_args()


def main():
    path        = args.imagePath
    gifName     = args.outputPath
    duration    = args.duration
    sample_scale= args.sampleScale
    filelist    = os.listdir(path)
    test_image  = os.path.join(path, filelist[0])
    img         = cv2.imread(test_image, cv2.IMREAD_UNCHANGED)
    size        = img.shape[0:2]
    size        = (int(size[1]*sample_scale),int(size[0]*sample_scale))
    frames      = []
    filelist.sort(key=lambda x: os.path.getctime(os.path.join(path, x)))
    n = 0
    for img_idx,item in enumerate(tqdm(filelist)):
        if item.endswith('.png') and n%2==0: 
            print(item)
            item    = os.path.join(path, item)
            img     = imageio.imread(item)
            if sample_scale != 1.0:
                img     = cv2.resize(img, size, interpolation = cv2.INTER_CUBIC)
            frames.append(img)
        n += 1
    print("saving gif......")
    imageio.mimsave(gifName, frames, 'GIF', duration = duration)

if __name__ == '__main__':
    main()