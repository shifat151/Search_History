$(function () {
    $("#startdate").datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: "2000:2040",
        dateFormat: "yy-mm-dd",
        defaultDate: '',
        showAnim: "slideDown"
        // You can put more options here.

    });
    $("#enddate").datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: "2000:2040",
        dateFormat: "yy-mm-dd",
        defaultDate: '',
        showAnim: "slideDown"
        // You can put more options here.

    });
    $(".form-check-input, .datepicker").on("change", function () {
        var _filterObj = {}
        $(".form-check-input").each(function (index, ele) {
            var _filterKey = $(this).data('filter');
            _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function (el) {
                return el.value;
            });
            console.log('now');
        });

        if ($('#startdate').datepicker('getDate') !== null) {
            var startdate = $('#startdate').datepicker('getDate');
            _filterObj["startdate"] = startdate.getTime() / 1000;
        }
        if ($('#enddate').datepicker('getDate') !== null) {
            var enddate = $('#enddate').datepicker('getDate');
            _filterObj["enddate"] = enddate.getTime() / 1000;
        }

        console.log(_filterObj)

        $.ajax({
            url: 'search-result/filters/',
            data: _filterObj,
            dataType: 'json',
            success: function (data) {
                console.log(data);
                $("#search-reults").html(data.results);
            }
        });

    });
});

// $("#startdate").on("change", function () {
//     console.log($(this).datepicker('getDate'));
// });

