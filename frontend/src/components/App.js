import React, { Component } from "react";
import { render } from "react-dom";
import { Button } from "bootstrap";
// import { Button } from 'reactstrap';

export default class App extends Component {
    constructor(props) {
      super(props);
    }

    render() {
      return <Button className="btn btn-info">A button</Button>
    }
  }

  const appDiv = document.getElementById("app");
  render(<App />, appDiv);