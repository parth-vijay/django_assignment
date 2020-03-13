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
	$('.table-responsive table tbody tr input').click(function(){
		if(this.checked){
			$('.selectallbtn').show();
		}
		else{
			$('.selectallbtn').hide();
		}
	});
	$('.table-responsive table thead tr th:nth-child(1) input').click(function(){
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
	$('#draganddropfm input').change(function(){
		$('#draganddropfm').submit();
	});
	$('.search-container form input').keyup(function(){
		var searchtext=$(this).val()
		console.log(searchtext)
		$('.table-responsive table tbody tr').hide()
		var tlen=$('.table-responsive table tbody tr:not(.notfound) td:contains("'+searchtext+'")').length
		console.log(tlen)
		if( tlen > 0 ){
			$('.table-responsive table tbody tr:not(.notfound) td:contains("'+searchtext+'")').each(function(){
				$(this).closest('tr').show();
			});
		}
		else{
			$('.notfound').show();
		}
	});
	$('.showbutton').click(function(){

	});

	$('.deleteselect').click(function(){
		// console.log('hello delete')
		var select_row=[];
		$('.table-responsive table tbody tr input:checked').each(function(){
			var data=$(this).val()
			console.log(data)
			select_row.push(data)
		});
		console.log(select_row)
		$.ajax({
			url: "/data/",
			type: "POST",
			data: {'id[]':select_row},
			success:function(e)
			{
				console.log(e)
			}
		})
	});
});
