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

interface Corpus {
  id: number;
  corpus_name: string;
  labels: string[];
  description: string;
  version: string;
  numDocuments: number;
}


/**
 * @const AnalyzePage
 * @description Manages the analization section. 
 *              Lists corpus and selecting one, redirects to dashboard.
 * @returns html page
 */
const AnalyzePage = () => {
  const [corpusData, setCorpusData] = useState<Corpus[]>([]);

  useEffect(() => {
    const fetchCorpusData = async () => {
      try {
        const response = await fetch('http://localhost:5000/corpus');
        const data = await response.json();
        setCorpusData(data.response);
        console.log(data.response[0].corpus_id)
      } catch (error) {
        console.error('Error fetching corpus data:', error);
      }
    };
    fetchCorpusData();

  }, []);

  return (
    <Layout>
    <div className="flex flex-col">
      <div className="flex-grow">
        <div className="flex flex-col items-center justify-center my-8">
          <div className="text-center w-10/12">
            <h1 className="text-4xl font-bold mb-6">Analyze</h1>
            <p className='mb-10'>Here are some corpus, you can see the complete information by pressing some card.</p>
            {/* Corpus Cards */}
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
              {corpusData.map((corpus) => (
                <Card key={corpus.id}>
                  <CardContent>
                    <Typography variant="h5" component="h2">
                      Corpus name: {corpus.corpus_name}
                    </Typography>
                    <Typography color="textSecondary" gutterBottom>
                      Labels: {corpus.labels}
                    </Typography>
                    <Typography variant="body2" component="p">
                      Description: {corpus.description}
                    </Typography>
                    <Typography variant="body2" component="p">
                      Version: {corpus.version}
                    </Typography>
                    <Typography variant="body2" component="p">
                      Number of Documents: {corpus.numDocuments}
                    </Typography>
                  </CardContent>
                </Card>
              ))}
            </div>
            {/* End Corpus Cards */}

          </div>
        </div>
      </div>
    </div>
  </Layout>
  );
}

export default AnalyzePage;
