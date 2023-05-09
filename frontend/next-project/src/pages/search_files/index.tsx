/**
   * @file index.tsx Typescript file. 
   * @description Search section
   * @version 1.0
   * @author Siddique Muhammad
*/

/**
 * @imports
 * NavBar component
 * Footer 
 * React library, useState
 */
import NavBar from "@/components/navbar";
import Footer from "@/components/footer";
import React, { useState } from "react";


/**
 * @constant SearchPage
 * @returns html page
 */
const SearchPage = () => {
  
  // Define constants
  const [query, setQuery] = useState(''); // query passed in the searc
  const [message, setMessage] = useState(''); // message to show of results found
  const [results, setResults] = useState<string[]>([]); // results to show
  const [selectedResult, setSelectedResult] = useState<string | null>(null);  // selected Result

  /**
   * @constant handleSubmit
   * @param event 
   */
  const handleSubmit = async (event:any) => {

    // preventDefault
    event.preventDefault();

    // Reset values
    setSelectedResult(null);
    setResults([]);

    // Response from the server
    const response = await fetch('http://localhost:5000/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    });

    // Set data as a result
    const data = await response.json();

    // Results length
    const numResults = data.length;

    // If there are results, show them; else "No data found" message.
    if (numResults > 0) {
      setResults(data);
      setMessage(`${numResults} result${numResults === 1 ? '' : 's'} found`);
    } else {
      // setResults(['No data found']);
      setMessage('No data found');
    }
  };

  // Return html
  return (
    <div>

      {/* NavBar */}
      <NavBar></NavBar>

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
              <label htmlFor="search" className="mr-4 font-medium text-xl">
                Search:
              </label>
              <input
                type="text"
                value={query} onChange={(e) => setQuery(e.target.value)}
                id="search"
                name="search"
                className="border border-gray-300 px-4 py-2 rounded-md flex-grow"
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


          {/* Results */}
          <div className="grid grid-cols-1 gap-5 mt-8">
            {results.map((result) => (
              <div key={result} className={`bg-gray-200 p-4 rounded-lg ${selectedResult === result ? 'border-2 border-blue-500' : ''}`}>
              <label>
                <input type="checkbox" checked={selectedResult === result} onChange={() => setSelectedResult(result)} />
                <span className="ml-2">{result}</span>
              </label>
            </div>
            ))}
          {/* End Results */}
          </div>

        {/* End Searching (Search and results) */}
        </div>

        {/* Selected Result */}
        <div className="basis-1/2">
          {selectedResult !== null && (
            <div className="ml-9 p-4 bg-gray-200 rounded-lg">
              <h2 className="text-lg font-bold mb-2">{selectedResult}</h2>
              <p>This is the data for {selectedResult}.</p>
            </div>
          )}
        {/* End Selected Result */}
        </div>

      {/* End Search (Results, search, and selected)*/}
      </div>

      {/* End General Div*/}
      </div>



      {/* Footer */}
      <div className='absolute inset-x-0 bottom-0'>
        <Footer></Footer>
      {/* End Footer */}
      </div>

    </div>
  );
};

// Exports SearchPage
export default SearchPage;