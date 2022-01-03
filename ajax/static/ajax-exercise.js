'use strict';

// PART 1: SHOW A FORTUNE

function showFortune(evt) {
  // TODO: get the fortune and show it in the #fortune-text div
  evt.preventDefault();

  fetch('/fortune')
  .then(res => res.text())
  .then(data => {
    document.querySelector('#fortune-text').innerText = data;
  });
}

document.querySelector('#get-fortune-button').addEventListener('click', showFortune);

// PART 2: SHOW WEATHER

function showWeather(evt) {
  evt.preventDefault();

  const url = '/weather.json';
  const zipcode = document.querySelector('#zipcode-field').value;
  console.log(zipcode);
  const our_url = `/weather.json?zipcode=${zipcode}`;
  console.log(our_url);
  // TODO: request weather with that URL and show the forecast in #weather-info
  fetch( our_url)
  .then(res => res.json())
  .then(data => {
    document.querySelector('#weather-info').innerText = data.forecast;
    console.log(data);
  });
}

document.querySelector('#weather-form').addEventListener('submit', showWeather);

// PART 3: ORDER MELONS

function orderMelons(evt) {
  evt.preventDefault();

  // TODO: show the result message after your form
  // TODO: if the result code is ERROR, make it show up in red (see our CSS!)
  const form_inputs = {
    quantity: document.querySelector('#quantity-field').value,
    type: document.querySelector('#melontype-field').value,    
  };
  fetch('/order-melons.json', {
    method:'POST',
    body: JSON.stringify(form_inputs),
    headers: {
      'Content-Type': 'application/json',
    },
  })
  .then(res => res.json())
  .then (responseJson => {
    alert(responseJson.status);}
  )};
document.querySelector('#order-form').addEventListener('submit', orderMelons);
