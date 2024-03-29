/**
   * @file index.tsx Typescript file. 
   * @description Search documents in the database
   * @version 1.0
   * @author Siddique Muhammad
*/

/**
 * @imports
 * Layout
 * React library, useState
 */
import Layout from "@/components/Layout";
import { useRouter } from "next/router";
import React, { useState } from "react";


/**
 * @interface SearchResult
 * @description interface for results
 */
interface SearchResult {
    id:string;
    name: string;
    data: string;
}
  
  
/**
 * @constant SearchDocs
 * @returns html page
 */
const SearchDocs = () => { 

    // Define constants
    const [isLoading, setIsLoading] = useState(false);
    const [keyword, setKeyword] = useState(''); // query passed in the searc
    const [message, setMessage] = useState(''); // message to show of results found
    const [results, setResults] = useState<SearchResult[]>([]);
    const [selectedResult, setSelectedResult] = useState<SearchResult | null>(
      null
    );
    const [errors, setErrors] = useState('')

    // Next router
    const router = useRouter();

    /**
     * @constant handleSubmit
     * @param event
     */
    const handleSubmit = async (event:any) => {

        // preventDefault
        event.preventDefault();

        // set isLoading to true to show the loading animation
        setIsLoading(true); 
        
        // setErrors blank on Submit
        setErrors(''); 

        // Reset values
        setSelectedResult(null);
        setResults([]);
    
        // Response from the server

        try {
            const response = await fetch('http://localhost:5000/search-elastic', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ keyword }),
            });
            // const data = await response.json();

            // console.log(response)
        
            if (response.status==500) {
                setErrors('An error occurred')

            } else if (response.status==400) {
                setErrors('No data received')
            }
            else {
                // Set data as a result
                const data = await response.json();
                console.log(data)

                setResults(data)
                console.log(data)
                // Results length
                const numResults = data.length;


                // If there are results, show them; else "No data found" message.
                if (numResults > 0) {
                // setResults(data);
                setMessage(`${numResults} result${numResults === 1 ? '' : 's'} found`);
                } else {
                    setMessage('No data found');
                }
            }
        } catch (error) {
            setErrors('An error occurred');
        } finally {
            setIsLoading(false);
        }

      };


    return (
       <Layout>

        {/* General Div*/}
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 m-3">

        {/* Heading */}
        <div className="text-center p-5">
            <h1 className="text-4xl font-bold mb-4">
            Semantic Search Engine
            </h1>
        {/* End Heading */}
        </div>

        {/* Search (Results and selected) */}
        <div className="flex flex-row">
            
            {/* Searching (Search and results) */}
            <div className="basis-full">

            <form onSubmit={handleSubmit}>

                {/* Search input */}
                <div className="flex items-center mb-4">
                <label htmlFor="keyword" className="mr-4 font-medium text-xl">
                    Search:
                </label>
                <input
                    type="text"
                    value={keyword} onChange={(e) => setKeyword(e.target.value)}
                    id="keyword"
                    name="keyword"
                    className="border border-gray-300 px-4 py-2 rounded-md flex-grow"
                    required
                />
                <br></br>

                {/* Search button */}
                <div>
                    <button
                    type="submit"
                    id="search-document-btn"
                    onClick={() => console.log("Search documents")}
                    className="ml-4 bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
                    >
                    Search documents  
                    </button>

                {/* End Search button */}
                </div>

                {/* End Search Input */}
                </div>

            </form>

            {/* Show message, count results found  */}
            <div>
                {message && <p className="text-sm">{message}</p>}
            {/* End show message */}
            </div>

            {isLoading ? (
              <div className="p-10">
                <div className="loader"></div>
              </div>
            ) : (
              <div className="grid grid-cols-1 gap-5 mt-8">
                <ul>
                  {results.map((result) => (
                    <div
                      key={result.name}
                      className={`bg-gray-200 p-4 rounded-lg m-2 ${
                        selectedResult === result ? "border-2 border-blue-500" : ""
                      }`}
                    >
                      <label>
                        <input
                          type="checkbox"
                          checked={selectedResult === result}
                          onChange={() => setSelectedResult(result)}
                        />
                        <h1>{result.name}</h1>
                        <span className="ml-2">{result.data.substring(0, 100) + "..."}</span>
                      </label>
                    </div>
                  ))}
                </ul>
              </div>
            )}
          </div>
          <div className="basis-1/2">
            {selectedResult !== null && (
              <div className="ml-9 p-4 bg-gray-200 rounded-lg">
                <h2 className="text-lg font-bold mb-2">{selectedResult.name}</h2>
                <p className="font-bold mb-2">Id document. {selectedResult.id}.</p>

                <p className="mb-2">This is the data for {selectedResult.name}.</p>
                <p className="text-justify">{selectedResult.data.substring(0,300)+"..."}</p>
                <button
                    onClick={() => router.push(`/view/${selectedResult.id}`)}
                    className="mt-4 bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
                >
                    View Document
                </button>
              </div>
            )}
          </div>
        </div>
        {errors}
      </div>
    </Layout>
    );
}


export default SearchDocs;