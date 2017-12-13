/*window.onload = function(){
  $('#upload-btn').prop('disabled',true);
};

$('.upload-file').on("change",function(){
  $('#upload-btn').prop('disabled',false);
};

*/



window.onload = function() {
    document.getElementById("upload-btn").disabled = true;
}
function selectFile() {
  if (document.getElementById("upload-file").value === "") {
    document.getElementById("upload-btn").disabled = true;
  }
  else {
    document.getElementById("upload-btn").disabled = false;
  }
}

