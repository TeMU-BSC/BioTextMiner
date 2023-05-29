/**
 * 
 */

import { useRouter } from "next/router";
import Layout from "@/components/Layout";

const DocumentView = () => {
  const router = useRouter();
  const { id } = router.query;

  // TODO: Fetch the document data based on the `id` parameter

  return (
    <Layout>
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 m-3">
        <div className="text-center p-5">
          <h1 className="text-4xl font-bold mb-4">Document View</h1>
        </div>
        <div className="ml-9 p-4 bg-gray-200 rounded-lg">
          <h2 className="text-lg font-bold mb-2">Document ID: {id}</h2>
          {/* Render the document text here */}
        </div>
      </div>
    </Layout>
  );
};

export default DocumentView;
