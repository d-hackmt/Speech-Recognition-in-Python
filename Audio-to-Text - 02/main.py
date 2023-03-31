import sys
# reading file

from api_communication import *

# 1. upload the file to assembly ai

# https://www.assemblyai.com/docs/walkthroughs#uploading-local-files-for-transcription
# for refernce code



filename = sys.argv[1]

#  sys.argv[1] gets the filename argument passed to the script,
# and then opens and reads the contents of the file.


audio_url = upload(filename)
save_transscript(audio_url , filename)