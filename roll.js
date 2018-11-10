console.log("Hello");
RollDice(2, 6);
function RollDice(num, dice){
	console.log("Num: " + num);
	console.log("Dice:" + dice);
	for (var i = 0; i < num; i++) {
		console.log(Math.floor(Math.random() * dice) + 1);
	}
}
