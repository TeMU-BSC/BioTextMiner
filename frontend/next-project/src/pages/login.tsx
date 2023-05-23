/**
   * @file login.tsx Typescript file. 
   * @description Login page with form and fetching with login api
   * @version 1.2
   * @author Siddique Muhammad
*/

/**
 * @imports
 * NavBar component
 * Footer 
 * React library
 * Link from next/link
 * Cookies
 */
import Footer from '@/components/footer'
import NavBar from '@/components/Navbar'
import Link from 'next/link'
import { useState } from 'react'
import Cookies from "js-cookie";


/**
 * @function Login
 * Definition of the function
 * @returns html page
 */
export default function Login() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [mis, setMis] = useState('')

  /**
   * Handle submit
   * @param e 
   */
  const handleSubmit = async (e:any) => {
    e.preventDefault()

    // Send a POST request to the login endpoint
    const res = await fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    })

    const data = await res.json()

    if (data.error || data.err=="true" || data.data==null) {
      setError(data.error)
      setMis("Error")
    }  else {
      // console.log(data.mis)
      localStorage.setItem('user', username)

      // Set cookie for logged session
      Cookies.set("loggedin", "true");
      // Cookies.set("userId", "true");
      console.log(data)
      // Cookies.set("userId", data.user.user_id);
      
      window.location.href = '/'
    } 
  }
  
  // Return html
  return (
    <div>
    <NavBar></NavBar>
    <div>
      <form onSubmit={handleSubmit} className="w-80 flex flex-col space-y-4 mx-auto">
      <label className='text-center m-6 text-sky-400/100 text-3xl font-extrabold underline'>Login</label>
        <div>
          <label htmlFor="username" className="text-gray-700 font-bold mb-2">Username:</label>
          <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} className="w-full border border-gray-400 p-2 rounded-lg"/>
        </div>
        <div>
          <label htmlFor="password" className="text-gray-700 font-bold mb-2">Password:</label>
          <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} className="w-full border border-gray-400 p-2 rounded-lg"/>
        </div>

        <button type="submit" className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded animate-pulse">
        Login</button>

        <div className='animate-bounce mx-auto text-red-600 font-bold'>
          {error && <div>{error}</div>}
          {mis && <div>{mis}</div>}
        </div>

        <div className='text-center'>
          Don not have an account? 
          <div className='border-2 rounded-xl w-24 mx-auto bg-blue-400  hover:bg-blue-500 p-2 m-2'>
            <Link href={'/register'}> Register!</Link>
          </div>
        </div>
      </form>
    </div>
    <div className='absolute inset-x-0 bottom-0'>
      <Footer></Footer>
    </div>
    </div>
  )
}