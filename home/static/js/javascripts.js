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
});