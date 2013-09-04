var theme_list_open = false;
var colour_list_open = false;

jQuery(document).ready(function () {
	
	jQuery("#theme_dropdown a").each(function() {

		jQuery(this).poshytip({
			content: '<img src="' + jQuery(this).attr('title') + '" alt="preview image" />',
			className: 'tip-twitter',
			followCursor: true,
			slide: false,
			showTimeout: 1,
			fade: false,
			offsetX: 50,
			offsetY: 0
		});
	});

	function fixHeight () {
	
		var headerHeight = jQuery("#switcher").height();
				
		jQuery("#iframe").attr("height", ((jQuery(window).height()) - headerHeight) + 'px');
	
	}
	
	jQuery(window).resize(function () {
		
		fixHeight();
	
	}).resize();
	
	jQuery("#theme_select").click( function () {
	
		if (theme_list_open == true) {
	
			jQuery("#theme_list ul").hide();
			
			theme_list_open = false;
		
		} else {
		
			jQuery("#theme_list ul").show();         		
			
			theme_list_open = true;
		
		}
		
		return false;
	
	});
	
	jQuery("#colour_select").click( function () {
	
		if (colour_list_open == true) {
	
			jQuery("#colour_list ul").hide();
			
			colour_list_open = false;
		
		} else {
		
			jQuery("#colour_list ul").show();         		
			
			colour_list_open = true;
		
		}
		
		return false;
	
	});
	
	
	function showColours(elem, currentTheme) {
		
		if(elem.attr('data-colour')=='true') {	
			
			jQuery('#colour_list').fadeIn(200);
		} else {
			jQuery('#colour_list').fadeOut(200);
			jQuery('#colour_dropdown').html('');
		}
		
	}

	jQuery("#theme_list ul li a").click(function () {
		
	
		var theme_data = jQuery(this).attr("rel").split(",");
					
		jQuery("li.purchase a").attr("href", theme_data[1]);
		jQuery("li.remove_frame a").attr("href", theme_data[0]);
		jQuery("#iframe").attr("src", theme_data[0]);
		
		jQuery("#theme_select").html(jQuery(this).html());
		
		jQuery("#theme_select").find('span').remove();
		
		jQuery(".center ul li ul").hide();
		
		var currentTheme =  jQuery('#theme_select').text().toLowerCase();
		
		showColours(jQuery(this), currentTheme);
		
		isFreeTheme(jQuery(this));
		
		theme_list_open = false;
		colour_list_open = false;
		
		return false;
	
	});
	
	jQuery('#theme_dropdown li a').each( function() {
		
		var currentTheme =  jQuery('#theme_select').html();
		
		
		if(jQuery(this).html().split('<span')[0] == currentTheme) {
			showColours(jQuery(this), currentTheme.toLowerCase());
			
			isFreeTheme(jQuery(this));
			
		}
		
	});
	
	function isFreeTheme(theme) {
		
		if(theme.attr('data-type') == 'free') {
			jQuery('#purchaseLink').removeClass('purchase').addClass('download');
		} else {
			jQuery('#purchaseLink').addClass('purchase').removeClass('download');
		}
	}
	
	//console.log(currentTheme);

});