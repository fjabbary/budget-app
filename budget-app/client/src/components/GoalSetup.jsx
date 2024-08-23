import React, { useState } from 'react';
import { useLocation, Link } from "react-router-dom";
import Vector from "../assets/Vector.png";
import { goals } from '../goals'; 
import Button from 'react-bootstrap/esm/Button';

const GoalSetup = () => {
  const location = useLocation();
  const { userInfo, financialInfo, remainingBalance } = location.state;
  console.log(userInfo, financialInfo, remainingBalance);

 
  const [selectedGoals, setSelectedGoals] = useState([]);
  const [step, setStep] = useState("one"); 

  const [customGoalName, setCustomGoalName] = useState('')


  const handleGoalClick = (goal) => {
    const foundGoal = selectedGoals.find(
      (item) => item.id === goal.id
    );
    if (!foundGoal) {
      goal.selected = true;
      setSelectedGoals([...selectedGoals, goal]);
    } else {
      goal.selected = false;
      const filteredGoals = selectedGoals.filter(
        (item) => item.id !== goal.id
      );
      setSelectedGoals(filteredGoals);
    }
  };


  const handleCustomGoalName = e => {
    setCustomGoalName( e.target.value)

    const updatedGoals = selectedGoals.map(item => {
      if(item.id === 'custom') {
          return {...item, text: e.target.value}
      }
      return item
    })

    setSelectedGoals(updatedGoals)
  }
  
  return (
    <div id="goal-setup">
      {step === "one" && (
        <div>
          <Link to="/budget-setup">
            <img className="back" src={Vector} alt="backbutton" />
          </Link>

          <h2>What are your main financial goals?</h2>

          <div className="goalset d-flex flex-wrap gap-3">
            {goals.map((goal) => (
              <div
                className="goalset-item d-flex flex-column align-items-center justify-content-center"
                key={goal.id}
                onClick={() => handleGoalClick(goal)}
                style={{
                  border: goal.selected ? "3px solid #f6f5f7" : "none",
                }}
              >
                <img src={goal.icon} alt={goal.text} className="goalset-icon" />
                <p className="goalset-text mt-2">{goal.text}</p>
              </div>
            ))}
          </div>

          {  !selectedGoals.find(item => item.id === 'custom') && <Button className="btn btn-green w-100"
          onClick={() => setStep('two')}
          disabled={selectedGoals.length === 0}
          >Continue</Button>}

          { selectedGoals.find(item => item.id === 'custom') && <div className="custom-goal-info">
            <p>Enter your custom financial goal</p>
            <input type="text" onChange={handleCustomGoalName} name='customName' value={customGoalName} />
            {/* <p>What amount do you want to save</p> */}
            {/* <input type="number" placeholder='$0.00' onChange={handleCustomGoalInfo} name="customAmount" value={customGoalInfo.customAmount} /> */}
            <Button className="btn btn-green w-100"
              onClick={() => setStep('two')}
              disabled={!customGoalName}
              >Continue</Button>
          </div>}
        </div>
      )}
      
      {step === "two" && (
        <div>
          <img
            className="back"
            src={Vector}
            alt="backbutton"
            onClick={() => setStep("one")}
          />

          <h2>Which one is your primary focus?</h2>
          
          


          <div className="goal-list">
            {selectedGoals.map((item) => (
              <div
                className="goal-item d-flex justify-content-between align-items-center px-3 py-3 my-2"
                key={item.id}
              >
                <div className="goal-icon">
                  <img src={item.icon} alt={item.text} className="me-2" />{" "}
                  <span>{item.text}</span>{" "}
                </div>
                <div className="goal-input d-flex align-items-center">
                  <input
                    name="goal"
                    type="radio"
                    className="w-100 p-2"
                  />{" "}
                </div>
              </div>
            ))}
          </div>



          <Button
            className="btn btn-green w-100"
            onClick={() => setStep("three")}
          >
            Continue
          </Button>
        </div>
      )}
    </div>
  );
};

export default GoalSetup;