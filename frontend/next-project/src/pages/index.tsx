import NavBar from '../components/navbar'
import Link from 'next/link';
import Image from 'next/image';

const HomePage = () => (
  <div>
    <NavBar />
    <div className="flex items-center justify-center m-8">
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-6">Welcome to BioTextMiner</h1>
        
        <div className='w-96'>
          <p className="text-lg animate-pulse text-black-900 text-xl">BioTextMiner is a web application developed by the NLP4BIA that provides a user-friendly interface for corpus control of biomedical corpora. With BioTextMiner, researchers can easily manage and manipulate large-scale biomedical text data by organizing and curating it in a centralized database </p>
        </div>

        <div>
        {/* <Image
          src="https://editor.analyticsvidhya.com/uploads/50641nlp.jpeg"
          alt="Picture of the author"
          width={500}
          height={500}
        /> */}
        </div>
      </div>
    </div>
  </div>
)

export default HomePage