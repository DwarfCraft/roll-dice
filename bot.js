var Discord = require('discord.io');
var logger = require('winston');
var auth = require('./auth.json');
// Configure logger settings
logger.remove(logger.transports.Console);
logger.add(new logger.transports.Console, {
    colorize: true
});
logger.level = 'debug';
// Initialize Discord Bot
var bot = new Discord.Client({
   token: auth.token,
   autorun: true
});
bot.on('ready', function (evt) {
    logger.info('Connected');
    logger.info('Logged in as: ');
    logger.info(bot.username + ' - (' + bot.id + ')');
});
bot.on('message', function (user, userID, channelID, message, evt) {
    // Our bot needs to know if it will execute a command
    // It will listen for messages that will start with `!`
    if (message.substring(0, 1) == '!') {
        var args = message.substring(1).split(' ');
        var cmd = args[0];
       
        args = args.splice(1);
		if (Number.isInteger(cmd)) {
	    	bot.sendMessage({
				to: channelID,
				message: Math.floor(Math.random() * cmd) + 1
			});
		}
		else {
			
		}
        switch(cmd) {
            // !ping
            case 'ping':
                bot.sendMessage({
                    to: channelID,
                    message: 'Pong!'
                });
            break;
            case 'roll':
                bot.sendMessage({
                    to: channelID, 
                    message: Math.floor(Math.random() * 20) + 1
                });
            break;
            case '4':
                bot.sendMessage({
                    to: channelID, 
                    message: Math.floor(Math.random() * 4) + 1
                });
            break;
            case '6':
                bot.sendMessage({
                    to: channelID, 
                    message: Math.floor(Math.random() * 6) + 1
                });
            break;
            case '8':
                bot.sendMessage({
                    to: channelID, 
                    message: Math.floor(Math.random() * 8) + 1
                });
            break;
            case '10':
                bot.sendMessage({
                    to: channelID, 
                    message: Math.floor(Math.random() * 10) + 1
                });
            break;
            case '12':
                bot.sendMessage({
                    to: channelID, 
                    message: Math.floor(Math.random() * 12) + 1
                });
            break;
            case '20':
                bot.sendMessage({
                    to: channelID, 
                    message: Math.floor(Math.random() * 20) + 1
                });
            break;
            case '100':
                bot.sendMessage({
                    to: channelID, 
                    message: Math.floor(Math.random() * 100) + 1
                });
            break;
	    default:
		bot.sendMessage({
		    to: channelID,
		    message: Math.floor(Math.random() * cmd) + 1
		});
	    break;
            // Just add any case commands if you want to..
         }
     }
});
