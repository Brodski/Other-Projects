import React from 'react'
import { Route, Link, BrowserRouter, Switch } from 'react-router-dom';
import { ThemeToggle } from './contexts/ThemeToggle';
import { ThemeContextProvider } from './contexts/ThemeContext';
import { Nav } from './contexts/Nav';
import { BookContextProvider } from './contexts/BookContext';
import { BookList } from './contexts/BookList'

//import Contact from './rContacts';
//import Contact from './rContacts.js'

export class RoutingTut extends React.Component {
  render() { return (
    <BrowserRouter>
      <ThemeContextProvider>
        <div>
          <Nav />
          <BookContextProvider>
            <BookList />
          </BookContextProvider>
          <Switch>
            <Route exact path='/' component={Home} />
            <Route exact path='/user' component={AllUser} />
            <Route component={NotFound} />
          </Switch>
        </div>
      </ThemeContextProvider>
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