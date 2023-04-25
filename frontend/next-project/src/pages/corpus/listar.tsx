import NavBar from '@/components/navbar'
import axios from 'axios'
import { useEffect, useState } from 'react'

type CorpusData2 = {
    corpus_id: number,
    corpus_name: string,
    labels: string,
    description: string,
    version: string,
    n_docs: number
  }
  

type CorpusData = {
  // Definimos la estructura de los datos de respuesta
  // que vamos a recibir del endpoint Flask
  result: string,
  response: any
}

export default function CorpusPage() {
  const [corpusData, setCorpusData] = useState<CorpusData>()

  useEffect(() => {
    // Hacemos una solicitud HTTP al endpoint Flask
    axios.get<CorpusData>('http://localhost:5000/corpus')
      .then(response => setCorpusData(response.data))
      .catch(error => console.error(error))
  }, [])

  return (
    <div>
      {corpusData ?
        <>
        <NavBar></NavBar>
          <pre>{JSON.stringify(corpusData.response, null, 2)}</pre>
          <h1>{corpusData.result}</h1>

        </>
        :
        <p>Cargando datos...</p>
      }
    </div>
  )
}
