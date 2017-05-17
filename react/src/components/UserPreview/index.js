import React from 'react';
import { Link } from "react-router-dom";


class UserPreview extends React.PureComponent {
  render() {
    return (
      <div className="user-preview">
        <div className="user-preview__link">
          <Link to={'/settings'} />
        </div>
        <div className="user-preview__avatar">
          <img src="/images/fish/user-avatar--small.png" />
        </div>
        <div className="user-preview__name">
          O. Crawford
        </div>
      </div>
    )
  }
}

export default UserPreview;
