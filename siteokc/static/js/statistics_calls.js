function ExportToExcel(type, fn, dl) {
       var elt = document.getElementById('tbl_exporttable_to_xls');
       var wb = XLSX.utils.table_to_book(elt, { sheet: "sheet1" });
       return dl ?
         XLSX.write(wb, { bookType: type, bookSST: true, type: 'base64' }):
         XLSX.writeFile(wb, fn || ('document.' + (type || 'xlsx')));
    }


function ExportToExcel1(type, fn, dl) {
       var elt = document.getElementById('tbl_exporttable_to_xls1');
       var wb = XLSX.utils.table_to_book(elt, { sheet: "sheet1" });
       return dl ?
         XLSX.write(wb, { bookType: type, bookSST: true, type: 'base64' }):
         XLSX.writeFile(wb, fn || ('document.' + (type || 'xlsx')));
    }


var modal = document.getElementById('id01');
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        }
    }


function exportHTML(){
    var header = "<html xmlns:o='urn:schemas-microsoft-com:office:office' "+
                 "xmlns:w='urn:schemas-microsoft-com:office:word' "+
                 "xmlns='http://www.w3.org/TR/REC-html40'>"+
                 "<head><meta charset='utf-8'><title>Export HTML to Word Document with JavaScript</title></head><body>";
    var footer = "</body></html>";
    var sourceHTML = header+document.getElementById("export_doc").innerHTML+footer;

    var source = 'data:application/vnd.ms-word;charset=utf-8,' + encodeURIComponent(sourceHTML);
    var fileDownload = document.createElement("a");
        document.body.appendChild(fileDownload);
        fileDownload.href = source;
        fileDownload.download = 'document.doc';
        fileDownload.click();
        document.body.removeChild(fileDownload);
    }

function exportHTML1(){
    var header = "<html xmlns:o='urn:schemas-microsoft-com:office:office' "+
                 "xmlns:w='urn:schemas-microsoft-com:office:word' "+
                 "xmlns='http://www.w3.org/TR/REC-html40'>"+
                 "<head><meta charset='utf-8'><title>Export HTML to Word Document with JavaScript</title></head><body>";
    var footer = "</body></html>";
    var sourceHTML = header+document.getElementById("export_doc1").innerHTML+footer;

    var source = 'data:application/vnd.ms-word;charset=utf-8,' + encodeURIComponent(sourceHTML);
    var fileDownload = document.createElement("a");
        document.body.appendChild(fileDownload);
        fileDownload.href = source;
        fileDownload.download = 'document.doc';
        fileDownload.click();
        document.body.removeChild(fileDownload);
    }
