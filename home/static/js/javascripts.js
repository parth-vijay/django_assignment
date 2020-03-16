$(document).ready(function(){
	$
	$('.orderuploadbtn').show()
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
	$('.table-responsive table tbody tr input[type="checkbox"]').click(function(){
		var inval=$(this);
		// console.log(inval)
		// $('.selectallbtn').show(this.checked)

		if(inval.filter('[type="checkbox"]').is(':checked')){
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
	$('.areakeyupload button:nth-child(2)').click(function(e){
	// 	var form=$(this)
		console.log('hello upload button')
		var le=$(this).length
		console.log(le)
		$('.orderhistory').show()
	});
	$('.areakeyupload button:nth-child(1)').click(function(e){
	// 	var form=$(this)
		// console.log('hello order button')
		var le=$(this).length
		// console.log(le)
		$('.orderuploadbtn').show()
	});

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
	$('.showbutton').click(function(e){
		console.log('hello csv')
		var select_row=[];
		$('.table-responsive table tbody tr input:checked').each(function(){
			var data=$(this).val()
			console.log(data)
			select_row.push(data)
		});
		console.log(select_row)
		e.preventDefault()
		var form=$('<form action="/export/" method="POST"></form>').append('<input name="csv_file[]" value="'+select_row+'" />')
		// console.log(form)
		// form.append()
		form.appendTo($('body')).submit()
		// $.ajax({
		// 	url: "/export/",
		// 	type: "POST",
		// 	data: {'csv_file[]':select_row},
		// 	success:function(e)
		// 	{
		// 		console.log(e)
		// 	}
		// })
	});
	// $('.showbutton').click(function(e){
	// 	$('.table-responsive table tbody tr input:checked').each(function(){
	// 		var da=$(this).val()
	// 		console.log(da)

	// 		var g=$('.areakeyinner form input').attr('value',da)
	// 		console.log(g)
	// 	});
	// })
	$('.confirmationorder').click(function(){
		// console.log('hello order')
		var select_order=[];
		$('.table-responsive table tbody tr input:checked').each(function(){
			var or_data=$(this).val()
			console.log(or_data)
			select_order.push(or_data)
		});
		console.log(select_order)
		$.ajax({
			url: "/order/",
			type: "POST",
			data: {'order[]':select_order},
			success:function(e)
			{
				console.log(e)
			}
		})
	})
});
