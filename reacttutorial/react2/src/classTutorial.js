import React from 'react';
import ReactDOM from 'react-dom';
import './styles.css'
import charData from './characterData.js'

/////  BASIC   ////
// HTML: <header class=[...]
// JSX: <header className=[...]
export function ClassEz() {
  return (
    <div>
      <h1>CSS Class tutorial: let us being!</h1>
      <header className="navheader">My colored header!! </header>
    </div>
  )
}

// use braces { } to escape JSX and enter Javascript
// note ES6: let message = `Hello ${student.name} from ${student.city}`;
// thus use braces {} and backtick `` for ES6 mode: {` [...] `}
export function ClassVariable() {
  var fname = "Joe"
  var lname = "Swanson"
  return (<div>
      <div> Hello {fname + ' ' + lname} !! </div>
      <div> Hello {`${fname} you're my bro  Mr ${lname}`} !! </div>
    </div>
    )
}

/////    CSS     /////
// Enter Javascript code: {} 
// Make JS object { } while in JS code
// JS code with JS object inside = {{}}
export function CssTrick() {
  return (
    <div style={{ color: "purple", backgroundColor: "grey" }}>Css trickz </div>)
}


//Better
//Note backgroundColor is not background-color (b/c were are not in CSS)
export function CssTrickBetter() {
  const dopeStyle = {
    color: "red",
    backgroundColor: "slateblue"
  }
  return (    
    <div style={dopeStyle} > Css trickz 2!</div>
  )
}

/////   PROPS   /////
//
export function PersonBlock(props) {
  return (
    <div className="cool-border">
      <p>{props.Person.name}</p>
      <p>{props.Person.catchPhrase}</p>
      <p>This is hard coded</p>
    </div>
  )
}
ReactDOM.render(<PersonBlock Person={{ name: "Bender2222", catchPhrase: "Bite my shiny metal ass" }} />, document.getElementById("PropBlocks1"));

// This is solid!
export function Block2() {
  return (
    <div style={{ color: "blue"}}>
      <PersonBlock Person={{ id: "1", name: "Leela", catchPhrase: "hi-yah! (kick)" }} />
      <PersonBlock Person={{ id: "2", name: "Fry", catchPhrase: "Woo-hoo! I'm gonna be a delivery boy!" }} />
    </div>
  )
}
ReactDOM.render(<PersonBlock Person={{ name: "Proffessor Farnsworth", catchPhrase: "Good news everyone!" }} />, document.getElementById("PropBlocks2"));

// EZ
export function Map101() {
  var numbers = [1, 2, 3, 4, 5];
  var numMap = numbers.map(x => x * x);
  return (<div>map: {numMap.toString()}</div>)
}
ReactDOM.render(<Map101 />, document.getElementById("mapWarmup")); 

//import charadata from characterData.js
export function Map201() {
  var sitcomCharacters = charData.map(x => 'Id: ' + x.id + ', Name: ' + x.name + ', Catch Phrase: ' + x.catchPhrase + ' --- ') 
  return (
    <div>
      {sitcomCharacters}
    </div>
    )
}
ReactDOM.render(<Map201 />, document.getElementById("mapWarmup2"));

//Note, it is best practice to uniquely identify key, to improve performance by reducing redrawing
export function Map202(){
  const charData2 = [
    { id: 1, name: "Will Smith", catchPhrase: "Gettin giggy wit it" },
    { id: 2, name: "Steve Urkel", catchPhrase: "did I do that?" }
  ]
  var sitcomCharacters2 = charData2.map(x => <PersonBlock key={x.id} Person={x} />)
  return (
    <div>
      {sitcomCharacters2}
    </div>
    )
}
ReactDOM.render(<Map202 />, document.getElementById("mapWarmup3"));

export class BookBlock extends React.Component {
  render() {
    var message = "Class style message!";
    return (
      <div>
        Book title: {this.props.title}, Author: {this.props.author} also: {message}
        </div>
        )
    }
}
ReactDOM.render(<BookBlock title="Beyond Good And Evil" author="Nietzsche" />, document.getElementById("bookDiv")); 


/////////////////////////////////////////////////
/////////////////////// EVENTS
//////////////////////////////////////////////

export class ClickButton extends React.Component {
  constructor() {
    super()
    this.state = {
      counter: 0
    }
    this.incrementHandle = this.incrementHandle.bind(this)
  }
  incrementHandle() {
    console.log("Hello you clicked");
    //this.state.counter += 1 DONT DO THIS!!!!!!
    this.setState(prevState => { //We pass a lambda function to setState
      return {
        counter: prevState.counter + 1
      }
    })
  } 
  render() {
    return (
      <div style={{ color: "blue" }}>
        <div> ------------BUTTON -----------</div>
        <div> {this.state.counter} </div>
        <button onClick={this.incrementHandle} > Click me xd, counter </button>
      </div>
    )
  }
}

////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////





