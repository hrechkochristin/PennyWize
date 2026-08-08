import { useState } from 'react'

import './App.css'

import Header from "./components/Header/Header.jsx";
import Button from "./components/Button/Button.jsx";

import Welcome from "./pages/Welcome/Welcome.jsx";
import LogIn from "./pages/LogIn/LogIn.jsx";
import SignUp from "./pages/SignUp/SignUp.jsx";
import Transactions from "./pages/Transactions/Transactions.jsx";

import { BrowserRouter, Routes, Route, useNavigate } from "react-router-dom";

function NavigationBar() {
  const navigate = useNavigate();

  return (
    <>
      <Button onClick={() => navigate("/transactions")}>Транзакції</Button>
      <Button onClick={() => navigate("/login")}>Логін</Button>
      <Button onClick={() => navigate("/signup")}>Реєстрація</Button>
    </>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <div>
        <main>
          <Routes>
            <Route
              path="/"
              element={
                <>
                  <Welcome />
                </>
              }
            />
            <Route path="/transactions" element={<Transactions />} />
            <Route path="/login" element={<LogIn />} />
            <Route path="/signup" element={<SignUp />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}
