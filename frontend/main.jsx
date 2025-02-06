import React from 'react';
import ReactDOM from 'react-dom/client';
import App from '../frontend/src/components/App'; // Make sure this is your main App component

const root = ReactDOM.createRoot(document.getElementById('app'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

