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

    <div className="flex-grow">

      {/* Section welcome */}
      <section>
        <div className=" justify-center items-center w-8/12 mx-auto my-8">
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
        <div className="max-w-screen-lg mx-auto">
          <div className="bg-white rounded-md overflow-hidden shadow-md">
            <Image
              className="object-cover"
              src="/../public/nlp.jpg"
              alt="Picture of the author"
              width={950}
              height={100}
            />
          </div>
        </div>
      </section>

    </div>

  </Layout>
)

export default HomePage