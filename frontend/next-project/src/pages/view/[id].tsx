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
 * @description interface to specify the structure of documents data
 */
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
  const router = useRouter();
  const { id } = router.query;
  const [documentData, setDocumentData] = useState<DocumentData | null>(null);
  const [htmlContent, setHtmlContent] = useState<string | null>(null);

  useEffect(() => {
    if (id) {
      fetchDocumentData();
    }
  }, [id]);

  const fetchDocumentData = async () => {
    try {
      const response = await fetch(`http://localhost:5000/search-annotations/${id}`);

      const html = await response.text();
      console.log(html);
      // const data = await response.json();
      // console.log(data)
      // setDocumentData(data[0]);
      setHtmlContent(html); // Set the HTML content received from Flask
      console
    } catch (error) {
      console.error("Error fetching document data:", error);
    }
  };

  return (
    <Layout>
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 m-3">
        <div className="text-center p-5">
          <h1 className="text-4xl font-bold mb-4">Document View</h1>
        </div>
        {htmlContent && (
          <div className="ml-9 p-4 bg-gray-200 rounded-lg">
            <div dangerouslySetInnerHTML={{ __html: htmlContent }}></div>
          </div>
        )}
      </div>
    </Layout>
  );
};

export default DocumentView;
