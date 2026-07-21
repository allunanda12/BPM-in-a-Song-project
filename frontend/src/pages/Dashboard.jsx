function Dashboard({ data, goBack }) {
  return (
    <div
      style={{
        background: "#0f172a",
        color: "white",
        minHeight: "100vh",
        padding: "40px",
        fontFamily: "Arial",
      }}
    >
      {/* Top Bar */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: "20px",
        }}
      >
        <h1>🎵 BeatSense AI Dashboard</h1>

        <button
          onClick={goBack}
          style={{
            padding: "12px 20px",
            background: "#3b82f6",
            color: "white",
            border: "none",
            borderRadius: "10px",
            cursor: "pointer",
            fontSize: "16px",
          }}
        >
          ⬅ Analyze Another Song
        </button>
      </div>

      <hr />

      <div
        style={{
          background: "#1e293b",
          padding: "25px",
          borderRadius: "15px",
          marginTop: "25px",
          marginBottom: "30px",
        }}
      >
        <h2>🎼 Audio Analysis</h2>

        <p><b>Duration:</b> {data.analysis.duration} sec</p>
        <p><b>BPM:</b> {data.analysis.tempo}</p>
        <p><b>Sample Rate:</b> {data.analysis.sample_rate}</p>
        <p><b>RMS:</b> {data.analysis.rms}</p>
        <p><b>ZCR:</b> {data.analysis.zcr}</p>
        <p><b>Spectral Centroid:</b> {data.analysis.spectral_centroid}</p>
      </div>

      <div
        style={{
          background: "#1e293b",
          padding: "25px",
          borderRadius: "15px",
          marginBottom: "30px",
          textAlign: "center",
        }}
      >
        <h2>📈 Waveform</h2>

        <img
          src={`http://127.0.0.1:8000${data.waveform}`}
          alt="Waveform"
          width="900"
          style={{ borderRadius: "10px", maxWidth: "100%" }}
        />
      </div>

      <div
        style={{
          background: "#1e293b",
          padding: "25px",
          borderRadius: "15px",
          textAlign: "center",
        }}
      >
        <h2>🎵 Spectrogram</h2>

        <img
          src={`http://127.0.0.1:8000${data.spectrogram}`}
          alt="Spectrogram"
          width="900"
          style={{ borderRadius: "10px", maxWidth: "100%" }}
        />
      </div>
    </div>
  );
}

export default Dashboard;