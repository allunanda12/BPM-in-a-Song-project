function Navbar() {
  return (
    <nav
      style={{
        height: "80px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "0 60px",
        background: "rgba(20,25,40,0.8)",
        backdropFilter: "blur(10px)",
        borderBottom: "1px solid rgba(255,255,255,0.1)"
      }}
    >
      <h2
        style={{
          color: "#61dafb",
          fontWeight: "700"
        }}
      >
        🎵 BeatSense AI
      </h2>

      <div
        style={{
          display: "flex",
          gap: "30px",
          color: "white"
        }}
      >
        <span>Home</span>
        <span>Dashboard</span>
        <span>About</span>
      </div>
    </nav>
  );
}

export default Navbar;