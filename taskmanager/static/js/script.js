document.addEventListener('DOMContentLoaded', function () {

    // Sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Datepicker initialization
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmm, yyyy",
        i18n: {
            done: "Select"
        }
    });

    // select category dropdown initialization
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    // collapsible initialization 
    let collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);
});