

 
//searchMediaTbody() keyup event listener called from body tag onload=
function getSearchEvent() {
    if (document.getElementById('entrySearchInput')) {
        document.getElementById('entrySearchInput').addEventListener('keyup', searchEntryTbody, false);
    };        
    if (document.getElementById('mediaSearchInput')) {
        document.getElementById('mediaSearchInput').addEventListener('keyup', searchMediaTbody, false);  
    };
}


function searchMediaTbody(event) {
    
    var rows = document.querySelector("#mediaTbody").rows;
    if (event!="ckBox"){
        var mediaSearch = document.getElementById('mediaSearchInput')
        if (mediaSearch.value != "") {
            if (event.target.value == mediaSearch.value){
                var filter = mediaSearch.value.toUpperCase();
            }
        }else{
            var filter = mediaSearch.value.toUpperCase();
        }
    }else{
        var filter = document.getElementById('mediaSearchInput').value.toUpperCase(); 
    }

    //typeFilterTest
    var typeChecked = [];
    var typeFilterTest = false
    var checkBoxRowsType = document.querySelectorAll(`input[name="typeFilter"]:checked`);
    for (let i = 0; i < checkBoxRowsType.length; i++){
        let x = checkBoxRowsType[i].id 
        typeChecked.push(x);
    }
    if (typeChecked < 1) {
        checkBoxRowsType = document.querySelectorAll(`input[name="typeFilter"]`)
        for (let i = 0; i < checkBoxRowsType.length; i++){
            let x = checkBoxRowsType[i].id 
            typeChecked.push(x);
        }
    }

    //ratingFilterTest
    var ratingChecked = [];
    var ratingFilterTest = false
    var checkBoxRowsRating = document.querySelectorAll(`input[name="ratingFilter"]:checked`);
    for (let i = 0; i < checkBoxRowsRating.length; i++){
        let rating = checkBoxRowsRating[i].id 
        ratingChecked.push(rating);
    }
    //selects all checkboxes 
    if (ratingChecked.length < 1) {
        checkBoxRowsRating = document.querySelectorAll(`input[name="ratingFilter"]`)
        for (let i = 0; i < checkBoxRowsRating.length; i++){
            let rating = checkBoxRowsRating[i].id 
            ratingChecked.push(rating);
        }
    } 

    for (var i = 0; i < rows.length; i++) {
        var firstCol = rows[i].cells[1].textContent.toUpperCase();
        var secondCol = rows[i].cells[2].textContent.toUpperCase();
        var thirdCol = rows[i].cells[3].textContent.toUpperCase();
        var typeInRow = rows[i].cells[5].textContent;
        var typeFilterTest = typeChecked.includes(typeInRow);
        var ratingInRow = rows[i].cells[9].textContent;
        var ratingFilterTest = ratingChecked.includes(ratingInRow);     

        if (firstCol.indexOf(filter) > -1 || secondCol.indexOf(filter) > -1
        || thirdCol.indexOf(filter) > -1) {
            if (typeFilterTest && ratingFilterTest){
                rows[i].style.display = "";   
            }else{
                rows[i].style.display = "none";
            }
        } else {
            rows[i].style.display = "none";
        }
    }          
}   

