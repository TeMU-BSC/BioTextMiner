import Link from 'next/link';
import Image from 'next/image';
import { useEffect, useState } from 'react';


const NavBar = () => {

  // Perform localStorage action
  const [user, setUser] = useState<string | null>(null);

  useEffect(() => {
    try {
      const userData = localStorage.getItem('user');

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

    // Refresh the page to reflect the logout state
    window.location.reload();
  };

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
                  <Link href="/search" className="ml-4 px-3 py-2 rounded-md text-base font-medium">
                    Search
                  </Link>
                  <Link href="/corpus" className="ml-4 px-3 py-2 rounded-md text-base font-medium">
                  Corpus
                  </Link>
                  <Link href="/documents" className="ml-4 px-3 py-2 rounded-md text-base font-medium">
                    Documents
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