# This is a sample Python script.
import os
import time

import numpy
import pygame



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# TODO: integrate with headphone touch gestures
# TODO: stop playing when headphone disconnects
def playMusic():
    music_dir = "C:\\Users\\aweso\\my music"
    songs = os.listdir(music_dir)
    numpy.random.shuffle(songs)
    list_connected_devices()
    playlist(songs, music_dir)
def list_connected_devices():
    mngd_objs = mngr.GetManagedObjects()
    for path in mngd_objs:
        con_state = mngd_objs[path].get('org.bluez.Device1', {}).get('Connected', False)
        if con_state:
            addr = mngd_objs[path].get('org.bluez.Device1', {}).get('Address')
            name = mngd_objs[path].get('org.bluez.Device1', {}).get('Name')
            print(f'Device {name} [{addr}] is connected')


def playlist(songs, music_dir):
    print(songs)
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    pygame.mixer.init()
    songno = 0
    pygame.mixer.set_num_channels(8)
    voice = pygame.mixer.Channel(5)
    for song in songs:
        sound = pygame.mixer.Sound(os.path.join(music_dir, song))
        playingsong = os.path.join(music_dir, song)
        # sound.set_volume(0.1)
        voice.play(sound)
        while voice.get_busy():
            time.sleep(1)
        songno = songno + 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    playMusic()
    while True:
        time.sleep(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
