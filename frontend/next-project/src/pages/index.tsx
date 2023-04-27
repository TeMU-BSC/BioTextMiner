import NavBar from '../components/navbar'
import Link from 'next/link';
import Image from 'next/image';
import Footer from '@/components/footer';

const HomePage = () => (
  <div>
    <NavBar />
    <div className="flex justify-center items-center m-9 w-8/12 mx-auto">
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-6">Welcome to BioTextMiner</h1>
        
        <div className=' m-10  '>
          <p className="text-l animate-pulse text-black-900 text-xl text-justify">BioTextMiner is a web application developed by the NLP4BIA that provides a user-friendly interface for corpus control of biomedical corpora. With BioTextMiner, researchers can easily manage and manipulate large-scale biomedical text data by organizing and curating it in a centralized database </p>
        </div>

        <div className='grid h-screen place-items-center'>
          <div className='drop-shadow-2xl'>
            <Image 
                className="rounded"
                src="/../public/nlp.jpg"
                alt="Picture of the author"
                width={950}
                height={100}
              />
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
)

export default HomePage