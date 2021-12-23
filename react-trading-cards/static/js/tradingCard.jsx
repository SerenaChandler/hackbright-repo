'use strict';

const tradingCardData = [
  {
    name: 'Balloonicorn',
    skill: 'video games',
    imgUrl: '/static/img/balloonicorn.jpg',  
  },
  {
    name: "Float",
    skill: "baking pretzels",
    imgUrl: "/static/img/float.jpg",
  },
  {
    name:"Llambda",
    skill:"knitting scarves",
    imgUrl:"/static/img/llambda.jpg",
  },
  {
    name:"Merge",
    skill:"swimming",
    imgUrl:"/static/img/merge.png"
  },
  {
    name: "Off-By-One",
    skill: "climbing mountains",
    imgUrl: "/static/img/off-by-one.jpeg",
  },
];


function TradingCard(props) {
  return (
    <div className="card">
      <h2>Name: {props.name}</h2>
      <img src={props.imgUrl} alt="profile" />
      <h2>Skill: {props.skill}</h2>
    
    </div>
  );
}


function TradingCardContainer(){
  const paragraphs = [];

  for (const currentCard of tradingCardData){
    paragraphs.push(<TradingCard name={currentCard.name} skill={currentCard.skill} imgUrl={currentCard.imgUrl} />);
  }

  return (
    <React.Fragment>
      {paragraphs}
    </React.Fragment>
  ); 
}

ReactDOM.render(<TradingCardContainer />, document.querySelector("#all-cards"));

// ReactDOM.render(
//   <TradingCard name="Balloonicorn" skill="video games" imgUrl="/static/img/balloonicorn.jpg" />,
//   document.querySelector('#balloonicorn')
// );

