from .audio import AsyncAudioPlayer

class AlarmClock(object):

    def __init__(self, audio_filepath):
        self._audio_player = AsyncAudioPlayer(audio_filepath)

    def sound(self):
        print("Sounding the alarm")
        self._audio_player.play()

    def snooze(self):
        print("Snooze")
        self._audio_player.stop()

    def stop(self):
        print("stop")
        self._audio_player.stop()
