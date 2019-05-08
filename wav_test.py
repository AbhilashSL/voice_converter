from pydub import AudioSegment
sound = AudioSegment.from_mp3("arctic_a0004.mp3")
sound.export("D:\mp3.wav", format="wav")