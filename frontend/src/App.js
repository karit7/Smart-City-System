import React, { Component } from 'react';
import axios from 'axios';

const list = [
  {
    "id":"1",
    "amount":"100.99",
    "payer":"1",
    "receiver":"2",
    "note":"Learn Django properly."
  },
  {
    "id":"2",
    "amount":"20",
    "payer":"2",
    "receiver":"3",
    "note":"Integer amount."
  },
  {
    "id":"3",
    "amount":"7.5",
    "payer":"2",
    "receiver":"1",
    "note":"Another transaction."
  }
]

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { 
      transactions: []
     };
  }

  componentDidMount(){
    this.getTransactions();
  }

  getTransactions(){
    axios.get('http://127.0.0.1:8000/api/v1/transactions/')
    .then( res => {
      this.setState({ transactions: res.data });
    })
    .catch(err => {
      console.log(err);
    });
  }
  render() {
    return (
      <div>
        <table>
          <tr>
            <th>Id</th>
            <th>Note</th>
            <th>Amount</th>
            <th>Receiver</th>
            <th>Payer</th>
          </tr>
        {this.state.transactions.map(item => (
          <tr>
            <th>{item.id}</th>
            <th>{item.note}</th>
            <th>{item.amount}</th>
            <th>{item.receiver}</th>
            <th>{item.payer}</th>
          </tr>
        ))}
        </table>
      </div>
    );
  }
}

export default App;      