// public/js/script.js
window.onload = function() {
	arr = document.getElementsByClassName('delete');
	//arr.forEach(e => {
	for(let e of arr){
		e.onclick = function(){
			var select = confirm('정말로 삭제하시겠습니까?');			
			if(select){
				document.getElementById('frm' + e.id).submit();
			}
			return false;
		}	
	}	
};
