function TradingCard(props) {
  return (
    <div className="card">
      <p> Name: {props.name} </p>
      <img src={props.imgUrl} alt="profile" />
      <p> Skill: {props.skill} </p>
    </div>
  );
}

function AddTradingCard(props) {
  const [name, setName] = React.useState('');
  const [skill, setSkill] = React.useState('');
  function addNewCard() {
    fetch('/add-card', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({name, skill}),
    }).then(response => {
      response.json().then(jsonResponse => {
        const {cardAdded} = jsonResponse; // same as cardAdded = jsonResponse.cardAdded
        const {cardId, name: cardName, skill: cardSkill} = cardAdded;
        props.addCard(cardId, cardName, cardSkill);
      });
    });
  }
  return (
    <React.Fragment>
      <h2>Add New Trading Card</h2>
      <label htmlFor="nameInput">
        Name
        <input
          value={name}
          onChange={event => setName(event.target.value)}
          id="nameInput"
          style={{marginLeft: '5px'}}
        />
      </label>
      <label htmlFor="skillInput" style={{marginLeft: '10px', marginRight: '5px'}}>
        Skill
        <input value={skill} onChange={event => setSkill(event.target.value)} id="skillInput" />
      </label>
      <button type="button" style={{marginLeft: '10px'}} onClick={addNewCard}>
        Add
      </button>
    </React.Fragment>
  );
}

function TradingCardContainer() {
  const [cards, setCards] = React.useState([]);

  function addCard(cardId, name, skill) {
    const imgUrl = 'static/img/placeholder.png';
    const newCard = {cardId, skill, name, imgUrl}; // equivalent to { cardId: cardId, skill: skill, name: name, imgUrl: imgUrl }
    const currentCards = [...cards]; // makes a copy of cards. similar to doing currentCards = cards[:] in Python
    // [...currentCards, newCard] is an array containing all elements in currentCards followed by newCard
    setCards([...currentCards, newCard]);
  }

  React.useEffect(() => {
    fetch('/cards.json')
      .then(response => response.json())
      .then(data => setCards(data.cards));
  }, []);

  const tradingCards = [];

  // the following line will print out the value of cards
  // pay attention to what it is initially and what it is when the component re-renders
  console.log(`cards: `, cards);

  for (const currentCard of cards) {
    tradingCards.push(
      <TradingCard
        key={currentCard.cardId}
        name={currentCard.name}
        skill={currentCard.skill}
        imgUrl={currentCard.imgUrl}
      />
    );
  }

  return (
    <React.Fragment>
      <AddTradingCard addCard={addCard} />
      <h2>Trading Cards</h2>
      <div className="grid">{tradingCards}</div>
    </React.Fragment>
  );
}

ReactDOM.render(<TradingCardContainer />, document.getElementById('container'));
