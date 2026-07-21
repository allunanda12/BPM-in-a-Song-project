import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt


def generate_waveform(audio_path, output_path):
    y, sr = librosa.load(audio_path, sr=None)

    plt.figure(figsize=(12, 4))
    librosa.display.waveshow(y, sr=sr)

    plt.title("Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def generate_spectrogram(audio_path, output_path):
    y, sr = librosa.load(audio_path, sr=None)

    D = librosa.amplitude_to_db(
        np.abs(librosa.stft(y)),
        ref=np.max
    )

    plt.figure(figsize=(12, 4))

    librosa.display.specshow(
        D,
        sr=sr,
        x_axis="time",
        y_axis="log"
    )

    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()