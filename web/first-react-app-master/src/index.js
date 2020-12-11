import React from 'react';
import ReactDOM from 'react-dom';
//import App from './components/FirstApp/FirstApp';
import App from './components/PhoneBook/App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
