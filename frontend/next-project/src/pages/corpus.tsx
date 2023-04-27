import NavBar from '../components/navbar'
import Link from 'next/link';
import { Card, CardContent, Typography } from '@mui/material';
import Footer from '@/components/footer';

const CorpusPage = () => (
  <div>
    <NavBar />
    <div className="flex items-center justify-center m-8">
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-6">Corpus Page</h1>
        
        <div className='w-96'>
          <p className="text-lg text-gray-700 mb-4">The corpus page is a section of the application that focuses on managing text corpora. A corpus is a collection of texts, documents, or conversations used for linguistic or other types of analysis. In the context of the application, corpora are collections of texts related to a specific topic, such as biomedicine or linguistics.</p>
          <p className="text-lg text-gray-700 mb-4">The corpus page allows users to create, edit, and delete text corpora. They can also add individual documents to the corpus or import sets of documents in zip format. Additionally, users can view and filter the list of available corpora based on various criteria, such as name, language, or number of documents.</p>
          <p className="text-lg text-gray-700 mb-4">With the corpus page, researchers and analysts can easily organize and curate large-scale text data and use it for various purposes, such as language modeling, information retrieval, or natural language processing.</p>
        </div> 
        <div>
          <button className="m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition-all duration-500 transform hover:scale-110">
            <Link href='/corpus/insert'>Insert a corpus Now</Link>
          </button>
          <button className="m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition-all duration-500 transform hover:scale-110">
            <Link href='/corpus/list'>List corpus</Link>
          </button>
        </div>

      </div>
    </div>
    <Footer></Footer>
  </div>
)

export default CorpusPage