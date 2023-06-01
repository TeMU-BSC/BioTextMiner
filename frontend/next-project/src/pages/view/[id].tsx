/**
 * @file [id].tsx
 * @description view for a document
 * @author Siddique Muhammad
 * @version 1.1
 */


/**
 * @imports
 */
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import Layout from "@/components/Layout";

/**
 * @interface DocumentData
 * @description interface to specify the strcuture of documents data
 */
// Interfaz para especificar la estructura de los datos del documento
interface DocumentData {
  data: string;
  id: string;
  name: string;
}

/**
 * @constant DocumentView
 * @returns html
 */
const DocumentView = () => {

  // Definitions
  const router = useRouter();
  const { id } = router.query;
  const [documentData, setDocumentData] = useState<DocumentData | null>(null);

  // useEffect
  useEffect(() => {
    if (id) {
      fetchDocumentData();
    }
  }, [id]);

  /**
   * @constant fetchDocumentData
   */
  const fetchDocumentData = async () => {
    try {
      const response = await fetch(`http://localhost:5000/search-document/${id}`);
      const data = await response.json();
      setDocumentData(data[0]);
    } catch (error) {
      console.error("Error fetching document data:", error);
    }
  };

  // Return html 
  return (
    <Layout>
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 m-3">
        <div className="text-center p-5">
          <h1 className="text-4xl font-bold mb-4">Document View</h1>
        </div>
        {documentData && (
          <div className="ml-9 p-4 bg-gray-200 rounded-lg">
            <h2 className="text-lg font-bold mb-2">Document ID: {id}</h2>
            <h3 className="text-lg font-bold mb-2">Name: {documentData.name}</h3>
            <p className="text-justify">{documentData.data}</p>
          </div>
        )}
      </div>
    </Layout>
  );
};

export default DocumentView;
