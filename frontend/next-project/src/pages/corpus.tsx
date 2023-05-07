/**
 * @file corpus main page
 * @author Siddique Muhammad
 * @version 1.1
 */

import NavBar from '../components/navbar'
import Link from 'next/link';
import { Card, CardContent, Typography } from '@mui/material';
import Footer from '@/components/footer';

const CorpusPage = () => (
  <>
  {/* Main Div */}
  <div className="min-h-screen flex flex-col bg-gray-100 ">

    {/* NavBar */}
    <div>
      <NavBar />
    {/* End NavBar */}
    </div>

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

    {/* Footer */}
    <div>
      <Footer></Footer>
    {/* End Footer */}
    </div> 

  {/* End Main Div */} 
  </div>
  </>
);

export default CorpusPage;
