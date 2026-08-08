import { useState } from 'react'

import './Welcome.css'
import Header from "../../components/Header/Header.jsx";
import Button from '../../components/Button/Button.jsx'

import { useNavigate } from 'react-router-dom';

export default function Welcome(){
  const navigate = useNavigate();
  function handleClick() {
        navigate('/login');
    }

  return (
    <>
        <label>Фінансова впевненість починається сьогодні.</label>
        <br></br>
        <Button onClick={handleClick}>Увійти</Button>
    </>
  )
}