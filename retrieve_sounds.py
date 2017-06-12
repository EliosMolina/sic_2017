import freesound, sys,os
import random

client = freesound.FreesoundClient()
client.set_token(os.environ['TOKEN_FREESOUND'],"token")

sounds = client.text_search(filter="tag:animal duration:[0 TO 15]",
                            page_size=150,
                            fields="id,name,previews,tags,duration")
count = 0

# Get all sounds for later shuffling
snds = []
while sounds != None and count < 300:
	print count
	for snd in sounds:
		snds.append(snd)
		count += 1
	try:
		sounds = sounds.next_page()
	except:
		sounds = None

# Retrieve previews of N random sounds
N = 20
random.shuffle(snds)
for snd in snds[0:N]:
	print snd.name, snd.id, snd.tags, snd.duration
	snd.retrieve_preview('.', snd.name + '.mp3')
