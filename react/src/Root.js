import React 						from 'react';
// import {Link} from "react-router-dom";
import Home 						from "./components/Home";
// import About from "./components/About";
// import Flag from "./containers/Flag";

import Sidebar 						from './components/Sidebar';
import Header 						from './components/Header';
import CustomSolutionComponent 		from './components/CustomSolutionComponent';
import SolutionComponent 			from './components/SolutionComponent';
import SolutionDetailComponent		from './components/SolutionDetailComponent';
import ResultDetailComponent		from './components/ResultDetailComponent';

import "./styles/root.scss";
import {Switch, Route} 				from "react-router";
import SolutionLibraryPage 			from "./containers/SolutionLibraryPage";
import MyDashboardPage 				from "./containers/MyDashboardPage";
import MySolutionsPage 				from "./containers/MySolutionsPage";
import SettingsPage 				from "./containers/SettingsPage";


export default class Root extends React.Component {
	render() {
		return (
		  <div className="page">
			  <div className="layout">
				  <div className="layout__aside">
					  <Sidebar />
				  </div>
				  <div className="layout__main">
					  <div className="layout__header">
						  <Header />
					  </div>
					  <div className="layout__content">
						  <Switch>
							  <Route exact path="/" component={Home}/>
							  <Route exact path="/solution-library" component={SolutionLibraryPage}/>
							  <Route exact path="/solution-library" component={SolutionComponent}/>

							  <Route path="/solution" component={SolutionComponent}/>
							  <Route path="/solution-detail" component={SolutionDetailComponent}/>
							  <Route path="/custom-solution" component={CustomSolutionComponent}/>
							  <Route path="/result-detail" component={ResultDetailComponent}/>
							  <Route path="/my-dashboard" component={MyDashboardPage}/>
							  <Route path="/my-solutions" component={MySolutionsPage}/>
							  <Route path="/settings" component={SettingsPage}/>
						  </Switch>
					  </div>
				  </div>
			  </div>
		  </div>
		);
	}
}

// {
// 	<div>
// 		<ul>
// 			<li>
// 				<Link to={'/'}>Home</Link>
// 			</li>
// 			<li>
// 				<Link to={'/about'}>About</Link>
// 			</li>
// 			<li>
// 				<Link to={'/flag'}>Flag</Link>
// 			</li>
// 		</ul>
// 		<Route exact path="/" component={Home}/>
// 		<Route path="/about" component={About}/>
// 		<Route path="/flag" component={Flag}/>
// 	</div>
// }