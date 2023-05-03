import Footer from "@/components/footer";
import NavBar from "@/components/navbar";
import React, { useState } from "react";

const SearchPage = () => {
  
  // Define constants
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const handleSubmit = async (event:any) => {

    event.preventDefault();
    console.log(query)
    const response = await fetch('http://localhost:5000/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    });
    const data = await response.json();
    setResults(data);
    console.log(data);
  };

  // Return html
  return (
    <div>
    <NavBar></NavBar>
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 m-3">
      <div className="text-center p-5">
        <h1 className="text-4xl font-bold mb-4">Semantic Search Engine</h1>
      </div>
      <form onSubmit={handleSubmit}>
        <div className="flex items-center mb-4">
          <label htmlFor="search" className="mr-4 font-medium">
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
          <div>
          <button
          type="submit"
            id="search-document-btn"
            onClick={() => console.log("Search documents")}
            className="ml-4 bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
          >
            Search documents  
          </button>
          </div>
        </div>
      </form>
    </div>
    <div>
      <ul>
        {results.map((result) => (
          // <li key={result.id}>{result.title}</li>
          <li key={result}></li>
        ))}
      </ul>
    </div>
    <div className='absolute inset-x-0 bottom-0'>
      <Footer></Footer>
    </div>
    </div>
  );
};

export default SearchPage;
