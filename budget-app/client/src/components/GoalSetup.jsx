import React from 'react'
import { useLocation } from "react-router-dom";
import Vector from "../assets/Vector.png";
import { Link } from 'react-router-dom';

const GoalSetup = () => {
    const location = useLocation();
    const {  userInfo, financialInfo, remainingBalance  } = location.state;

    console.log( userInfo, financialInfo, remainingBalance )


  return (
    <div id="goal-setup">
        <Link to="/budget-setup">
        <img
            className="back"
            src={Vector}
            alt="backbutton"
          />
        </Link>
        
       

        <h2>What are your main financial goals?</h2>

    </div>
  )
}

export default GoalSetup
