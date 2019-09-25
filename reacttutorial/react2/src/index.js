import React from 'react';
import ReactDOM from 'react-dom';

import OtherFileFunct from './fromFileHw2'; 
import { ClassEz, ClassVariable, CssTrick, CssTrickBetter, PersonBlock, Block2, Map101, Map201, BookBlock, ClickButton } from './classTutorial'
import * as LotsOfShit from './classTutorial'
import { RoutingTut } from './routing'
//import Contacts from './routing2.js'

/* Set-up
 *   $ npm install -g create-react-app
 *   $ npx create-react-app myfirstreact
 * Run
 *   $ cd myfirstreact
 *   $ npm start
 */

ReactDOM.render(<RoutingTut />, document.getElementById("RoutingTutDiv"));

// Tutorial from: https://www.youtube.com/watch?v=DLX62G4lc44Learn 
//              React.js - Full Course for Beginners - Tutorial 2019  (stopped at around 3 hours)

ReactDOM.render(<ClassEz />, document.getElementById("Class101"));
ReactDOM.render(<ClassVariable />, document.getElementById("VarJS"));
ReactDOM.render(<CssTrick />, document.getElementById("Css1"));
ReactDOM.render(<CssTrickBetter />, document.getElementById("CssBetter")); 
ReactDOM.render(<Block2 />, document.getElementById("PropBlocksBetter")); 
//EVENTS
ReactDOM.render(<ClickButton />, document.getElementById("clickDiv")); 

// Good Tutorial: tic - tac - toe: https://reactjs.org/tutorial/tutorial.html#what-is-react
 /////////////////////////////////



////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////   BASICS   //////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
//  (IDK where i found tutorial)
/////////////////////////////////////////////////////////////////////////////////

// 1st
ReactDOM.render(<h3>HERE IT IS BABY!</h3>, document.getElementById('div1'));

// 2nd
var hw1 = (<ul>
  <li> 2 item1 </li>
  <li>    2 item2 </li>
  <li> 2 item3    </li>
</ul>
);
ReactDOM.render(hw1, document.getElementById('div2'));

// 2.5 render from a file, "fromFilewHw2.js"
//    import OtherFileFunct from './fromFileHw2';   (at top)
ReactDOM.render(<OtherFileFunct />, document.getElementById('div22File'));


// 3 Functional Components
function My1stFunction() {
  return ( <ul>
            <li>3 Func comp item1 </li>
            <li>3 Func comp item2 </li>
            <li>3 Funct comp item3</li>
          </ul>
    );
}
ReactDOM.render(<My1stFunction />, document.getElementById('div3FuncComp'));

//
// 4 Class Components
class Car extends React.Component {
  render() {
    return <h3> 4 I am a Class Component - Car!</h3>;
  }
}
ReactDOM.render(<Car />, document.getElementById('div4ClassComp'));


// 5 Constructor

class DonkeyKong extends React.Component {
  constructor() {
    super();
    this.state = {
      favoritefood: "banana",
      gun: "coconut gun"
    };
  }
  render() {
    return <h3>5 Donkey Kong's favourite food: {this.state.favoritefood}! His {this.state.gun} can fire in spurts</h3>;
  }
}
ReactDOM.render(<DonkeyKong />, document.getElementById('div5Constructor'));
// Change state via "setState()" function.
//
//  changeColor = () => { this.setState({ color: "blue" }); }
//  <button onClick = { this.changeColor }>Change color </button >



//
// 6 Props
// arguments passed into React components
class Mario extends React.Component {
  render() {
    return <h3>6 Mario's favorite food is: {this.props.favoritefood}!</h3>;
    } 
  }
ReactDOM.render(<Mario favoritefood="Mushrooms" />, document.getElementById('div6Props'));

//
// 7 Comp in Comp
class Hamburgers extends React.Component {
  render() {
    return <div> hamburgers: 1000 calories, processed, trans, animal farms</div>;
  }
}
class Restaurant extends React.Component {
  render() {
    return (
      <div>
        <h3>7 Things in a restaurant?</h3>
        <Hamburgers />
        <Hamburgers />
      </div>
    );
  }
}
ReactDOM.render(<Restaurant />, document.getElementById('div7CompInComp'));


//
// 8 Pass arguement (props)
class Person extends React.Component {
  render() {
    return <div> I am {this.props.man.name}! I wear {this.props.man.clothing}. </div>;
  }
}
class Garage extends React.Component {
  render() {
    const info = { name: "Luigi", color: "green", clothing: "overalls" };
    return (
      <div>
        <h3>Tell me about this person</h3>
        <Person man={info} />
      </div>
    );
  }
}
ReactDOM.render(<Garage />, document.getElementById('divPassArg'));
// 8.5 Props in the Constructor
//  ReactDOM.render(<Car model = "Mustang" />

////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////   EVENTS   //////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

// EVENTS
// 1
function doEzEventFunct() {
  alert("You clicked me!");
}
const myButton = (
  <button onClick={doEzEventFunct}>Click me!</button>
);
ReactDOM.render(myButton, document.getElementById('divEventz'));


// 2
// Class (prefered)
class Soccer extends React.Component {
  doEzEvent2() {
    alert("Great Click (class)!");
  }
  render() {
    return (
      <button onClick={this.doEzEvent2}>Click Me Class!</button>
    );
  }
}
ReactDOM.render(<Soccer />, document.getElementById('divEventzClass'));

// 3
// Pass argument
class Sportsball extends React.Component {
  shoot = (a) => {
    alert(a);
  }
  render() {
    return (
      <button onClick={() => this.shoot("Gooooooooooooal")}>JKick the ball! (parameter</button>
    );
  }
}

ReactDOM.render(<Sportsball />, document.getElementById('divEventzArg'));

