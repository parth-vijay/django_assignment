$(document).ready(function(){
	$('.active').show();
	if($('.active')){
		$('.changeicon').removeClass('fa-plus').addClass('fa-minus')
	}
	else{
		$('.changeicon').addClass('fa-plus').removeClass('fa-minus')
	}
	$('.productmenulist h4 i').click(function(){
		// $(this).toggleClass("fa-minus");
		$('.productmenulist ul:nth-child(1)').toggle();
		
		// $(this).toggleClass("fa fa-minus");
		var ele = $('.changeicon');
  		if(ele.hasClass('fa-plus')){
			ele.removeClass('fa-plus').addClass('fa-minus')
  		}
		else{
			ele.addClass('fa-plus').removeClass('fa-minus')
		}
	});
	$('.areakeyupload button:nth-child(1)').click(function(){
		$('.dragndrop .item form').show();

	});
	$('.table-responsive table tbody tr:nth-child(1) th input').click(function(){
		console.log('hello');
		$('.selectallbtn').toggle();
	});
	$('.table-responsive table thead tr th:nth-child(1) input').click(function(){
		console.log('hi');
		if(this.checked){
			$('.table-responsive table tbody tr th input').prop('checked', true)
		}
		else{
			$('.table-responsive table tbody tr th input').prop('checked', false)
		}
	});


	// $('.draganddrop input').click(function(e){
	// 	var form=$(this)
	// 	console.log(form)
	// 	console.log('kam kr raha ha fn')
	// 	// e.preventDefault()
	// 	// e.stopPropagation();
	// 	$('.draganddrop input:nth-child(2)').submit()
	// })
	// 
});
function formsubmit(){
	console.log('hello')
	// .preventDefault()
	$('.dragndrop form').submit();
}