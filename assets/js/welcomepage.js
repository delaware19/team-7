var add = new Map([
    ["2500 Maryland Road, Suite 510 Willow Grove, PA 19090", "Nemours duPont Pediatrics, Willow Grove"],
    ["1200 Old York Road Abington, PA 19001","Nemours duPont Pediatrics at Abington Hospital - Jefferson Health"],
    ["1280 Almonesson Road Deptford, NJ 08096","Nemours duPont Pediatrics, Deptford"],
    ["Foulkstone Plaza 1405 Foulk Road, Suite 101 Wilmington, DE 19803","Nemours duPont Pediatrics, Foulk Road"],
    ["1600 Rockland Road Wilmington, DE 19803","Children's Hospital, Nemours/Alfred I. duPont Hospital for Children"]
]);

var search = document.getElementById("search");
search.addEventListener("keyup", function(event){
    if(event.keyCode === 13) {
        location.href = "http://127.0.0.1:5500/AppoinmentTypePage.html"
    }
});