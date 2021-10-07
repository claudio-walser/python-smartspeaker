#!/usr/bin/env python3

import speech_recognition as sr

from os import path
audio_file = "./english.wav"

recognizer = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
