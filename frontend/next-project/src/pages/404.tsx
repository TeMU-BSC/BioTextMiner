import Layout from '@/components/Layout';
import Link from 'next/link';

function PageNotFound() {
  return (
    <Layout>
        <div className='min-h-screen'>
            <div className='text-center'>
                <h1
                className="font-extrabold text-transparent text-8xl bg-clip-text bg-gradient-to-r from-blue-400 to-green-600 m-10">
                Page Not Found
                </h1>
            </div>

            <div className='border-4 w-96 mx-auto text-center p-2'>
                <p className='p-4 italic'>
                    The page you requested could not be found.
                </p>
                <div className='border-2 w-60 mx-auto bg-gradient-to-r from-cyan-300 to-blue-400 p-2 rounded-lg'>
                    <Link href="/">
                        Go back to the homepage
                    </Link>
                </div>
            </div>
        </div>
    </Layout>
  );
}

export default PageNotFound;