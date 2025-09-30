import axios from "axios";

// Backend URL
const API_URL = "http://localhost:5000"; // Use localhost explicitly

export const predictBreed = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await axios.post(`${API_URL}/predict`, formData, {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        });
        return response.data;
    } catch (err) {
        console.error("Backend error:", err);
        throw err;
    }
};
