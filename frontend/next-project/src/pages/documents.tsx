import NavBar from "../components/navbar";
import Link from "next/link";

const DocumentsPage = () => (
  <div>
    <NavBar />
    <div className="flex items-center justify-center m-8">
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-6">Documents Page</h1>
        <div className="w-96">
          <p className="text-lg text-gray-700 mb-4">
            The documents page is a section of the application where users can
            upload and manage zip files to insert data in the database.
            Additionally, they can also search and filter existing documents,
            with anotations criteria.
          </p>
          <p className="text-lg text-gray-700 mb-4">
            On the documents page, users can see a list of all the documents
            they have uploaded, with detailed information such as name, author,
            date, and other information. They can also click on a document to
            open it and view its contents.
          </p>
          <p className="text-lg text-gray-700 mb-4">
            Furthermore, the documents page allows users to upload new zip files
            to the application. When a file is successfully uploaded, it is
            automatically decompressed and added to the list of documents.
          </p>
        </div>
        <div className="space-x-4">
          <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition-all duration-500 transform hover:scale-110">
            <Link href="/documents/upload">Upload a zip Now</Link>
          </button>
          <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition-all duration-500 transform hover:scale-110">
            <Link href="/documents/insert">Create a document</Link>
          </button>
        </div>
      </div>
    </div>
  </div>
);

export default DocumentsPage;
