let display = document.getElementById("res");

function isOperator() {
    if (display.innerHTML.endsWith('+') || display.innerHTML.endsWith('-') || display.innerHTML.endsWith('*') || display.innerHTML.endsWith('/')) {
        return true;
    }
}

btn0.onclick = function() {
    display.innerHTML += '0';
}

btn1.onclick = function() {
    display.innerHTML += '1';
}

btnClr.onclick = function() {
    display.innerHTML = '';
}

btnEql.onclick = function() {
    if (isOperator()) {
        alert("Invalid inputs.");
    } else {
        let reNumbers = /\d+/g;
        let reOperators = /[\+\-\*\/]+/g;
        let numbers = display.innerHTML.match(reNumbers);
        let operators = display.innerHTML.match(reOperators);
        
        while (operators.length > 0) {
            if (operators.includes('*')) {
                let index = operators.indexOf('*');
                let res = (index != 0 ? parseInt(numbers[index-1], 2) : parseInt(numbers[index], 2)) * parseInt(numbers[index+1], 2);
                numbers.splice(index, 2);
                numbers.splice(index, 0, res.toString(2));
                operators.splice(index, 1);
            } else if (operators.includes('/')) {
                let index = operators.indexOf('/');
                let res = (index != 0 ? parseInt(numbers[index-1], 2) : parseInt(numbers[index], 2)) / parseInt(numbers[index+1], 2);
                numbers.splice(index, 2);
                numbers.splice(index, 0, res.toString(2));
                operators.splice(index, 1);
            } else if (operators.includes('+')) {
                let index = operators.indexOf('+');
                let res = (index != 0 ? parseInt(numbers[index-1], 2) : parseInt(numbers[index], 2)) + parseInt(numbers[index+1], 2);
                numbers.splice(index, 2);
                numbers.splice(index, 0, res.toString(2));
                operators.splice(index, 1);
            } else {
                let index = operators.indexOf('-');
                let res = (index != 0 ? parseInt(numbers[index-1], 2) : parseInt(numbers[index], 2) ) - parseInt(numbers[index+1], 2);
                numbers.splice(index, 2);
                numbers.splice(index, 0, res.toString(2));
                operators.splice(index, 1);
            }
            display.innerHTML = numbers[0].toString(2);
        }
    }
}

btnSum.onclick = function() {
    if (display.innerHTML.length != 0 && !isOperator()) {
        display.innerHTML += '+';
    }
}

btnSub.onclick = function() {
    if (display.innerHTML.length != 0 && !isOperator()) {
        display.innerHTML += '-';
    }
}

btnMul.onclick = function() {
    if (display.innerHTML.length != 0 && !isOperator()) {
        display.innerHTML += '*';
    }
}

btnDiv.onclick = function() {
    if (display.innerHTML.length != 0 && !isOperator()) {
        display.innerHTML += '/';
    }
}

