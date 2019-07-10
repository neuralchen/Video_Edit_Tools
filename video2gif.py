import os
import cv2
from tqdm import tqdm
import argparse
import imageio
import PIL
from PIL import Image

parser = argparse.ArgumentParser(description='translation images to video')

parser.add_argument('--videoPath', type=str, default="F:\\FFOutput\\1.avi", help='path to your video')#, required=True)
parser.add_argument('--duration', type=float, default=0.001, help='gif duration')
parser.add_argument('--outputPath', type=str, default="F:\\FFOutput\\vangogh.gif", help='path to the output gif file')
parser.add_argument('--sampleScale', type=float, default=0.6, help='sampling sale of your images')
parser.add_argument('--sampleInterval', type=int, default=4, help='sampling interval of images')
args = parser.parse_args()


def main():
    path        = args.videoPath
    gifName     = args.outputPath
    duration    = args.duration
    sample_scale= args.sampleScale
    sampleInter = args.sampleInterval
    # cutStart
    cap         = cv2.VideoCapture(path)
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
        return
    frames = []
    i = 0
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            if i == 0:
                size  = frame.shape[0:2]
                size  = (int(size[1]*sample_scale),int(size[0]*sample_scale))
            if i%sampleInter == 0:
                print("append %d-th frame"%i)
                frameTemp = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                if sample_scale != 1.0:
                    frameTemp = cv2.resize(frameTemp, size, interpolation = cv2.INTER_CUBIC)
                frames.append(frameTemp)
        else: 
            break
        i += 1
    cap.release()
    print("saving gif......")
    imageio.mimsave(gifName, frames, 'GIF', duration = duration)

if __name__ == '__main__':
    main()