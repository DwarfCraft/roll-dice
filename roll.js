console.log("Hello");
RollDice(2, 6);
RollDiceV2("2d6");

function RollDice(num, dice){
	console.log("Num: " + num);
	console.log("Dice:" + dice);
	for (var i = 0; i < num; i++) {
		console.log(Math.floor(Math.random() * dice) + 1);
	}
}
function RollDiceV2(dice){
	console.log("Dice:" + dice);
	diceArray = dice.split(new RegExp("[dD]"));
	console.log(diceArray);
	for (var i = 0; i < diceArray[0]; i++) {
		console.log(Math.floor(Math.random() * diceArray[1]) + 1);
	}
}
