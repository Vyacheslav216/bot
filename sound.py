from os import path
import pydub
from pydub import AudioSegment
import os
#import database as dat


def convert(path,name,idf):
	# files                                                                         
	src = path
	name=name[0:-4]
	dst = name+".wav"
                                                          
	sound = AudioSegment.from_ogg(src)
	sound.set_frame_rate(16000).set_channels(1).export('./sound/'+dst, format="wav")
	os.remove(path)
	dat.savedata(idf,'./sound/'+dst)

