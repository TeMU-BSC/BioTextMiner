import axios from 'axios';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import { Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material';
import NavBar from '@/components/navbar';
import Footer from '@/components/footer';

const Corpus = () => {
  const router = useRouter();
  const { id } = router.query;
  const [corpusData, setCorpusData] = useState(null);

  const [name, setName] = useState('')
  const [labels, setLabels] = useState('')
  const [description, setDesc] = useState('')
  const [vers, setVersion] = useState('')
  const [num_docs, setNum] = useState('')

  useEffect(() => {
    const fetchData = async () => {
      const result = await axios(`http://localhost:5000/corpus/${id}`);
      console.log(id)
      console.log(result.data.result[0])


      setCorpusData(result.data);
      setName(result.data.result[0][1])
      setLabels(result.data.result[0][2])
      setDesc(result.data.result[0][3])
      setVersion(result.data.result[0][4])
      if ((result.data.result[0][5]) != null) {
        setNum(result.data.result[0][5])

      } else {
        setNum('0')
      }



    };

    if (id) {
      fetchData();
    }
  }, [id]);
  // console.log(result.data)
  console.log(name)


  return (
    <>
      <NavBar />
      <div className="m-8 max-w-5xl mx-auto p-6 bg-white shadow-md rounded-lg">
        <h1 className="font-bold text-2xl mb-4">Corpus {name}</h1>
        <div className="grid grid-cols-2 gap-4">
          <p className="text-gray-600 font-medium">Corpus Id:</p>
          <p>{id}</p>
          <p className="text-gray-600 font-medium">Description:</p>
          <p>{description}</p>
          <p className="text-gray-600 font-medium">Labels:</p>
          <p>{labels}</p>
          <p className="text-gray-600 font-medium">Version:</p>
          <p>{vers}</p>
          <p className="text-gray-600 font-medium">Number of documents:</p>
          <p>{num_docs}</p>
        </div>
      </div>

      <div>
        <div className="absolute inset-x-0 bottom-0">
          <Footer />
        </div>
      </div>
    </>
  );
};

export default Corpus;
