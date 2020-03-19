$(document).ready(function(){
	$('.orderuploadbtn').show()
	$('.orderhistory').hide()
	var allpanel=$('.productmenulist > ul').hide()
	$('.productmenulist > h4 > i').click(function(){
		$('.productmenulist > ul').slideUp();
		$(this).parent().next().slideDown();
	});

	$('.orderuploadbtn table tbody tr input[type="checkbox"]').click(function(){
		var inval= $('.areakeycheckbox:checked').length
		if(inval>0){
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
		// e.preventDefault()
		var le=$(this).length
		console.log(le)
		$('.orderhistory').show()
		if(le > 0){
			$('.orderuploadbtn').hide()
		}
	});
	$('.areakeyupload button:nth-child(1)').click(function(e){
		var le=$(this).length
		$('.orderuploadbtn').show()
		if(le > 0){
			$('.orderhistory').hide()
		}

	}); 
	$('#draganddropfm input').change(function(){
		$('#draganddropfm').submit();
	});
	$('.search-container form input').keyup(function(){
		var searchtext=$(this).val()
		console.log(searchtext)
		$('.table-responsive table tbody tr').hide()
		var tlen=$('.table-responsive table tbody tr:not(.notfound) td:contains("'+searchtext+'")').length
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
		window.location.reload();
	});
	$('.showbutton').click(function(e){
		console.log('hello csv')
		var select_row=[];
		$('.table-responsive table tbody tr input:checked').each(function(){
			var data=$(this).val()
			select_row.push(data)
		});
		e.preventDefault()
		var form=$('<form action="/export/" method="POST"></form>').append('<input name="csv_file[]" value="'+select_row+'" />')
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
	$('.confirmationorder').click(function(){
		var select_order=[];
		$('.table-responsive table tbody tr input:checked').each(function(){
			var or_data=$(this).val()
			select_order.push(or_data)
		});
		$.ajax({
			url: "/order/",
			type: "POST",
			data: {'order[]':select_order},
			success:function(e)
			{
				console.log(e)
			}
		})
		window.location.reload();
	});
});
