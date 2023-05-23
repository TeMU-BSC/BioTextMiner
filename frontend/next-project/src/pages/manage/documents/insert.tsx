/**
 * @file insert.tsx
 * @description insert documents
 * @author Siddique Muhammad
 */


/**
 * @imports
 */
import React, { useState } from 'react';
import axios from 'axios';
import Layout from '@/components/Layout';


/**
 * @const DocumentForm
 * @returns html form
 */
const DocumentForm = () => {
  const [formData, setFormData] = useState({
    name : '',
    author: '',
    source: '',
    date : '',
    collection: '',
    language: '',
    text: '',
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
      const response = await axios.post('http://localhost:5000/documents', formData);

      console.log(response.data);

      setFormMessage(response.data.result);
      // reset the form after successful submit
      setFormData({
        name : '',
        author: '',
        source: '',
        date : '',
        collection: '',
        language: '',
        text: '',
      });
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Layout>

    <div className='m-8'>
      <form onSubmit={handleSubmit} className="max-w-lg mx-auto p-6 bg-white shadow-md rounded-md">
      <h1 className='text-4xl font-bold m-2'>Insert Document</h1>

        <div className="mb-4">
          <label className="block text-gray-700 font-bold mb-2" htmlFor="name">
            Document Name:
          </label>
          <input
            className="appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="name"
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 font-bold mb-2" htmlFor="author">
            Author:
          </label>
          <input
            className="appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="author"
            type="text"
            name="author"
            value={formData.author}
            onChange={handleChange}
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 font-bold mb-2" htmlFor="source">
            Source:
          </label>
          <input
            className="appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="source"
            type="text"
            name="source"
            value={formData.source}
            onChange={handleChange}
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 font-bold mb-2" htmlFor="collection">
            Collection:
          </label>
          <textarea
            className="appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="collection"
            name="collection"
            value={formData.collection}
            onChange={handleChange}
          ></textarea>
        </div>
        <div className="mb-4">
        <label className="block text-gray-700 font-bold mb-2" htmlFor="language">
          Language:
          </label>
          <input
            className="appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="language"
            type="text"
            name="language"
            value={formData.language}
            onChange={handleChange}
          />
        </div>
        <div className="mb-4">
        <label className="block text-gray-700 font-bold mb-2" htmlFor="date">
          Date:
          </label>
          <input
            className="appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="date"
            type="date"
            name="date"
            value={formData.date}
            onChange={handleChange}
          />
        </div>
        <div>
        <label className="block text-gray-700 font-bold mb-2" htmlFor="text">
          Text:
          </label>
          <textarea
            className="appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="text"
            name="text"
            value={formData.text}
            onChange={handleChange}
          ></textarea>
        </div>
        <div className="flex justify-center m-7">
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >
            Submit
          </button>
        </div>

        {formMessage && <p className="text-center text-green-500 m-2">{formMessage}</p>}

      </form>
    </div>

    </Layout>
  );
};

export default DocumentForm;
