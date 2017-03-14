import os
import numpy as np

log_dir = '/home/chang/Code/lipreading/word_align.log'
align_path = '/media/chang/fe3dd8af-5577-42cb-95fb-4bd30a47cc9e' \
             '/dataset/GRID/align'
aligned_frame_path = '/media/chang/fe3dd8af-5577-42cb-95fb-4bd30a47cc9e/' \
            'dataset/GRID/alignedFrames'
bad_video_path = '/media/chang/fe3dd8af-5577-42cb-95fb-4bd30a47cc9e/' \
            'dataset/GRID/badVideo'
all_categories = ('command', 'color', 'preposition', 'letter', 'digit', 'averb')


# deal with a sentence in one video(alignment file)
def move_bad_video(video_name, label):
    for i in range(len(all_categories)):
        source_path = os.path.join(aligned_frame_path, all_categories[i],
                                   label[i], video_name)
        target_path = os.path.join(bad_video_path, all_categories[i],
                                   label[i])
        # if bad video exist,deal with it
        print source_path
        print target_path
        if os.path.exists(source_path):
            if not os.path.exists(target_path):
                os.makedirs(target_path)
            # deal with the videos with some problems
            assert not os.system(' '.join(['mv', source_path, target_path]))
    print 'moved all frames of bad videos.'

log_file = open(log_dir, mode='r')
log = log_file.read().splitlines()
log_file.close()
log = filter(lambda string: string.startswith('/'), log)
print len(log)

for bad_video in log:
    talker = bad_video.split('/')[-2]
    bad_video_name = bad_video.split('/')[-1]
    align_file = open(os.path.join(align_path, talker,
                                   'align', bad_video_name+'.align'))
    alignment = np.reshape(align_file.read().split(), (-1, 3))
    align_file.close()
    if alignment.shape[0] > 8:
                sp_ind = np.nonzero(alignment == 'sp')[0]
                alignment = np.delete(alignment, sp_ind, 0)
    move_bad_video(bad_video_name, alignment[1:7, 2])
