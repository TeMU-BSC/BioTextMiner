/**
 * @file Navbar.tsx
 * @description NavBar for the application
 * @author Siddique Muhammad
 * @version 1.0
 */


/**
 * @imports
 * @Link from next/link
 * @Image from next library
 * @Cookies from js-cookie
 * @router from next/router
 */
import Link from 'next/link';
import Image from 'next/image';
import { useEffect, useState } from 'react';
import Cookies from 'js-cookie';
import router from 'next/router';



/**
 * @const Navbar
 * @descriptiion manages navbar
 * @returns html navbar
 */
const NavBar = () => {

  // Perform localStorage action
  const [user, setUser] = useState<string | null>(null);
  const [isAdmin, setIsAdmin] = useState(false);

  useEffect(() => {
    try {
      const userData = localStorage.getItem('user');
      const role = localStorage.getItem('role') || '';
      setIsAdmin(role === 'admin');
      
      // If userData is True, update and set user state variable
      if(userData) {
        setUser(userData);
      }

    } catch (error) {
      // handle error
    }
  }, []);

  // Handle Logout Action
  const handleLogout = () => {

    // Remove the user data from local storage
    localStorage.removeItem('user');
    
    // Remove the cookies
    Cookies.remove("loggedin");
    // Cookies.remove("userId");

    // Refresh the page to reflect the logout state
    router.push('/');
  };

  // Return html navbar
  return (
    
    <nav className="bg-gray-900 text-white py-px">

      {/* Max width */}
      <div className="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">

        {/* Navbar container */}
        <div className="relative flex items-center justify-between h-16">

     
          <Image 
            className="rounded"
            src="/../public/bsc.jpg"
            alt="Picture of the author"
            width={75}
            height={10}
          />

          {/* Navigation links */}
          <div className="hidden sm:block sm:ml-6">
            <div className="flex">
              <Link href="/" className="px-3 py-2 rounded-md text-base font-medium">
                Home
              </Link>

              {/* Show Login/Register or Logout depending on isLogged or not */}
              {/* <div> */}
                {user ? (
                <div>
                  <Link href="/view" className="ml-4 px-3 py-2 rounded-md text-base font-medium">
                    View
                  </Link>
                  <Link href="/search" className="ml-4 px-3 py-2 rounded-md text-base font-medium">
                    Search
                  </Link>
                  <Link href="/analyze" className="ml-4 px-3 py-2 rounded-md text-base font-medium">
                    Analyze
                  </Link>
                  <button className="ml-4 px-3 py-2 rounded-md text-base font-medium" onClick={handleLogout}>
                        Logout
                  </button>
                </div>
                ) : (
                  <>
                  <Link href="/login" className="ml-4 px-3 py-2 rounded-md text-base font-medium">
                  Login
                  </Link>
                  <Link href="/register" className="ml-4 px-3 py-2 rounded-md text-base font-medium ">
                    Register
                  </Link>
                  </>
                )}

            </div>

          </div>

        </div>

      </div>

    </nav>
  )
};

export default NavBar;