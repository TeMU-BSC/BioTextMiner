import { ReactNode } from 'react';
import Footer from './footer';
import NavBar from './navbar';

interface LayoutProps {
  children: ReactNode;
}


const Layout = ({ children }: LayoutProps) => {
  return (
    <div className="bg-gray-100 min-h-screen">
      <NavBar/>
      {children}
      <div className='bottom-0 w-full text-center'>
        <Footer/>
      </div>
    </div>
  );
};

export default Layout;