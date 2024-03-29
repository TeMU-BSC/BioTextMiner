/**
 * @file footer section
 * @author Siddique Muhammad
 * @version 1.1
 */


/**
 * @const Footer 
 * @description html Footer
 */
const Footer = () => {

    // Return Footer html
    return (
        <footer className="mt-10 left-0 z-20 w-full p-4 bg-white border-t border-gray-200 shadow md:flex md:items-center md:justify-between md:p-6 dark:bg-gray-800 dark:border-gray-600">
            <span className="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2023 <a href="https://temu.bsc.es/" className="hover:underline">Temu-BSC</a>. All Rights Reserved.
            </span>
            <ul className="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0">
                <li>
                    <a href="/view" className="mr-4 hover:underline md:mr-6">View</a>
                </li>
                <li>
                    <a href="/search" className="mr-4 hover:underline md:mr-6">Search</a>
                </li>
                <li>
                    <a href="/analyze" className="mr-4 hover:underline md:mr-6">Analyze</a>
                </li>
            </ul>
        </footer>
    );
};

export default Footer;
