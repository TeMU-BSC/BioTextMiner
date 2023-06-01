/**
 * @file view.tsx
 * @description list all documents from data base
 * @author Siddique Muhammad
 * @version 1.1
 */


/**
 * @imports
 */
import { useState, useEffect } from 'react';
import Layout from '@/components/Layout';
import { TextField, Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Pagination } from '@mui/material';
import { useRouter } from 'next/router';
import Link from 'next/link';


/**
 * @interface
 * @description Document data interface
 */
interface Document {
    id: number;
    name: string;
    // Agrega más propiedades del documento según sea necesario
  }


  /**
   * @constant ViewPage
   * @returns html
   */
const Viewpage = () => {

    // Definitions
    const [searchTerm, setSearchTerm] = useState('');
    const [documents, setDocuments] = useState<Document[]>([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [documentsPerPage] = useState(10);

    // Router
    const router = useRouter();

    // Handle pagination
    const handlePaginationChange = (_event: React.ChangeEvent<unknown>, page: number) => {
        setCurrentPage(page);
    };

    // fetchDocuments
    const fetchDocuments = async () => {

    // Try to fetch, except errors.
    try {

        // Response
        const response = await fetch(`http://localhost:5000/api/documents?search=${encodeURIComponent(searchTerm)}`);

        // parse response to json
        const data = await response.json();

        // Set id and name
        const documents = data.response.map((item: any) => ({
        id: item[0],
        name: item[1],
        // Otras propiedades según sea necesario
        }));

        // Set documents in constant
        setDocuments(documents);
    } catch (error) {

        // Catch errors
        console.error(error);
        setDocuments([]);
    }
    };

    // useEffect to fecth the documents data
    useEffect(() => {
        fetchDocuments();
    }, [searchTerm, currentPage]);

    // Logic for displaying documents
    const indexOfLastDocument = currentPage * documentsPerPage;
    const indexOfFirstDocument = indexOfLastDocument - documentsPerPage;
    const currentDocuments = documents.slice(indexOfFirstDocument, indexOfLastDocument);

    // Return html
    return (
    <Layout>

        {/* Section to display the documents data and search */}
        <section className="text-center m-10">
            <h1 className="text-4xl font-bold">Document List</h1>

            {/* Search Field */}
            <div className="my-4 flex justify-center">
                    <TextField
                    label="Search"
                    variant="outlined"
                    value={searchTerm}
                    onChange={(e: React.ChangeEvent<HTMLInputElement>) => setSearchTerm(e.target.value)}
                />
            </div>

            {/* Table to display the documents */}
            <TableContainer component={Paper}>
                <Table>

                    {/* Table Head */}
                    <TableHead>
                        <TableRow>
                            <TableCell>ID</TableCell>
                            <TableCell>Name</TableCell>
                            {/* Agregar más encabezados de tabla según sea necesario */}
                        </TableRow>
                    </TableHead>

                    {/* Table Body */}
                    <TableBody>
                        {currentDocuments.map((document) => (
                            <TableRow key={document.id}>
                            <TableCell>
                                <span style={{ color: 'black' }}>{document.id}</span>
                            </TableCell>
                            <TableCell>
                                <Link 
                                href={`/view/${document.id}`}
                                className='text-blue-600 font-bold'
                                >
                                    {document.name}
                                </Link>
                            </TableCell>
                            {/* Agregar más celdas de tabla para otras propiedades del documento */}
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>

            {/* Paginations */}
            <Pagination
                count={Math.ceil(documents.length / documentsPerPage)}
                page={currentPage}
                onChange={handlePaginationChange}
            />
        </section>
    </Layout>
    );
};

// Export ViewPage
export default Viewpage;