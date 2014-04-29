
function get_page(page) {
	$.getJSON(
		'pages.php?page='+page,
		function(data){
			if (data.container != undefined) {
				data = Base64.decode(data.container).split('\n')
				$.map(data, function( val, i ) {
					data[i] = val.split('').reverse().join('');
				});
				$("#container").html(data.join('\n'))
			}
		}
	);
}

$(document).ready(
    function(){
    	get_page('home')
		$(".navbar li a").click(function() {
			get_page($(this).text())
			$(".navbar li").removeClass('active')
			$(this).parent('li').addClass('active')
		});
    }
);