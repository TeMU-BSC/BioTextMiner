import NavBar from '../components/navbar'
import { useState } from 'react';
import Link from 'next/link';


export default function RegisterPage() {
  const [name, setName] = useState('');
  const [surname, setSurname] = useState('');
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');


  const handleSubmit = async (event:any) => {
    event.preventDefault();

    // Send a POST request to the register endpoint
    const response = await fetch('http://localhost:5000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name, surname, email, username, password })
    });

    if (response.ok) {

        // Parse the response body as JSON
        const data = await response.json();

      // Redirect to the login page
      window.location.href = '/login';
    } else {
      // Show an error message
      setError('An error has ocurred');
    }
  };



return (
  <div>
      <NavBar />
      
      <form onSubmit={handleSubmit} className="w-80 flex flex-col space-y-4 mx-auto ">
        <label className='text-center m-6 text-sky-400/100 text-3xl font-extrabold underline'>Register</label>
        <div>
          <label htmlFor="name" className="text-gray-700 font-bold mb-2">
            Name
          </label>
          <input
            type="name"
            id="name"
            value={name}
            onChange={(event) => setName(event.target.value)}
            required
            className="w-full border border-gray-400 p-2 rounded-lg"
          />
        </div>
        <div>
          <label htmlFor="surname" className="text-gray-700 font-bold mb-2">
          surname
          </label>
          <input
            type="surname"
            id="surname"
            value={surname}
            onChange={(event) => setSurname(event.target.value)}
            required
            className="w-full border border-gray-400 p-2 rounded-lg"
          />
        </div>
        <div>
          <label htmlFor="email" className="text-gray-700 font-bold mb-2">
            Email
          </label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
            required
            className="w-full border border-gray-400 p-2 rounded-lg"
          />
        </div>
        <div>
          <label htmlFor="username" className="text-gray-700 font-bold mb-2">
            Username
          </label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(event) => setUsername(event.target.value)}
            required
            className="w-full border border-gray-400 p-2 rounded-lg"
          />
        </div>
        <div>
          <label htmlFor="password" className="text-gray-700 font-bold mb-2">
            Password
          </label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
            required
            className="w-full border border-gray-400 p-2 rounded-lg"
          />
        </div>
        <button type="submit" className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded animate-pulse">
          Register
        </button>

        <div className='animate-bounce mx-auto text-red-600 font-bold'>
          {error && <div>{error}</div>}
        </div>
        
        <div className='text-center'>
          Already have an account? 
          <div className='border-2 rounded-xl w-24 mx-auto bg-blue-400  hover:bg-blue-500 p-1 m-2'>
            <Link href={'/login'}> Login!</Link>
          </div>
        </div>
      </form>
    </div>
  )
}