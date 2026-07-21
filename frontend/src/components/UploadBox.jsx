import { useState } from "react";
import api from "../services/api";

function UploadBox({ setResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadSong = async () => {
    if (!file) {
      alert("Please select a song.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const res = await api.post("/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      console.log(res.data);

      setResult(res.data);
    } catch (err) {
      console.error(err);

      if (err.response) {
        alert(
          "Upload Failed\n\n" +
            JSON.stringify(err.response.data, null, 2)
        );
      } else {
        alert("Cannot connect to FastAPI server.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#0f172a",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        color: "white",
      }}
    >
      <div
        style={{
          width: "700px",
          padding: "40px",
          background: "#1e293b",
          borderRadius: "20px",
          textAlign: "center",
        }}
      >
        <h1>🎵 BeatSense AI</h1>

        <p>Upload any song and let AI analyze it.</p>

        <input
          type="file"
          accept=".mp3,.wav"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <br />
        <br />

        <button
          onClick={uploadSong}
          disabled={loading}
          style={{
            padding: "12px 30px",
            background: "#3b82f6",
            color: "white",
            border: "none",
            borderRadius: "10px",
            cursor: "pointer",
          }}
        >
          {loading ? "Analyzing..." : "Analyze Song"}
        </button>
      </div>
    </div>
  );
}

export default UploadBox;