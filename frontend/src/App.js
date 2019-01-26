import React, { Component } from 'react'
import Instructions from './Instructions'
import Show from './Show'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      shows: [
        {id: 1, name: "Game of Thrones", episodes_seen: 0},
        {id: 2, name: "Naruto", episodes_seen: 220},
        {id: 3, name: "Black Mirror", episodes_seen: 3},
      ],
      name: "",
      episodes_seen: ""
    }
  }

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value
    })
  }

  handleSubmit = (e) => {
    e.preventDefault()
    this.setState(state => ({
      shows: state.shows.concat({
        name: this.state.name,
        episodes_seen: parseInt(this.state.episodes_seen)
      }),
      name: "",
      episodes_seen: ""
    }))
  }

  render() {
    return (
      <div className="App">
        <Instructions complete={true}/>
        {this.state.shows.map(x => (
          <Show id={x.id} name={x.name} episodes_seen={x.episodes_seen} />
        ))}
        <div>
          <form onSubmit={this.handleSubmit}>
            <input type="text" name="name" value={this.state.name} onChange={this.handleChange}/>
            <input type="text" name="episodes_seen" value={this.state.episodes_seen} onChange={this.handleChange}/>
            <button type="submit">Add Show</button>
          </form>
        </div>
      </div>
    )
  }
}

export default App
