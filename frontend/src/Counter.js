import React, { Component } from 'react'

class Counter extends Component {
  constructor(props) {
    super(props)
    this.state = {
      count: this.props.count
    }
  }

  increment = () => {
    this.setState(state => ({
      count: state.count + 1
    }))
  }

  decrement = () => {
    this.setState(state => {
      if (state.count > 0) {
        return {
          count: state.count -1
        }
      }
    })
  }

  render() {
    return (
      <div>
        <p>{this.state.count}</p>
        <button onClick={this.increment}>Increment</button>
        <button onClick={this.decrement}>Decrement</button>
      </div>
    )
  }
}

export default Counter
