var num = 0;
var num2 = 0;

function ClickIndex(id) {
    num = id;
    document.getElementsByTagName("form")[1].action = "del/" + num + "/";
    document.getElementById("myForm").style.display = "block";

}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}

function ClickIndexEdit(id) {
    num2 = id;
    document.getElementsByTagName("form")[2].action = "edit/" + num2 + "/";
    document.getElementById("myForm2").style.display = "block";


}

function closeForm2() {
  document.getElementById("myForm2").style.display = "none";
}


var modal = document.getElementById('id01');
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function ExportToExcel(type, fn, dl) {
       var elt = document.getElementById('export_excel');
       var wb = XLSX.utils.table_to_book(elt, { sheet: "sheet1" });
       return dl ?
         XLSX.write(wb, { bookType: type, bookSST: true, type: 'base64' }):
         XLSX.writeFile(wb, fn || ('document.' + (type || 'xlsx')));
    }