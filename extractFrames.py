import cv2
import os

source_path = '/media/chang/fe3dd8af-5577-42cb-95fb-4bd30a47cc9e/dataset/GRID/video'
destination_path = '/media/chang/fe3dd8af-5577-42cb-95fb-4bd30a47cc9e/dataset/GRID/frames'

speaker_num = 34
for files in os.listdir(source_path):
    print('processing:%s' % files)
    for filename in os.listdir(os.path.join(source_path, files)):
        if filename.endswith('.mpg'):
            frame_count = 0
            vc = cv2.VideoCapture(os.path.join(source_path, files, filename))
            print cv2.cv.CV_CAP_PROP_FPS
            if vc.isOpened():
                dest_dir = os.path.join(destination_path, files, str(filename.split('.', 1)[0]))
                while True:
                    rval, frame = vc.read()
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    jpg_filename = os.path.join(dest_dir, str(frame_count)+'.jpg')
                    if (rval is True) and (frame is not None):
                        cv2.imwrite(jpg_filename, frame)
                        print('saving:%d' % frame_count)
                        frame_count += 1
                    else:
                        break
                    cv2.waitKey(1)
            vc.release()


