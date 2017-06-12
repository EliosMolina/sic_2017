# Experiments with Freesound and Gaia

## Retrieve Freesound subset
see: https://github.com/MTG/freesound-python
Set environment variable with token:
`export TOKEN_FREESOUND=""`

Then run python script.
`python retrieve_sounds.py` 

## Extract descriptors using essentia
see: http://essentia.upf.edu/documentation/installing.html

I'm using `/home/emolina/git/essentia/build/src/examples/essentia_streaming_extractor_freesound` (see Essentia instructions to compile examples)

Then I extract sigs for all mp3 files:
`for f in *.mp3; do ../essentia/build/src/examples/essentia_streaming_extractor_freesound "$f" "$f.sig" profile.txt; done`

## Create Gaia dataset for query by example (nn search)
note: At the moment I just tried search by id
`python create_nn.py`


