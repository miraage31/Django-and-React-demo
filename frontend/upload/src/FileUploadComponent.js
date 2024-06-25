// FileUploadComponent.js
import React, { useState } from 'react';
import axios from 'axios';

const FileUploadComponent = () => {
    const [file, setFile] = useState(null);

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };
//  This is an important file please study this so yeah
    const handleFileUpload = async () => {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:8000/api/upload-csv/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            console.log(response.data);
            alert('CSV Uploaded Successfully');
        } catch (error) {
            console.error('Error uploading file: ', error);
            alert('Error uploading CSV');
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleFileUpload}>Upload CSV</button>
        </div>
    );
};

export default FileUploadComponent;
