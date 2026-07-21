import librosa
import numpy as np

def extract_audio_features(audio_path):
    # Load audio
    y, sr = librosa.load(audio_path, sr=None)

    # Basic information
    duration = librosa.get_duration(y=y, sr=sr)

    # Estimate BPM
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

    # MFCC
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

    # Chroma
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)

    # RMS
    rms = librosa.feature.rms(y=y)

    # Zero Crossing Rate
    zcr = librosa.feature.zero_crossing_rate(y)

    # Spectral Centroid
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)

    return {
        "duration": round(float(duration), 2),
        "sample_rate": sr,
        "tempo": round(float(tempo), 2),
        "mfcc_mean": np.mean(mfcc, axis=1).tolist(),
        "chroma_mean": np.mean(chroma, axis=1).tolist(),
        "rms": round(float(np.mean(rms)), 5),
        "zcr": round(float(np.mean(zcr)), 5),
        "spectral_centroid": round(float(np.mean(centroid)), 2)
    }               