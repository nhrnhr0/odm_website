function addToFave(button){

    if(button.isChecked == undefined) {
        
        button.classList.add('unchecked');
        button.isChecked = false;
    }

    if(button.isChecked == false) {
        button.isChecked  = true;
        button.classList.replace('unchecked', 'checked');
    }
    else { 
        button.isChecked = false;
        button.classList.replace('checked', 'unchecked');

    }
    button.blur();
};