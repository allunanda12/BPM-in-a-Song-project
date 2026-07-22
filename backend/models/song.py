from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SongAnalysis(Base):
    __tablename__ = "song_analysis"

    id = Column(Integer, primary_key=True, index=True)
    song = Column(String, nullable=False)
    duration = Column(Float)
    bpm = Column(Float)
    sample_rate = Column(Integer)
    rms = Column(Float)
    zcr = Column(Float)
    spectral_centroid = Column(Float)