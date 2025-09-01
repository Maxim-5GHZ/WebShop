import { useState } from 'react'
import './App.css'


function App() {
  return (
    <>
      <Header/>
    </>
  )
}

function Header() {
  return (
    <>
      <header className="container-fluid">
        <div className="row align-items-center bg-primary">
          <div className="col text-center">
            <p className="text-primary">Web Shop</p>
          </div>
        </div>
      </header>
    </>
  );
}

export default App
