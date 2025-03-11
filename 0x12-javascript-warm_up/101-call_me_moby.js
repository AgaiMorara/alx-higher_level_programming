#!/usr/bin/node

// a function that executes X times a function. ( visible from outside)

exports.callMeMoby = function(X, theFunction){	
		while (X > 0){
			theFunction();
			X--;
		}
	};
