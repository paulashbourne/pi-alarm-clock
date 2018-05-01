from multiprocessing import Process


def play_audio(filepath):
    import pygame
    #pygame.init()
    #pygame.mixer.init()
    #pygame.mixer.music.load(filepath)
    #pygame.mixer.music.play()
    #while pygame.mixer.music.get_busy(): 
    #    pygame.time.Clock().tick(10)
    while True: 
        print "Alarm!!!"
        pygame.time.Clock().tick(1)

def _generate_player(filename):
    return lambda: play_audio(filename)


class AsyncAudioPlayer(object):

    def __init__(self, filepath):
        self.filepath = filepath
        # Internal variables
        self._subprocess = None

    def play(self):
        if self._subprocess is not None:
            raise RuntimeError("Audio process already running")
        self._subprocess = Process(target=_generate_player(self.filepath))
        self._subprocess.start()

    def stop(self):
        if self._subprocess is None:
            raise RuntimeError("Audio is not playing")
        self._subprocess.terminate()
        self._subprocess = None
