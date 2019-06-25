import os
import cv2
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(description='translation images to video')

parser.add_argument('--imagePath', type=str,default=None, help='path to your images',required=True)
parser.add_argument('--videoFPS', type=int,default=10, help='the FPS of output video')
parser.add_argument('--outputPath', type=str,default="./result.avi", help='path to the output file')
parser.add_argument('--sampleScale', type=float,default=1.0, help='sampling sale of your images')

args = parser.parse_args()

def main():
    path        = args.imagePath
    videoname   = args.outputPath
    fps         = args.videoFPS
    sample_scale= args.sampleScale
    filelist    = os.listdir(path)
    test_image  = os.path.join(path, filelist[0])
    img         = cv2.imread(test_image, cv2.IMREAD_UNCHANGED)
    size        = img.shape[0:2]
    size        = (int(size[1]*sample_scale),int(size[0]*sample_scale))
    print("video size:"+str(size))
    video   = cv2.VideoWriter(videoname, cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
    filelist.sort(key=lambda x: os.path.getctime(os.path.join(path, x)))
    for img_idx,item in enumerate(tqdm(filelist)):
        if item.endswith('.png'): 
            item    = os.path.join(path, item)
            img     = cv2.imread(item)
            if sample_scale != 1.0:
                img = cv2.resize(img, size, interpolation = cv2.INTER_CUBIC)
            video.write(img)
    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()