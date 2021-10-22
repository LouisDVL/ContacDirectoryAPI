import React, { useState } from "react";

function Nav() {
  const [toggle, setToggle] = useState(false);

  function navToggle(e) {
    e.preventDefault();
    setToggle(!toggle);
  }

  function setNavClass() {
    if (toggle) {
      return "navbar responsive";
    } else {
      return "navbar";
    }
  }

  const navClass = setNavClass();

  return (
    <div className={navClass} id="navbar">
      <a href="#" className="brand">
        <h1>Home</h1>
      </a>
      <a href="#" className="navlink">
        Users
      </a>
      <a href="#" className="navlink">
        Emails
      </a>
      <a href="#" className="navlink">
        Phone Numbers
      </a>
      <a className="icon" id="icon" onClick={navToggle}>
        <h1>
          <i className="fa fa-bars"></i>
        </h1>
      </a>
    </div>
  );
}

export default Nav;
