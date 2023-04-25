import React, { useState } from 'react';
import axios from 'axios';
import NavBar from '@/components/navbar';

const FileUploadForm: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);

  const handleFileInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files.length > 0) {
      setFile(event.target.files[0]);
    }
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    if (!file) {
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
    <NavBar></NavBar>
    <div className='w-80 m-8 mx-auto'>
    <h1 className="text-4xl font-bold mb-6 text-center">Upload zip file</h1>

    <form onSubmit={handleSubmit} className="flex flex-col items-center space-y-4">
      <label className="w-full flex flex-col items-center justify-center border-4 border-dashed border-gray-400 py-4 rounded-md">
        <svg
          className="w-6 h-6 text-gray-400"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M15 19l-7-7 7-7"
          />
        </svg>
        <span className="mt-2 text-base leading-normal">
          Select a file or drag and drop it here
        </span>
        <input
          type="file"
          className="hidden"
          onChange={handleFileInputChange}
        />
      </label>

      <button
        type="submit"
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
        Submit
      </button>
    </form>

        
    </div>
    </>
  );
};

export default FileUploadForm;
