/*
 Tooltips and Popovers must be initialized with jQuery: select the specified element and call the tooltip() or popover() methods.
*/

$(function() {
    $('[data-toggle="tooltip"]').tooltip();
});

$(function() {
    $('[data-toggle="popover"]').popover();
});

