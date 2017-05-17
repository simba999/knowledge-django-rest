import React from 'react';
import { Link } from "react-router-dom";

import Contacts from '../Contacts';


class Sidebar extends React.PureComponent {
  render() {
    return (
      <div className="sidebar">
        <div className="sidebar__header">
          <Link to={'/'}>
            <img src="/images/logo.png" className="sidebar-logo" />
          </Link>
        </div>
        <div className="sidebar__body">
          <div className="sidebar__item">
            <Link to={'/solution-library'} className="sidebar-item sidebar-item--library">
              <div className="sidebar-item__text">
                Solution Library
              </div>
            </Link>
          </div>
          <div className="sidebar__item">
            <Link to={'/my-dashboard'} className="sidebar-item sidebar-item--dashboard">
              <div className="sidebar-item__text">
                My Dashboard
              </div>
            </Link>
          </div>
          <div className="sidebar__item">
            <Link to={'/my-solutions'} className="sidebar-item sidebar-item--solutions">
              <div className="sidebar-item__text">
                My Solutions
              </div>
            </Link>
          </div>
          <div className="sidebar__item">
            <Link to={'/settings'} className="sidebar-item sidebar-item--settings">
              <div className="sidebar-item__text">
                Settings
              </div>
            </Link>
          </div>
        </div>
        <div className="sidebar__footer">
          <div className="sidebar__contacts">
            <Contacts />
          </div>
        </div>
      </div>
    )
  }
}

export default Sidebar;
