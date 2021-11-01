import logo from "./logo.svg";
import Nav from "./components/Nav";
import "./App.css";
import { Switch, Route } from "react-router-dom";
import UsersTable from "./components/UsersTable";
import PhoneNumberTable from "./components/PhoneNumberTable";
import EmailTable from "./components/EmailTable";

function App() {
  return (
    <div>
      <Nav />
      <div className="App">
        <h1>
          Hello welcome to my first python django react Full stack applications
          <Switch>
            <Route exact path="/" component={UsersTable} />
            <Route path="/phone" component={PhoneNumberTable} />
            <Route path="/email" component={EmailTable} />
          </Switch>
        </h1>
      </div>
    </div>
  );
}

export default App;
