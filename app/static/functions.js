$("#search-btn").click(function () {
	var specInput = $("#spec").val();
	var locInput = $("#loc").val();
	var city = "";
	var index = 1;
	function f(doc) {
		console.log("Hello",doc);
		$("#search-box").animate({marginTop: "0px"}, 400, "linear", function () {
			$("#doctor-list-wrapper").text("");
			makeDoctorCards(doc);
		});
		$("#pagination-wrapper").show();
	}
	getDoctorData(specInput,locInput,city,index, f);
});

$("#page-list li").on("click", function (){
	var pageId = $(this).attr("id");
	var index = $(this).text();
	var specInput = $("#spec").val();
	var locInput = $("#loc").val();
	var city = "";
	var docList = getDoctorData(specInput,locInput,city,index);
	
	$(".doctorCard").slideUp(500)
	$("#doctor-list-wrapper").text("");
	makeDoctorCards(docList);
});

function makeDoctorCards(docList) {
	var len = docList.length;
	var limit = 10;
	if(len < 10)
		limit = len;
	if(len==0)
	{
		$("<p>").text("No results to display").appendTo("#doctor-list-wrapper");
	}
	else {

		for(var i=0;i<limit;i++) {
			var txt = "<h2>" + docList[i]["name"] + "</h2><p>" + docList[i]["education"] + "</p><p>Experience: " + docList[i]["experience"] + "</p>";
			var newRow = $("<div>").addClass("row").appendTo("#doctor-list-wrapper");
			var newCard = $("<div>").addClass("col-sm-8").addClass("doctorCard").addClass("col-sm-offset-2");
			$("<div>").addClass("sideCard").appendTo(newCard).append("<p>Specialization: " + docList[i]["specialization"] + "<br>In: " + docList[i]["area"] + "<br>Fee: " + docList[i]["fee"] + "</p>");
			newCard.appendTo(newRow).slideDown(1000).append(txt);	
		}
	}
}

$("#spec").on("input",function() {
	$("#spec").autocomplete ({
	source: getSpecialityList()
	});	
});

 $("#loc").on("input", function() {
 	$("#loc").autocomplete({
 		source: getLocationList("bangalore")
 	});
 });

function getLocationList(city){
	var cityList = [];
	$.get("get/bangalore", function(data){
		var List = data.results;
		for (var i = 0;i < List.length;i++){
			cityList.push(List[i].area);
		}
		console.log(cityList);
	});
	return cityList;
}
function getDoctorData(speciality, location, city, index, func_proc) {

	var docList = [];
	var Data;
	$.get("bangalore/jp nagar/surgeon/1", function(data){
		var docList = data.results;
		console.log(docList);
		func_proc(docList);
	});
	// //var docList = [
	// 	{
	// 		"name": "Dr Tony Stark",
	// 		"experience": "5 Years",
	// 		"specialization": "Cardiologist",
	// 		"rate": "INR 500",
	// 		"education": "M.B.B.S, M.D",
	// 		"imgsrc": "/img/1.png",
	// 		"area": "JP Nagar",
 //        	"completeaddress": "This is the complete address of the clinic"
	// 	}
}

function getSpecialityList() {
	return ["Dentist", "Dermatologist", "Pediatrician", "Homeopath", "Cardiologist"];
}