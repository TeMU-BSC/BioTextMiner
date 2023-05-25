/**
 * @file home main page
 * @author Siddique Muhammad
 * @version 1.1
 */


/**
 * @imports
 * @Image from next/image
 * @Layout component
 */
import Image from 'next/image';
import Layout from '@/components/Layout';


/**
 * @const HomePage
 * @returns html home page
 */
const HomePage = () => (
  
    <Layout>

    <header
      className="flex items-center justify-center h-screen mb-12 bg-fixed bg-center bg-cover custom-img"
      >
      <div className="p-5 text-2xl bg-purple-300 bg-opacity-50 rounded-xl">
          Welcome to BioTextMiner!
      </div>
    </header>
    
    <main className="flex-grow">

      {/* Section welcome */}
      <section>
      <div className="justify-center items-center mx-auto my-8 px-60">
          <div className="text-center">
          <h1 className="text-4xl font-bold mb-6">Welcome to BioTextMiner</h1>
          
          <div className=''>
              <p className="text-l animate-pulse text-black-900 text-xl text-justify">BioTextMiner is a web application developed by the NLP4BIA that provides a user-friendly interface for corpus control of biomedical corpora. With BioTextMiner, researchers can easily manage and manipulate large-scale biomedical text data by organizing and curating it in a centralized database </p>
          </div>
          </div>
      </div>
      </section>

      {/* Section image */}
      <section>
      <div className="max-w-screen-lg mx-auto mb-10">
          <div className="bg-white rounded-md overflow-hidden shadow-2xl">
          <Image
              className="object-cover mx-auto"
              src="/../public/nlp.jpg"
              alt="Picture of the author"
              width={800}
              height={100}
          />
          </div>
      </div>
      </section>

    </main>
  
    </Layout>
)

export default HomePage