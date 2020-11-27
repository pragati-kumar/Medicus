// import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import { CardList} from './components/card-list/card-list.component';


class App extends Component{

  constructor(){
    super();

    this.state= {
      results: [ ],
      uploadStatus: 'Upload your file'
    };
  }

  componentDidMount(){
    // fetch('https://DUMMY/getResults')
    // .then(response =>response.json())
    // .then(getResults => this.setState({results: getResults}));
  }

  render(){
    return (
      <div className="App">
      
      <div>
       {/*beautify this section and populate it with info of the website*/}
      <p>Home Page</p>
      </div>

      <CardList name= "Chest">
      <h1>Chest</h1>
      
      <button className="upload-button" type= "submit" onClick= {() => this.setState({uploadStatus: "Successfully uploaded!" })}>{ this.state.uploadStatus}</button>
      <p>Diagnosis-</p>
      {this.state.results}
      {
        this.state.results.map(patient => (
          <h1 key= {patient.id}>{ patient.name }</h1>
          
        ))
      }
      </CardList>
      </div>
      
    );
  }
  
}

export default App;
