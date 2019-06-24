import React from 'react';
import AppNavBar from './AppNavbar'
import GreetingMessageAJAX from './GreetingMessageAJAX';



class App extends React.Component {
  render() {
    return (
      <div>
        <AppNavBar />
        <GreetingMessageAJAX />
      </div>
    )
  }
}

export default App;