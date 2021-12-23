'use strict';

function Homepage() {
  
  return (
  <div>
  <a href = '/cards'>Click here to see your card</a>
  <img src = '/static/img/balloonicorn.jpg'/>
  </div>
  )}

ReactDOM.render(<Homepage />, document.querySelector('#app'));
