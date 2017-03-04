import cv2
import os

source_path = '/media/chang/fe3dd8af-5577-42cb-95fb-4bd30a47cc9e/dataset/GRID/video'
destination_path = '/media/chang/fe3dd8af-5577-42cb-95fb-4bd30a47cc9e/dataset/GRID/frames'

speaker_num = 34
for files in os.listdir(source_path):
    video_count = 0
    print('processing:%s' % files)
    for filename in os.listdir(os.path.join(source_path, files)):
        print('video:%s' % video_count)
        if filename.endswith('.mpg'):
            video_count += 1
            frame_count = 0
            vc = cv2.VideoCapture(os.path.join(source_path, files, filename))
            print cv2.cv.CV_CAP_PROP_FPS
            if vc.isOpened():
                rval, frame = vc.read()
            else:
                rval = False
                print rval
            while rval:
                rval, frame = vc.read()
                dest_dir = os.path.join(destination_path, files, str(video_count))
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                jpg_filename = os.path.join(dest_dir, str(frame_count)+'.jpg')
                cv2.imwrite(jpg_filename, frame)
                print('saving:%d' % frame_count)
                frame_count += 1
                cv2.waitKey(1)
            vc.release()


