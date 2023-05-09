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
      <Footer/>
    </div>
  );
};

export default Layout;