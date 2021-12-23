'use strict';

function Homepage() {
  
  return (
  <div>
  <a href = '/cards'>Click here to see your card</a>
  <img src = '/static/img/balloonicorn.jpg'/>
  <a href = '/about'>Click here to see about me</a>
  </div>
  )}

ReactDOM.render(<Homepage />, document.querySelector('#app'));
