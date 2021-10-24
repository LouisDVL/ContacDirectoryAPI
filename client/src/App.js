import logo from "./logo.svg";
import Nav from "./components/Nav";
import "./App.css";
import { Switch, Route } from "react-router-dom";
import UsersTable from "./components/UsersTable";

function App() {
  return (
    <div>
      <Nav />
      <div className="App">
        <h1>
          Hello welcome to my first python django react Full stack applications
          <Switch>
            <Route exact path="/" component={UsersTable} />
          </Switch>
        </h1>
      </div>
    </div>
  );
}

export default App;
