import numpy as np
import skimage.io
from scipy.io import wavfile
from progress.bar import Bar

__SPAN = 0.00784313725490196  # (1-(-1))/255
__SAMPLE_RATE = 44100


def encodeImage(imageFile: str, outputFile: str) -> None:
    img = skimage.io.imread(imageFile)
    rows = img.shape[0]
    cols = img.shape[1]
    wave = np.zeros(((rows*cols*3),), dtype=np.float32)

    bar = Bar("Encoding", max=rows)
    index = 0
    for row in range(rows):
        for col in range(cols):
            (r, g, b) = img[row][col]
            wave[index] = -1.0 + r*__SPAN
            wave[index+1] = -1.0 + g*__SPAN
            wave[index+2] = -1.0 + b*__SPAN
            index += 3
        bar.next()
    bar.finish()

    wavfile.write(outputFile, __SAMPLE_RATE, wave)
