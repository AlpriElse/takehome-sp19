import React, { Component } from 'react'
import Counter from './Counter'

class App extends Component {
  render() {
    return (
      <div>
        <h3>{this.props.name}</h3>
        <Counter count={this.props.episodes_seen} />
      </div>
    )
  }
}

export default App
