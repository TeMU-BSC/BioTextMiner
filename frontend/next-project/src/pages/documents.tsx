/**
 * @file documents main page
 * @author Siddique Muhammad
 * @version 1.1
 */

import NavBar from '../components/Navbar'
import Link from 'next/link';
import Footer from '@/components/footer';

const DocumentsPage = () => (
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
        <h1 className="text-4xl font-bold mb-6">Documents Page</h1>
        
        {/* Text */}
        <div className='bg-white rounded-lg shadow-lg p-8 text-justify'>
          <p className="text-lg text-gray-700 mb-4">The documents page is a section of the application where users can upload and manage zip files to insert data in the database. Additionally, they can also search and filter existing documents, with anotations criteria.</p>
          <p className="text-lg text-gray-700 mb-4">On the documents page, users can see a list of all the documents they have uploaded, with detailed information such as name, author, date, and other information. They can also click on a document to open it and view its contents.</p>
          <p className="text-lg text-gray-700 mb-4">Furthermore, the documents page allows users to upload new zip files to the application. When a file is successfully uploaded, it is automatically decompressed and added to the list of documents.</p>

        {/* End Text */}
        </div>  

        {/* Buttons */}
        <div className="flex justify-center space-x-4 mt-8">

          <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition-all duration-500 transform hover:scale-110">
            <Link href='/documents/upload'>Upload a zip Now</Link>
          </button>

          <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition-all duration-500 transform hover:scale-110">
            <Link href='/documents/insert'>Create a document</Link>
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

export default DocumentsPage