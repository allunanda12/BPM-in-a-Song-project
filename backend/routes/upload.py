from fastapi import APIRouter, UploadFile, File
import os
import shutil
import csv

from database import SessionLocal
from models.song import SongAnalysis

from ml.extract_features import extract_audio_features
from services.visualization import (
    generate_waveform,
    generate_spectrogram,
)

router = APIRouter()

UPLOAD_FOLDER = "uploads"
WAVEFORM_FOLDER = "static/waveforms"
SPECTROGRAM_FOLDER = "static/spectrograms"
CSV_FILE = "results.csv"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(WAVEFORM_FOLDER, exist_ok=True)
os.makedirs(SPECTROGRAM_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):

    # Save uploaded audio
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract audio features
    analysis = extract_audio_features(filepath)

    filename = os.path.splitext(file.filename)[0]

    # Image paths
    waveform_path = os.path.join(
        WAVEFORM_FOLDER,
        filename + ".png"
    )

    spectrogram_path = os.path.join(
        SPECTROGRAM_FOLDER,
        filename + ".png"
    )

    # Generate visualizations
    generate_waveform(filepath, waveform_path)
    generate_spectrogram(filepath, spectrogram_path)

    # =====================================
    # Save results to CSV (Optional Backup)
    # =====================================

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile)

        if not file_exists:
            writer.writerow([
                "Song",
                "Duration",
                "BPM",
                "Sample Rate",
                "RMS",
                "ZCR",
                "Spectral Centroid"
            ])

        writer.writerow([
            file.filename,
            analysis["duration"],
            analysis["tempo"],
            analysis["sample_rate"],
            analysis["rms"],
            analysis["zcr"],
            analysis["spectral_centroid"]
        ])

    # =====================================
    # Save results to PostgreSQL Database
    # =====================================

    db = SessionLocal()

    try:

        song = SongAnalysis(
            song=file.filename,
            duration=analysis["duration"],
            bpm=analysis["tempo"],
            sample_rate=analysis["sample_rate"],
            rms=analysis["rms"],
            zcr=analysis["zcr"],
            spectral_centroid=analysis["spectral_centroid"]
        )

        db.add(song)
        db.commit()
        db.refresh(song)

    except Exception as e:
        db.rollback()
        print("Database Error:", e)

    finally:
        db.close()

    # =====================================
    # Return Response
    # =====================================

    return {
        "status": "success",
        "filename": file.filename,
        "analysis": analysis,
        "waveform": f"/static/waveforms/{filename}.png",
        "spectrogram": f"/static/spectrograms/{filename}.png"
    }