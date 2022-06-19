

 
//searchMediaTbody() keyup event listener called from body tag onload=
function getSearchEvent() {
    if (document.getElementById('entrySearchInput')) {
        document.getElementById('entrySearchInput').addEventListener('keyup', searchEntryTbody, false);
    };        
    if (document.getElementById('mediaSearchInput')) {
        document.getElementById('mediaSearchInput').addEventListener('keyup', searchMediaTbody, false);  
    };
    // if (document.getElementById('mediaTitleSearchInput')) {
    //     document.getElementById('mediaTitleSearchInput').addEventListener('keyup', searchTitleMediaTbody, false);  
    // };
    if (document.getElementById('btn-UserEntryTable')) {
        document.getElementById('btn-UserEntryTable').addEventListener('click', myCollapse, false);
    }
    if (document.getElementById('btn-StatusEntryTable')) {
        document.getElementById('btn-StatusEntryTable').addEventListener('click', myCollapse, false);
    }
    if (document.getElementById('btn-TypeEntryTable')) {
        document.getElementById('btn-TypeEntryTable').addEventListener('click', myCollapse, false);
    }
    if (document.getElementById('btn-RatingEntryTable')) {
        document.getElementById('btn-RatingEntryTable').addEventListener('click', myCollapse, false);
    }
    if (document.getElementById('btn-TypeMediaTable')) {
        document.getElementById('btn-TypeMediaTable').addEventListener('click', myCollapse, false);
    }
    if (document.getElementById('btn-RatingMediaTable')) {
        document.getElementById('btn-RatingMediaTable').addEventListener('click', myCollapse, false);
    }
}

//---------------------------------------------------------------------------------------------

//called from keyup event to search text in title, author, and actors columns of entry table

