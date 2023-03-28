from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine

A4_FREQUENCY = 440
A4_MIDI_NUM = 69


def generate_track_mp3(track):
    pass

def generate_note(note, tempo):
    result = AudioSegment.silent(duration=0)
    gen = Sine(midi_num_to_freq(note.pitch))

    sine = gen.to_audio_segment(duration=(60000/tempo)*note.duration)
    sine = sine.fade_in(50).fade_out(50)
    result += sine
    
    return result

def midi_num_to_freq(midi_num):
    return 2**((midi_num-A4_MIDI_NUM)/12) * A4_FREQUENCY

################
# TESTING ZONE #
################

class Note:
    def __init__(self, pitch, duration):
        self.pitch = pitch
        self.duration = duration

test_note = Note(69, 4)
play(generate_note(test_note, 120))