//called from keyup event to search text in title, author, and actors columns of media table
function searchEntryTbody(event) {
    if (document.querySelector("#entryTbody")){
        var rows = document.querySelector("#entryTbody").rows;
    }
    if (event!="ckBox"){
        if (document.getElementById('entrySearchInput').value != "") {
            if (event.target.value == document.getElementById('entrySearchInput').value){
                var filter = document.getElementById('entrySearchInput').value.toUpperCase();
            }
        }else{
            var filter = document.getElementById('entrySearchInput').value.toUpperCase();
        }
    }else{
        if (document.getElementById('entrySearchInput')){
            var filter = document.getElementById('entrySearchInput').value.toUpperCase(); 
        }
    }

    //userFilterTest
    var userChecked = [];
    var userFilterTest = false
    var checkBoxRowsUsers = document.querySelectorAll(`input[name="userFilter"]:checked`);
    for (let i = 0; i < checkBoxRowsUsers.length; i++){
        let user = checkBoxRowsUsers[i].id 
        userChecked.push(user.substring(5));
    }
    //selects all checkboxes 
    if (userChecked < 1) {
        checkBoxRowsUsers = document.querySelectorAll(`input[name="userFilter"]`)
        for (let i = 0; i < checkBoxRowsUsers.length; i++){
            let user = checkBoxRowsUsers[i].id
            userChecked.push(user.substring(5));
        }
    }

     //statusFilterTest
     var statusChecked = [];
     var statusFilterTest = false
     var checkBoxRowsStatus = document.querySelectorAll(`input[name="statusFilter"]:checked`);
     for (let i = 0; i < checkBoxRowsStatus.length; i++){
         let status = checkBoxRowsStatus[i].id 
         statusChecked.push(status);
     }
     //selects all checkboxes 
     if (statusChecked < 1) {
         checkBoxRowsStatus = document.querySelectorAll(`input[name="statusFilter"]`)
         for (let i = 0; i < checkBoxRowsStatus.length; i++){
             let status = checkBoxRowsStatus[i].id 
             statusChecked.push(status);
         }
     }

     //typeFilterTest
     var typeChecked = [];
     var typeFilterTest = false
     var checkBoxRowsType = document.querySelectorAll(`input[name="typeFilter"]:checked`);
     for (let i = 0; i < checkBoxRowsType.length; i++){
         let type = checkBoxRowsType[i].id 
         typeChecked.push(type);
     }
     //selects all checkboxes 
     if (typeChecked < 1) {
         checkBoxRowsType = document.querySelectorAll(`input[name="typeFilter"]`)
         for (let i = 0; i < checkBoxRowsType.length; i++){
             let type = checkBoxRowsType[i].id 
             typeChecked.push(type);
         }
     }

    //ratingFilterTest
    var ratingChecked = [];
    var ratingFilterTest = false
    var checkBoxRowsRating = document.querySelectorAll(`input[name="ratingFilter"]:checked`);
    for (let i = 0; i < checkBoxRowsRating.length; i++){
        let rating = checkBoxRowsRating[i].id
        ratingChecked.push(rating);
    }
    //selects all checkboxes 
    if (ratingChecked.length < 1) {
        checkBoxRowsRating = document.querySelectorAll(`input[name="ratingFilter"]`)
        for (let i = 0; i < checkBoxRowsRating.length; i++){
            let rating = checkBoxRowsRating[i].id 
            ratingChecked.push(rating);
        }
    } 
    
    for (var i = 0; i < rows.length; i++) {
        var firstCol = rows[i].cells[1].textContent.toUpperCase();
        var secondCol = rows[i].cells[2].textContent.toUpperCase();
        var thirdCol = rows[i].cells[3].textContent.toUpperCase();
        var userInRow = rows[i].cells[8].textContent;
        var userFilterTest = userChecked.includes(userInRow);
        var statusInRow = rows[i].cells[5].textContent;
        var statusFilterTest = statusChecked.includes(statusInRow);     
        var typeInRow = rows[i].cells[4].textContent;
        var typeFilterTest = typeChecked.includes(typeInRow);
        var ratingInRow = rows[i].cells[9].textContent;
        var ratingFilterTest = ratingChecked.includes(ratingInRow);            
        if (firstCol.indexOf(filter) > -1 || secondCol.indexOf(filter) > -1
        || thirdCol.indexOf(filter) > -1) {
            if (userFilterTest && typeFilterTest && statusFilterTest && ratingFilterTest){
                rows[i].style.display = "";   
            }else{
                rows[i].style.display = "none";
            }
        } else {
            rows[i].style.display = "none";
        }
    }          
}   




var vtitle='title'

function sortTableHeader(col) {
    if (col === 'title') {
        vtitle = '-title'
    }

}

