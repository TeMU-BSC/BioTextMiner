/**
 * @file [id].tsx
 * @description information of a corpus
 * @author Siddique Muhammad
 */
import axios from 'axios';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import Layout from '@/components/Layout';
import { Card, CardContent, Typography, TableContainer, Table, TableHead, TableRow, TableCell, TableBody } from '@mui/material';
import { List, ListItem, ListItemText } from '@mui/material';
import Link from 'next/link';

/**
 * @const Corpus
 * @returns html
 */
const Corpus = () => {
  const router = useRouter();
  const { id } = router.query;
  const [corpusData, setCorpusData] = useState<any>(null);
  
  const fetchData = async () => {
    try {
      const result = await axios(`http://localhost:5000/corpus_data/${id}`);
      setCorpusData(result.data);
      console.log(result.data.total_annotations)
    } catch (error) {
      console.error('Error fetching corpus data:', error);
    }
  };

  useEffect(() => {
    if (id) {
      fetchData();
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [id]);

  const labels = corpusData?.result[0][3]?.split(','); // Split labels by comma

  return (
    <Layout>
      <div>
        <h1 className='text-4xl font-bold text-center mt-10'>Dashboard</h1>
      </div>

      {corpusData && (
        <div className=" m-8 max-w-5xl mx-auto p-6 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 p-10"> 
          <Card className='bg-gradient-to-r from-green-300 to-blue-300'>
            <CardContent>
              <Typography variant="h5" component="h2" className='text-center p-6 font-bold'>
                {corpusData.result[0][1]}
              </Typography>
              <Typography variant="h5" component="h2" className='text-center'>
                Name of corpus
              </Typography>
            </CardContent>
          </Card>

          <Card className='bg-gradient-to-r from-green-300 to-blue-300'>
            <CardContent>
              <Typography variant="h5" component="h2" className='text-center p-6 font-bold'>
                {corpusData.total_documents}
              </Typography>
              <Typography variant="h5" component="h2" className='text-center'>
                Number of documents
              </Typography>
            </CardContent>
          </Card>

          <Card className='bg-gradient-to-r from-green-300 to-blue-300'>
            <CardContent>
              <Typography variant="h5" component="h2" className='text-center p-6 font-bold'>
              {corpusData.total_annotations}
              </Typography>
              <Typography variant="h5" component="h2" className='text-center'>
                Number of annotations
              </Typography>
            </CardContent>
          </Card>
        </div>
      )}

      {/* List Labels */}  
      <div className='m-8 max-w-5xl mx-auto p-6'>
      <h2 className='text-2xl'>Documents associated:</h2>
        <List>
          {labels && labels.map((label:any, index:any) => (
            <ListItem key={index}>
              <ListItemText primary={label.trim()} />
            </ListItem>
          ))}
        </List>
      </div>

      {/* Table documents by corpus */}
      <div className='m-8 max-w-5xl mx-auto p-6 bg-white shadow-md rounded-lg'>
        <h2 className='text-2xl'>Documents associated:</h2>
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Text ID</TableCell>
                <TableCell>Document Name</TableCell>
                <TableCell>Date</TableCell>
                <TableCell>Author</TableCell>
                <TableCell>Source</TableCell>
                <TableCell>Collection</TableCell>
                <TableCell>Language</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {corpusData &&
                corpusData.resultdoc.map((doc:any) => (
                  <TableRow key={doc[0]}>
                    <TableCell>{doc[0]}</TableCell>                    
                    <TableCell>
                      <Link href={`/view/${doc[0]}`} className="text-blue-600 font-bold underline text-lg">
                        {doc[1]}
                      </Link>
                    </TableCell>
                    <TableCell>{doc[2]}</TableCell>
                    <TableCell>{doc[3]}</TableCell>
                    <TableCell>{doc[4]}</TableCell>
                    <TableCell>{doc[5]}</TableCell>
                    <TableCell>{doc[6]}</TableCell>
                  </TableRow>
                ))}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
    </Layout>
  );
};

export default Corpus;
