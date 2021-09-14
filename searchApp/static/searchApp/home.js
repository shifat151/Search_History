$(function () {
    $(".datepicker").datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: "2000:2040",
        dateFormat: "yy-mm-dd",
        defaultDate: '',
        showAnim: "slideDown"
        // You can put more options here.

    });
});

$("#startdate").on("change", function () {
    console.log($(this).datepicker('getDate'));
});

