/**
 * @file analyze main page
 * @author Siddique Muhammad
 * @version 1.2
 */

/**
 * @imports
 * @Link from next/link
 * @Layout layout component
 */
import Link from 'next/link';
import Layout from '@/components/Layout';

// Not used yet
import { Card, CardContent, Typography } from '@mui/material';
import { useEffect, useState } from 'react';


/**
 * @const AnalyzePage
 * @description Manages the analization section. 
 *              Lists corpus and selecting one, redirects to dashboard.
 * @returns html page
 */
const AnalyzePage = () => {
  const [corpusData, setCorpusData] = useState([]);

  useEffect(() => {
    const fetchCorpusData = async () => {
      try {
        const response = await fetch('http://localhost:5000/corpus');
        const data = await response.json();
        setCorpusData(data);
      } catch (error) {
        console.error('Error fetching corpus data:', error);
      }
    };
    fetchCorpusData();

  }, []);

  return (
    <Layout>
      {/* Main Div */}
      <div className="flex flex-col bg-gray-100 ">

        {/* Content */}
        <div className="flex-grow ">

          <div className="flex flex-col items-center justify-center my-8">
            <div className="text-center w-10/12">
              <h1 className="text-4xl font-bold mb-6">Corpus Page</h1>

              {/* Text */}
              <div className='bg-white rounded-lg shadow-lg p-8 text-justify'>
                <p className="text-lg text-gray-700 mb-4">The corpus page is a section of the application that focuses on managing text corpora. A corpus is a collection of texts, documents, or conversations used for linguistic or other types of analysis. In the context of the application, corpora are collections of texts related to a specific topic, such as biomedicine or linguistics.</p>
                <p className="text-lg text-gray-700 mb-4">The corpus page allows users to create, edit, and delete text corpora. They can also add individual documents to the corpus or import sets of documents in zip format. Additionally, users can view and filter the list of available corpora based on various criteria, such as name, language, or number of documents.</p>
                <p className="text-lg text-gray-700 mb-4">With the corpus page, researchers and analysts can easily organize and curate large-scale text data and use it for various purposes, such as language modeling, information retrieval, or natural language processing.</p>

              {/* End Text */}
              </div>
              
              {/* Buttons */}
              <div className="flex justify-center space-x-4 mt-8">

                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition-all duration-500 transform hover:scale-110">
                  <Link href='/corpus/insert'>
                    Insert a Corpus
                  </Link>
                </button>
                
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition-all duration-500 transform hover:scale-110">
                  <Link href='/corpus/list'>
                    List Corpus
                  </Link>
                </button>

              {/* End Buttons */}
              </div>

            </div>

          </div>

        {/* End Content */}
        </div>


      {/* End Main Div */} 
      </div>
    </Layout>
  );
}

export default AnalyzePage;
