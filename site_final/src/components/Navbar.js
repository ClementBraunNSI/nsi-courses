import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import '../styles/Navbar.css';

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const location = useLocation();

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const isActive = (path) => {
    return location.pathname === path || location.pathname.startsWith(path + '/');
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-brand">
          <img src="/test.png" alt="NSI Logo" className="navbar-logo" />
        </Link>
        
        <div className={`navbar-menu ${isMenuOpen ? 'active' : ''}`}>
          <Link 
            to="/seconde" 
            className={`navbar-item ${isActive('/seconde') ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            <img src="/fox_seconde.png" alt="Seconde" className="level-icon" />
            <span>Seconde SNT</span>
          </Link>
          
          <Link 
            to="/premiere" 
            className={`navbar-item ${isActive('/premiere') ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            <img src="/fox_premiere.png" alt="Première" className="level-icon" />
            <span>Première NSI</span>
          </Link>
          
          <Link 
            to="/terminale" 
            className={`navbar-item ${isActive('/terminale') ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            <img src="/fox_terminale.png" alt="Terminale" className="level-icon" />
            <span>Terminale NSI</span>
          </Link>
        </div>
        
        <button 
          className={`navbar-toggle ${isMenuOpen ? 'active' : ''}`}
          onClick={toggleMenu}
          aria-label="Toggle menu"
        >
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </nav>
  );
};

export default Navbar;