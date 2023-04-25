import React, { useState } from 'react';
import axios from 'axios';
import NavBar from '@/components/navbar';

const CorpusForm = () => {
  const [formData, setFormData] = useState({
    corpus_id: '',
    corpus_name: '',
    labels: '',
    description: '',
    version: '',
    n_docs: ''
  });

  const [formMessage, setFormMessage] = useState('');

  const handleChange = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value
    });
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    try {
      const response = await axios.post('http://localhost:5000/corpus', formData);
      console.log(response.data);

      setFormMessage(response.data.result);
      // reset the form after successful submit
      setFormData({
        corpus_id: '',
        corpus_name: '',
        labels: '',
        description: '',
        version: '',
        n_docs: ''
      });
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
    <NavBar></NavBar>
    <form onSubmit={handleSubmit} className="max-w-lg mx-auto p-6 bg-white shadow-md rounded-md">
    <h1 className='text-4xl font-bold m-2'>Insert Corpus</h1>

      <div className="mb-4">
        <label className="block text-gray-700 font-bold mb-2" htmlFor="corpus_id">
          Corpus ID:
        </label>
        <input
          className="appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline  bg-gray-200"
          id="corpus_id"
          type="text"
          name="corpus_id"
          value={formData.corpus_id}
          onChange={handleChange}
          disabled
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 font-bold mb-2" htmlFor="corpus_name">
          Corpus name:
        </label>
        <input
          className="appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="corpus_name"
          type="text"
          name="corpus_name"
          value={formData.corpus_name}
          onChange={handleChange}
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 font-bold mb-2" htmlFor="labels">
          Labels:
        </label>
        <input
          className="appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="labels"
          type="text"
          name="labels"
          value={formData.labels}
          onChange={handleChange}
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 font-bold mb-2" htmlFor="description">
          Description:
        </label>
        <textarea
          className="appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="description"
          name="description"
          value={formData.description}
          onChange={handleChange}
        ></textarea>
      </div>
      <div>
      <label className="block text-gray-700 font-bold mb-2" htmlFor="version">
          Version:
        </label>
        <input
          className="appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="version"
          type="text"
          name="version"
          value={formData.version}
          onChange={handleChange}
        />
      </div>
      <div className="flex justify-center">
        <button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          type="submit"
        >
          Submit
        </button>
      </div>

      {formMessage && <p className="text-center text-green-500 m-2">{formMessage}</p>}

    </form>
    </>
  );
};

export default CorpusForm;
