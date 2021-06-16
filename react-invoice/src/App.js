import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Link } from "react-router-dom";
import Header from "./components/Header";
import Customers from "./components/Customers";
import AddInvoice from "./components/AddInvoice";

function App() {
  const addInvoice = async (invoice) => {
    console.log(invoice);
    // const res = await fetch('http://localhost:5000/tasks', {
    //   method: 'POST',
    //   headers: {
    //     'Content-type': 'application/json',
    //   },
    //   body: JSON.stringify(invoice),
    // })

    
    // const data = await res.json()

    // setTasks([...tasks, data])

    // const id = Math.floor(Math.random() * 10000) + 1
    // const newTask = { id, ...task }
    // setTasks([...tasks, newTask])
  };

  return (
    <Router>
      <div className="container">
        <Header />
        <Route
          path="/"
          exact
          render={(props) => (
            <>
              <h2>Skapa Faktura</h2>
              <AddInvoice onAdd={addInvoice} />
              <Link to="/customers">Kundregister</Link>
            </>
          )}
        />

        <Route path="/customers" component={Customers} />
      </div>
    </Router>
  );
}

export default App;
