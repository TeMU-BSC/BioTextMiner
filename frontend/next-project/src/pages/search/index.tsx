import Footer from "@/components/footer";
import NavBar from "@/components/navbar";
import React from "react";

const SearchPage = () => {
  return (
    <div>
      <NavBar></NavBar>
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 m-3">
        <div className="text-center p-5">
          <h1 className="text-4xl font-bold mb-4">Search</h1>
        </div>
        <div className="flex items-center mb-4">
          <label htmlFor="search" className="mr-4 font-medium">
            Search:
          </label>
          <input
            type="text"
            id="search"
            name="search"
            className="border border-gray-300 px-4 py-2 rounded-md flex-grow"
          />
          <br></br>
          <div>
            <button
              id="search-document-btn"
              onClick={() => console.log("Search documents")}
              className="ml-4 bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
            >
              Search documents
            </button>
            <button
              id="search-entity-btn"
              onClick={() => console.log("Search entity")}
              className="ml-4 bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
            >
              Search entity
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SearchPage;
