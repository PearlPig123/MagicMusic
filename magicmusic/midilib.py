from mido import *
from mido.messages import *
import mido

class MidiLib:

    # midi blob sample:
    #
    # c3 2.3 5.1
    # c4 4.0 7.0
    # <key startposition duration>
    # return a list of tuples
    # <"on/off", notekey, offset>
    @staticmethod
    def parse_midi_offset_from_blob(midi_blob):
        lines = midi_blob.strip().split("\n")

        # will sort everything
        note_messages = []

        for line in lines:
            splits = line.strip().split()
            note_key = splits[0]
            start = float(splits[1])    # absolute time
            duration = float(splits[2])
            end = start + duration  # absolute time

            note_messages.append(("on", note_key, start))
            note_messages.append(("off", note_key, end))

        sorted_note_messages = sorted(note_messages, key=lambda tuple: tuple[2])

        print(sorted_note_messages)

        offset_note_messages = []
        # print sorted message in an offset manner
        for i, message in enumerate(sorted_note_messages):
            if i == 0:
                offset_note_messages.append(message)
            else:
                offset = message[2] - sorted_note_messages[i-1][2]
                offset_note_messages.append((message[0], message[1], offset))

        return offset_note_messages

    # multipler will be used to magnify the time offset, e.g. 96
    @staticmethod
    def format_mido_onoffs_default_velocity(offset_note_messages, channel, multiplier):
        onoffs = ""
        for message in offset_note_messages:
            type = "note_" + message[0]
            note_key = message[1]
            offset = message[2]
            time = int(multiplier*offset)   # time must be int


            message = Message(type, channel=channel, time=time,
                              note=MidiLib.convert_note_key_to_num(note_key))

            line = str(message) + "\n"
            onoffs += line
        return onoffs


    # https://stackoverflow.com/questions/13926280/musical-note-string-c-4-f-3-etc-to-midi-note-value-in-python
    # Input is string in the form C#-4, Db-4, or F-3. If your implementation doesn't use the hyphen,
    # just replace the line :
    #    letter = midstr.split('-')[0].upper()
    # with:
    #    letter = midstr[:-1]
    @staticmethod
    def convert_note_key_to_num(midstr):
        Notes = [["C"], ["C#", "Db"], ["D"], ["D#", "Eb"], ["E"], ["F"],
                 ["F#", "Gb"], ["G"], ["G#", "Ab"], ["A"], ["A#", "Bb"], ["B"]]
        answer = 0
        i = 0
        # Note
        letter = midstr[:-1]
        for note in Notes:
            for form in note:
                if letter.upper() == form:
                    answer = i
                    break;
            i += 1
        # Octave
        answer += (int(midstr[-1])) * 12
        return answer