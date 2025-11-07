<!--

author:   DART Team, David Croft
email:    dart@chop.edu, david.croft@warwick.ac.uk
version:  1.4.1
current_version_description: Add text after Overview and Feedback that invites learners to the rest of the modules
language: en
narrator: UK English Female
title: Module Macros
comment:  This is placeholder module to save macros used in other modules.

@version_history 

Previous versions: 

- [1.3.0](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/bbd9189b6c598c77059da184995c83b4037cbd73/_module_templates/macros.md#1) :Add module\_id to macros for creating the REDCap survey link
- [1.2.1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/a9aa1b38fc51db4252c9547654d9e36dba7864e5/_module_templates/macros.md#1): make CSS come from GCS
- [1.1.0](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/ad25398d0eef884402cff0f0c4fb4ca360d3b8f4/_module_templates/macros.md#1): Add current\_version\_description and version\_history metadata.

@end



@overview
<div class = "overview">

## Overview
@comment

**Why is this content relevant?** @long_description

**Estimated time to completion:** @estimated_time_in_minutes minutes

**Learning Objectives**

After completion of this module, learners will be able to:

@learning_objectives

</div>

@end

@make_survey_url
<script modify="false">
function makeURL(title, version, module_type, module_id) {
  let url = new URL('https://redcap.chop.edu/surveys');
  url.searchParams.set('s', 'KHTXCXJJ93');
  url.searchParams.set('module_name', title);
  url.searchParams.set('version', version);
  url.searchParams.set('module_type', module_type);
  url.searchParams.set('module_id', module_id);
  return url;
}
var surveyURL = makeURL(@0, @1, @2, @3);

send.html(`<a href="${surveyURL}")">our brief survey</a>`)
</script>
@end

@attribution

Credit for the original versions and origin of these materials is given to the [Data and Analytics for Research Training (DART) Program](https://arcus.github.io/education_modules/) and the [Children's Hospital of Philadelphia (CHOP) Research Institute](https://www.research.chop.edu/).

<!-- style="max-width: 300px; margin: auto;" -->
![](https://github.com/arcus/education_modules/raw/main/assets/media/chop-logo.svg)

@end

@recap

In the beginning, we stated some goals.

**Learning Objectives:**

After completion of this module, learners will be able to:

@learning_objectives

@end


@gifPreload
<script>
(function($) {

  // Get the .gif images from the "data-alt".
	var getGif = function() {
		var gif = [];
		$('img').each(function() {
			var data = $(this).data('alt');
			gif.push(data);
		});
		return gif;
	}

	var gif = getGif();

	// Preload all the gif images.
	var image = [];

	$.each(gif, function(index) {
		image[index]     = new Image();
		image[index].src = gif[index];
	});

	// Change the image to .gif when clicked and vice versa.
	$('figure').on('click', function() {

		var $this   = $(this),
				$index  = $this.index(),

				$img    = $this.children('img'),
				$imgSrc = $img.attr('src'),
				$imgAlt = $img.attr('data-alt'),
				$imgExt = $imgAlt.split('.');

		if($imgExt[1] === 'gif') {
			$img.attr('src', $img.data('alt')).attr('data-alt', $imgSrc);
		} else {
			$img.attr('src', $imgAlt).attr('data-alt', $img.data('alt'));
		}

		// Add play class to help with the styling.
		$this.toggleClass('play');

	});

})(jQuery);
</script>
@end

@sectiontoc
<script run-once>
    let current = document.getElementById("focusedToc");
    let elements = document.querySelectorAll('.lia-toc__link');
    let section = [];
    let contains = false;

    for (let element of elements) 
    {
        // reset the list of sections
        if (element.classList.contains('lia-toc__link--is-lvl-1'))
        {
            // but if this was the section that contains the current element, we are done
            if (contains) break;
            section = [];
        }
        else if (element.classList.contains('lia-toc__link--is-lvl-2'))
            section.push( [ 0, element ] );
        else if (element.classList.contains('lia-toc__link--is-lvl-3'))
            section.push( [ 1, element ] );

        if ( element === current )
            contains = true;
    }

    let md = "LIASCRIPT: \n";
    for (let [lvl, element] of section)
        md += "  ".repeat(lvl) + "- [" + element.textContent + "](" + element.getAttribute('href') + ")\n\n";
    md
</script>
@end

script: https://kit.fontawesome.com/83b2343bd4.js
script:  https://code.jquery.com/jquery-3.6.0.slim.min.js

-->

# Module Macros

@overview

## Recap

@recap
