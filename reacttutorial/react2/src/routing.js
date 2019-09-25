import React from 'react'
import { Route, Link, BrowserRouter, Switch } from 'react-router-dom'
//import Contact from './rContacts';
//import Contact from './rContacts.js'

export class RoutingTut extends React.Component {
  render() { return (
    <BrowserRouter>
      <div>
        <ul>
          <li> <Link to="/"> Home </Link> </li>
          <li> <Link to="/user"> Userz </Link> </li>
          <li> <Link to="/nonexistentlink"> dead link </Link> </li>
        </ul>
        <Switch>
          <Route exact path='/' component={Home} />
          <Route exact path='/user' component={AllUser} />
          <Route component={NotFound} />
          </Switch>
      </div>
    </BrowserRouter>
    )
  }
}
//export default RoutingTut

function UserInfo(match) {
  return (
    <div>{match.params.id}</div>
    )
}
const User = ({ match }) => <p>{match.params.id}</p>

class AllUser extends React.Component {
  render() {
    //const { params } = this.props.match
    const { url } = this.props.match
    console.log(this.props)
    return (
      <div>
        <div>USER</div>
          <li> <Link to="/user/1"> Userz 1 </Link> </li>
          <li> <Link to="/user/2dank"> Userz 2 </Link> </li>
          <li> <Link to="/user/3"> Userz 3</Link> </li>
        <Route path="/user/:id" component={User} />
      </div>
      )
  }
}



class Home extends React.Component {
  render() {
    return (
      <div>HOME!</div>
    )
  }
}

function NotFound() {
  return (
    <div>NOTHING WAS FOUND</div>
  )
}