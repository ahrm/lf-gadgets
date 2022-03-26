import sys
import ffmpeg

def get_probe_duration(probe):
    for i in range(len(probe['streams'])):
        if 'duration' in probe['streams'][i]:
            return probe['streams'][i]['duration']

def get_probe_width(probe):
    for i in range(len(probe['streams'])):
        if 'width' in probe['streams'][i]:
            return probe['streams'][i]['width']

probe = ffmpeg.probe(sys.argv[1])
time = float(get_probe_duration(probe)) // 2

width = get_probe_width(probe)

moment = time // 2
ffmpeg.input(sys.argv[1], ss=moment).filter('scale', width, -1).output(sys.argv[2], vframes=1).run(overwrite_output=True)

