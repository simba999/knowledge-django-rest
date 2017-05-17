import React from 'react';

import Search from '../Search';
import UserPreview from '../UserPreview';


class Header extends React.PureComponent {
  render() {
    return (
      <div className="header">
        <div className="header__search">
          <Search />
        </div>
        <div className="header__user">
          <UserPreview />
        </div>
      </div>
    )
  }
}

export default Header;
