import os
import sys
import tarfile
import zipfile
import urllib


data_dir = '/media/chang/fe3dd8af-5577-42cb-95fb-4bd30a47cc9e/dataset/GRID'
num_talkers = 34
data_url_ = 'http://spandh.dcs.shef.ac.uk/gridcorpus/'


def maybe_download_and_extract():
    """Download and extract data."""
    raw_dir = os.path.join(data_dir, 'raw')
    video_dir = os.path.join(raw_dir, 'video')
    align_dir = os.path.join(raw_dir, 'align')
    # http://spandh.dcs.shef.ac.uk/gridcorpus/s1/video/s1.mpg_vcd.zip
    # http://spandh.dcs.shef.ac.uk/gridcorpus/s1/align/s1.tar

    def _progress(count, block_size, total_size):
        sys.stdout.write('\r>> Downloading %.1f%%' % (
            float(count * block_size) / float(total_size) * 100.0))
        sys.stdout.flush()

    def download_data(suffix='.mpg_vcd.zip', dir_path='video'):
        for instance in range(1, num_talkers+1):
            if not instance == 21:
                tar_type = suffix.split('.')[-1]
                filename = os.path.join(raw_dir, dir_path, str(instance)+'.'+tar_type)
                data_url = data_url_ + 's' + str(instance) + '/' + dir_path + '/s' + str(instance) + suffix
                # filename = data_url.split('/')[-1].split('.')[0][1]
                dest_directory = os.path.join(data_dir, dir_path)
                if not os.path.exists(os.path.join(dest_directory, 's'+str(instance))):
                    if os.path.exists(filename):
                        os.remove(filename)
                    urllib.urlretrieve(data_url, filename, _progress)
                    if dir_path == 'video':
                        zipfile.ZipFile(filename, 'r').extractall(dest_directory)
                    else:
                        dest_directory = os.path.join(data_dir, dir_path, 's'+str(instance))
                        tarfile.open(filename, 'r:tar').extractall(dest_directory)
                print instance
    if not os.path.exists(align_dir):
        os.makedirs(align_dir)
    if not os.path.exists(video_dir):
        os.makedirs(video_dir)
    download_data(suffix='.tar', dir_path='align')
    download_data()
    statinfo = os.stat(raw_dir)
    print('Successfully downloaded', statinfo.st_size, 'bytes.')


def main():
    maybe_download_and_extract()


if __name__ == '__main__':
    main()