function searchMediaTbody(event) {
    
    var rows = document.querySelector("#mediaTbody").rows;
    var filteredRows = rows.length
    if (event=="clearAll"){
        var filter = ""
        document.getElementById('mediaSearchInput').value = filter 
        document.getElementById('mediaSearchInput').value.refresh
    }
    
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
    if (event=="clearAll"){
        for (let i = 0; i < checkBoxRowsType.length; i++){
            let x = checkBoxRowsType[i] 
            x.checked = false
        }
    }else{
        for (let i = 0; i < checkBoxRowsType.length; i++){
            let x = checkBoxRowsType[i].id 
            typeChecked.push(x);
        }
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
    if (event=="clearAll"){
        for (let i = 0; i < checkBoxRowsRating.length; i++){
            let rating = checkBoxRowsRating[i] 
            rating.checked = false
        }    
    }else{
        for (let i = 0; i < checkBoxRowsRating.length; i++){
            let rating = checkBoxRowsRating[i].id 
            ratingChecked.push(rating);
        }
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
        var filteredCount = document.getElementById('filteredCount').innerHTML     
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
        if (rows[i].style.display == 'none'){
            filteredRows -= 1
        }

    } 
    document.getElementById('filteredCount').innerHTML = filteredRows
             
}   

//-------------------------------------------------------------------------------

//called from keyup event to search text in title column of media table for selecting
//a media for a new entry

function searchTitleMediaTbody(event) {

    var rows = document.querySelector("#mediaEntryTbody").rows;
    if (event=="clearAll"){
        var filter = ""
        document.getElementById('mediaTitleSearchInput').value = filter 
        document.getElementById('mediaTitleSearchInput').value.refresh
    }
    
    if (event!="ckBox"){
        var mediaSearch = document.getElementById('mediaTitleSearchInput')
        if (mediaSearch.value != "") {
            if (event.target.value == mediaSearch.value){
                var filter = mediaSearch.value.toUpperCase();
            }
        }else{
            var filter = mediaSearch.value.toUpperCase();
        }
    }else{
        var filter = document.getElementById('mediaTitleSearchInput').value.toUpperCase(); 
    }

    //typeFilterTest
    var typeChecked = [];
    var typeFilterTest = false
    var checkBoxRowsType = document.querySelectorAll(`input[name="typeFilter"]:checked`);
    if (event=="clearAll"){
        for (let i = 0; i < checkBoxRowsType.length; i++){
            let x = checkBoxRowsType[i] 
            x.checked = false
        }
    }else{
        for (let i = 0; i < checkBoxRowsType.length; i++){
            let x = checkBoxRowsType[i].id 
            typeChecked.push(x);
        }
    }
    if (typeChecked < 1) {
        checkBoxRowsType = document.querySelectorAll(`input[name="typeFilter"]`)
        for (let i = 0; i < checkBoxRowsType.length; i++){
            let x = checkBoxRowsType[i].id 
            typeChecked.push(x);
        }
    }


    for (var i = 0; i < rows.length; i++) {
        var firstCol = rows[i].cells[1].textContent.toUpperCase();
        var typeInRow = rows[i].cells[5].textContent;
        var typeFilterTest = typeChecked.includes(typeInRow);

        if (firstCol.indexOf(filter) > -1 ) {
            if (typeFilterTest ){
                rows[i].style.display = "";  
            }else{
                rows[i].style.display = "none";
            }
            
        } else {
            rows[i].style.display = "none";
        }
    }          
}   

//---------------------------------------------------------------------------------------------------------------

//called from keyup event to search text in title, author, and actors columns of media table
function searchEntryTbody(event) {
    if (document.querySelector("#entryTbody")){
        var rows = document.querySelector("#entryTbody").rows;
        var filteredRows = rows.length
    }
    if (event=="clearAll"){
        var filter = ""
        document.getElementById('entrySearchInput').value = filter 
        document.getElementById('entrySearchInput').value.refresh
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
    var userFilterTest = false;
    var checkBoxRowsUsers = document.querySelectorAll(`input[name="userFilter"]:checked`);
    
    if (event=="clearAll"){
        for (let i = 0; i < checkBoxRowsUsers.length; i++){
            let user = checkBoxRowsUsers[i] 
            user.checked = false
        }
    }else{
        for (let i = 0; i < checkBoxRowsUsers.length; i++){
            let user = checkBoxRowsUsers[i].id 
            userChecked.push(user.substring(5));
        }
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
    if (event=="clearAll"){
        for (let i = 0; i < checkBoxRowsStatus.length; i++){
            let x = checkBoxRowsStatus[i] 
            x.checked = false
        }
    }else{
        for (let i = 0; i < checkBoxRowsStatus.length; i++){
            let status = checkBoxRowsStatus[i].id 
            statusChecked.push(status);
        }
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
        if (event=="clearAll"){
            for (let i = 0; i < checkBoxRowsType.length; i++){
                let x = checkBoxRowsType[i] 
                x.checked = false
            }
        }else{
            for (let i = 0; i < checkBoxRowsType.length; i++){
                let x = checkBoxRowsType[i].id 
                typeChecked.push(x);
            }
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
     if (event=="clearAll"){
        for (let i = 0; i < checkBoxRowsRating.length; i++){
            let rating = checkBoxRowsRating[i] 
            rating.checked = false
        }    
    }else{
        for (let i = 0; i < checkBoxRowsRating.length; i++){
            let rating = checkBoxRowsRating[i].id 
            ratingChecked.push(rating);
        }
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
        var statusInRow = rows[i].cells[10].textContent;
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
        if (rows[i].style.display == 'none'){
            filteredRows -= 1
        }
    }
    document.getElementById('filteredCount').innerHTML = filteredRows          
}   



 //for implementing eventHandler for collapsing filters"
 
function myCollapse(event){
    var src = event.srcElement; 
    var content = src.nextElementSibling;
    if (content.style.display === "block") {
        content.style.display = "none";
    } else {
        content.style.display = "block";
 }
 }

