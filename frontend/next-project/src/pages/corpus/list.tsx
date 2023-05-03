import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import NavBar from '@/components/navbar';
import Footer from '@/components/footer';
import Link from 'next/link';

export default function Tabla() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await axios.get(
        'http://localhost:5000/corpus'
      );

      setData(result.data.response);

      // console.log(result)
    };

    fetchData();
  }, []);

  return (
    <>
    <NavBar></NavBar>
    <div className='m-8'>
      <h1 className='max-w-5xl mx-auto font-bold text-xl p-6'>List of corpus</h1>
      <TableContainer component={Paper} className="max-w-5xl mx-auto">
        <Table aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell align="right">Corpus Name</TableCell>
              <TableCell align="right">Labels</TableCell>
              <TableCell align="right">Description</TableCell>
              <TableCell align="right">Version</TableCell>
              <TableCell align="right">Number of documents</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {data.map((row) => (
              <TableRow key={row[0]}>
                <TableCell component="th" scope="row">
                  {row[0]}
                </TableCell>
                <TableCell align="right">
                  <Link href={`/corpus/${row[0]}`}>
                    {row[1]}
                  </Link>
                </TableCell>
                <TableCell align="right">{row[2]}</TableCell>
                <TableCell align="right">{row[3]}</TableCell>
                <TableCell align="right">{row[4]}</TableCell>
                <TableCell align="right">{row[5]}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    <div className='absolute inset-x-0 bottom-0'>
      <Footer></Footer>
    </div>
    </div>
    </>
  );
}
