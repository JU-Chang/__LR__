import os
import numpy
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(message)s',
                    filename='word_align.log',
                    filemode='w')

frame_path = '/media/chang/fe3dd8af-5577-42cb-95fb-4bd30a47cc9e/' \
            'dataset/GRID/frames'
aligned_frame_path = '/media/chang/fe3dd8af-5577-42cb-95fb-4bd30a47cc9e/' \
            'dataset/GRID/alignedFrames'
alignment_path = '/media/chang/fe3dd8af-5577-42cb-95fb-4bd30a47cc9e/' \
                 'dataset/GRID/align'
label_command = {'bin': 1, 'lay': 2, 'place': 3, 'set': 4}
label_color = {'red': 1, 'white': 2, 'blue': 3, 'green': 4}
label_preposition = {}
label_letter = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
                'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15,
                'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22,
                'x':23, 'y':24, 'z':25}
label_digit = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
               '9':9, '0':10}
label_adverb = {}
label_list = {}
all_categories = ('command', 'color', 'preposition', 'letter', 'digit', 'averb')


# copy frames related to one word
def save_frame(start_frame, end_frame, video_path, category, label):
    save_path = os.path.join(aligned_frame_path, category,
                             label, video_path.split('/')[-1])
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for i in range(start_frame, end_frame+1):
        source = os.path.join(video_path, str(i)+'.jpg')
        target = os.path.join(save_path, str(i)+'.jpg')
        assert os.path.exists(source)
        assert not os.system(' '.join(['cp', source, target]))


# deal with a sentence in one video(alignment file)
def save_sentence(start_fr, end_fr, video_path, label):
    for i in range(len(all_categories)):
        save_frame(start_fr[i], end_fr[i], video_path,
                   all_categories[i], label[i])

# assert not os.path.exists(aligned_frame_path), \
#     'alignedFrames exist!'
# os.mkdir(aligned_frame_path)

print 'start...'
for element in all_categories:
    if not os.path.exists(os.path.join(aligned_frame_path, element)):
        os.mkdir(os.path.join(aligned_frame_path, element))

for talker in os.listdir(alignment_path):
    logging.info('=======')
    logging.info(talker)
    print talker
    for align_name in os.listdir(os.path.join(alignment_path, talker, 'align')):
        video_name = align_name.split('.')[0]
        video_file = os.path.join(frame_path, talker, video_name)
        align_file = open(os.path.join(alignment_path,
                                       talker, 'align', align_name))
        # print os.path.join(alignment_path, talker, 'align', align_name)
        try:

            oneline = align_file.read()
            alignment = numpy.reshape(oneline.split(), (-1, 3))
            if alignment.shape[0]>8:
                alignment = numpy.delete(alignment, 4, 0)
            start_f = alignment[1:7, 0].astype(int)/1000
            end_f = alignment[1:7, 1].astype(int)/1000
            # logging.info(alignment[1:7, 2])
            save_sentence(start_f, end_f,
                          video_file, alignment[1:7, 2])
        except AssertionError:
            logging.info('==============')
            logging.info(video_file)
            logging.info(align_file)
            pass

        finally:
            align_file.close()
            print 'successfully.see log in \'word_align.log\''




