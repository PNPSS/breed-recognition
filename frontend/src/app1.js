// import React, { useState } from "react";
// import { predictBreed } from "./api";
// import "./App.css";

// function App() {
//   const [file, setFile] = useState(null);
//   const [preview, setPreview] = useState(null);
//   const [result, setResult] = useState(null);
//   const [loading, setLoading] = useState(false);

//   // Most common breeds
//   const commonBreeds = [
//     { name: "Gir", img: "/breeds/gir.png" },
//     { name: "Sahiwal", img: "/breeds/sahiwal.png" },
//     { name: "ongole", img: "/breeds/murrah.png" },
//     { name: "Jaffarabadi", img: "/breeds/jafarabadi.png" },
//   ];

//   // Handle file/camera input
//   const handleFileChange = (e) => {
//     const selectedFile = e.target.files[0];
//     setFile(selectedFile);
//     setResult(null);

//     if (selectedFile) {
//       const reader = new FileReader();
//       reader.onloadend = () => setPreview(reader.result);
//       reader.readAsDataURL(selectedFile);
//     } else {
//       setPreview(null);
//     }
//   };

//   // Upload image to backend
//   const handleUpload = async () => {
//     if (!file) return alert("Please select or capture an image!");
//     setLoading(true);

//     try {
//       const data = await predictBreed(file);
//       setResult(data);
//     } catch (err) {
//       alert("Prediction failed. Check backend.");
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="container">
//       <h1 className="title">Cattle & Buffalo Breed Recognition</h1>

//       {/* Most Common Breeds */}
//       <div className="breed-container">
//         <h3>Most Common Breeds</h3>
//         <div className="breed-grid">
//           {commonBreeds.map((breed, index) => (
//             <div key={index} className="breed-card">
//               <img src={breed.img} alt={breed.name} className="breed-image" />
//               <p>{breed.name}</p>
//             </div>
//           ))}
//         </div>
//       </div>

//       {/* Upload / Capture */}
//       <div className="upload-box">
//         <input
//           type="file"
//           accept="image/*"
//           capture="environment"
//           onChange={handleFileChange}
//           className="file-input"
//         />
//         <button onClick={handleUpload} className="button">
//           Predict
//         </button>
//       </div>

//       {/* Preview */}
//       {preview && (
//         <div className="preview-container">
//           <p>Preview:</p>
//           <img src={preview} alt="preview" className="preview-image" />
//         </div>
//       )}

//       {/* Loading */}
//       {loading && <p className="processing">Processing...</p>}

//       {/* Prediction Result */}
//       {result && (
//         <div className="result-box">
//           <p><b>Breed:</b> {result.breed}</p>
//           <p><b>Confidence:</b> {(result.confidence * 100).toFixed(2)}%</p>
//         </div>
//       )}
//     </div>
//   );
// }

// export default App;


import React, { useState } from "react";
import { predictBreed } from "./api";

function App() {
    const [file, setFile] = useState(null);
    const [preview, setPreview] = useState(null);
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [lastPredictedFile, setLastPredictedFile] = useState(null);

    // Most common breeds
    const commonBreeds = [
        { name: "Gir", img: "/breeds/gir.png" },
        { name: "Sahiwal", img: "/breeds/sahiwal.png" },
        { name: "Murrah", img: "/breeds/murrah.png" },
        { name: "Jaffarabadi", img: "/breeds/jafarabadi.png" },
    ];

    // Handle file/camera input
    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0];
        setFile(selectedFile);
        setResult(null);

        if (selectedFile) {
            const reader = new FileReader();
            reader.onloadend = () => setPreview(reader.result);
            reader.readAsDataURL(selectedFile);
        } else {
            setPreview(null);
        }
    };

    // Upload image to backend and predict
    const handleUpload = async () => {
        if (!file) return alert("Please select or capture an image!");

        // Reuse previous prediction if same file
        if (lastPredictedFile === file && result) {
            console.log("Reusing previous prediction");
            return;
        }

        setLoading(true);

        try {
            const data = await predictBreed(file);
            setResult(data);
            setLastPredictedFile(file); // remember last predicted file
        } catch (err) {
            alert("Prediction failed. Check backend.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={styles.container}>
            <h1 style={styles.title}>Cattle & Buffalo Breed Recognition</h1>

            {/* Most Common Breeds */}
            <div style={styles.breedContainer}>
                <h3>Most Common Breeds</h3>
                <div style={styles.breedGrid}>
                    {commonBreeds.map((breed, index) => (
                        <div key={index} style={styles.breedCard}>
                            <img
                                src={breed.img}
                                alt={breed.name}
                                style={styles.breedImage}
                            />
                            <p>{breed.name}</p>
                        </div>
                    ))}
                </div>
            </div>

            {/* Upload / Capture */}
            <div style={styles.uploadBox}>
                <input
                    type="file"
                    accept="image/*"
                    capture="environment"
                    onChange={handleFileChange}
                    style={styles.fileInput}
                />
                <button onClick={handleUpload} style={styles.button}>
                    Predict
                </button>
            </div>

            {/* Preview */}
            {preview && (
                <div style={styles.previewContainer}>
                    <p>Preview:</p>
                    <img
                        src={preview}
                        alt="preview"
                        style={styles.previewImage}
                    />
                </div>
            )}

            {/* Loading */}
            {loading && <p style={styles.processing}>Processing...</p>}

            {/* Prediction Result */}
            {result && (
                <div style={styles.resultBox}>
                    <p>
                        <b>Breed:</b> {result.breed}
                    </p>
                    <p>
                        <b>Confidence:</b>{" "}
                        {(result.confidence * 100).toFixed(2)}%
                    </p>
                </div>
            )}
        </div>
    );
}

// Styles
const styles = {
    container: {
        fontFamily: "Arial, sans-serif",
        textAlign: "center",
        padding: "20px",
        maxWidth: "800px",
        margin: "auto",
    },
    title: { color: "#007bff", fontSize: "2rem", marginBottom: "20px" },
    breedContainer: { marginBottom: "30px" },
    breedGrid: {
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "center",
        gap: "15px",
    },
    breedCard: { width: "120px", textAlign: "center" },
    breedImage: {
        width: "100%",
        height: "80px",
        objectFit: "cover",
        borderRadius: "8px",
        border: "1px solid #ccc",
    },
    uploadBox: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: "10px",
        marginBottom: "20px",
    },
    fileInput: { fontSize: "16px", padding: "5px" },
    button: {
        padding: "10px 20px",
        fontSize: "16px",
        backgroundColor: "#007bff",
        color: "#fff",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer",
    },
    previewContainer: { marginBottom: "20px" },
    previewImage: {
        width: "100%",
        maxWidth: "300px",
        height: "auto",
        borderRadius: "10px",
        marginTop: "10px",
    },
    processing: { color: "#ff9800", fontWeight: "bold" },
    resultBox: {
        marginTop: "20px",
        padding: "15px",
        border: "2px solid #007bff",
        borderRadius: "10px",
        backgroundColor: "#f1f8ff",
    },
};

export default App;
