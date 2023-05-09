import NavBar from "../components/navbar";
import Link from "next/link";
import { Card, CardContent, Typography } from "@mui/material";
import { useEffect, useState } from "react";
import CorpusImage from "@/components/corpusImage";
import axios from "axios";
export interface Corpus {
  corpus_id: number;
  corpus_name: string;
  labels: string;
  description: string;
  version: number;
  n_docs: number;
}

const CorpusPage = () => {
  const [corpuses, setCorpuses] = useState<Corpus[] | Corpus>([]);
  useEffect(() => {
    axios
      .get<any>("http://localhost:5000/corpus_top")
      .then((response) => setCorpuses(response.data.response))
      .catch((error) => console.error(error));
  }, []);

  const datos: Corpus[] = [
    {
      corpus_id: 1,
      corpus_name: "name",
      labels: "adasd,asdad",
      description: "string bla bla",
      version: 2,
      n_docs: 123,
    },
    {
      corpus_id: 2,
      corpus_name: "name2",
      labels: "adasd,asdad",
      description: "string bla bla 2",
      version: 1,
      n_docs: 13,
    },
    {
      corpus_id: 3,
      corpus_name: "name2",
      labels: "adasd,asdad",
      description: "string bla bla 2",
      version: 1,
      n_docs: 13,
    },
  ];

  const [user, setUser] = useState<string | null>(null);
  useEffect(() => {
    try {
      const userData = localStorage.getItem("user");
      // If userData is True, update and set user state variable
      if (!userData) {
        window.location.href = "/login";
      } else {
        setUser(userData);
      }
    } catch (error) {
      // handle error
    }
  }, []);
  return (
    user && (
      <div>
        <NavBar />
        <div className=" flex items-center flex-col  ">
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
          <div className="flex gap-9 m-2">
            {corpuses.map((corpus: { corpus_id: any }) => (
              <CorpusImage data={corpus} key={corpus.corpus_id}></CorpusImage>
            ))}
          </div>
          <div>
            <button className="m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition-all duration-500 transform hover:scale-110">
              <Link href="/corpus/insert">Insert a corpus Now</Link>
            </button>
            <button className="m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition-all duration-500 transform hover:scale-110">
              <Link href="/corpus/list">List corpus</Link>
            </button>
          </div>
        </div>
      </div>
    )
  );
};
export default CorpusPage;
