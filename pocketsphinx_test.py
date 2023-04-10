model = '/Users/chasehult/PycharmProjects/ista131/venv/lib/python3.9/site-packages/pocketsphinx/model/en-us/'

from os import path

from pocketsphinx import *

MODELDIR = "../../../model"
DATADIR = "../../../test/data"

# Create a decoder with certain model

# Decode streaming data.
decoder = Decoder(hmm=path.join(model, 'en-us'),
                  allphone=path.join(model, 'en-us-phone.lm.bin'),
                  lw=2.0,
                  beam=1e-10,
                  pbeam=1e-10)

decoder.start_utt()
stream = open('quick_beige_fox.wav', 'rb')
while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
    else:
        break
decoder.end_utt()

hypothesis = decoder.hyp()
print('Phonemes: ', ' '.join(seg.word for seg in decoder.seg()))
