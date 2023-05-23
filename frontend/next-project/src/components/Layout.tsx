/**
 * @file Layout.tsx
 * @description Layout for the pages
 * @author Siddique Muhammad
 * @version 1.1.
 */


/**
 * @imports
 * @ReactNode from react library
 * @Footer component
 * @NavBar component
 */
import { ReactNode } from 'react';
import Footer from './Footer';
import NavBar from './Navbar';

/**
 * @interface LayoutProps
 */
interface LayoutProps {
  children: ReactNode;
}


/**
 * @const Layout
 * @return html layout
 */
const Layout = ({ children }: LayoutProps) => {

  return (


    // General Div
    <div className="flex flex-col min-h-screen">

      {/* Include NavBar */}
      <NavBar/>

      {/* Children data */}
      <div className="flex-grow">{children}</div>

      {/* Include Footer */}
      <div className='bottom-0 w-full text-center'>
        <Footer/>
      </div>

    </div>
  );
};


// Export Layout
export default Layout;