import { useState } from "react";
import UploadBox from "../components/UploadBox";
import Dashboard from "./Dashboard";

function Home() {
  const [result, setResult] = useState(null);

  return (
    <>
      {result ? (
        <Dashboard
          data={result}
          goBack={() => setResult(null)}
        />
      ) : (
        <UploadBox setResult={setResult} />
      )}
    </>
  );
}

export default Home;