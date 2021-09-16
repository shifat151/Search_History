$(function () {
    $loader = $(".loading-div");
    $(".datepicker").datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: "2000:2040",
        dateFormat: "yy-mm-dd",
        defaultDate: '',
        showAnim: "slideDown"
        // You can put more options here.

    });


    $(".form-check-input, .datepicker").on("change", function () {

        $("#search-reults").html($loader.show());
        var filterObj = {}
        $(".form-check-input").each(function (index, ele) {
            var filterKey = $(this).data('filter');
            filterObj[filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + filterKey + ']:checked')).map(function (el) {
                return el.value;
            });
        });

        if ($('#startdate').datepicker('getDate') !== null) {
            var startdate = $('#startdate').datepicker('getDate');
            filterObj["startdate"] = startdate.getTime() / 1000;
        }
        if ($('#enddate').datepicker('getDate') !== null) {
            var enddate = $('#enddate').datepicker('getDate');
            filterObj["enddate"] = enddate.getTime() / 1000;
        }

        // console.log(_filterObj)

        $.ajax({
            url: 'search-result/filters/',
            data: filterObj,
            dataType: 'json',
            success: function (data) {
                $("#search-reults").html(data.results);
            },
            error: function (response) {
                $("#search-reults").html("<p>Sorry! No search result was found!</p>");

            },
        });

    });
});

// $("#startdate").on("change", function () {
//     console.log($(this).datepicker('getDate'));
// });

