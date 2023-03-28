from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import repositories.note_repository as note_repository
import ffmpeg

A4_FREQUENCY = 440
A4_MIDI_NUM = 69

def beats_to_ms(duration, tempo):
    return (60000/tempo) * duration

def generate_track_mp3(track):
    notes = note_repository.notes_in_track(track)
    result = AudioSegment.silent(duration=0)

    for note in notes:
        position = beats_to_ms(note.location, track.tempo)
        end_position = position + \
            beats_to_ms(note.duration, track.tempo)
        note_to_add = generate_note(note, track.tempo)

        if end_position > len(result):
            new_result = AudioSegment.silent(duration=end_position)
            result = new_result.overlay(result)

        result = result.overlay(note_to_add, position)

    result.export(f"out/{track.title}.mp3", "mp3",)

def generate_note(note, tempo):
    result = AudioSegment.silent(duration=0)
    
    gen = Sine(midi_num_to_freq(note.pitch))

    sine = gen.to_audio_segment(
        duration = beats_to_ms(note.duration, tempo) )
    sine = sine.fade_in(20).fade_out(20)

    result += sine
    return result

def midi_num_to_freq(midi_num):
    return 2**((midi_num-A4_MIDI_NUM)/12) * A4_FREQUENCY