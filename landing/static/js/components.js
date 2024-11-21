$(document).ready(function() {
    $('.daterange').each(function() {
        var $input = $(this);
        $input.daterangepicker({
            opens: 'center',
            autoApply: true,
            locale: {
                format: 'DD/MM/YYYY'
            },
            drops: 'auto'
        }, function(start, end) {
            $input.val(`${start.format('DD/MM/YYYY')} - ${end.format('DD/MM/YYYY')}`);
        });
    });

    const searchSelectParams = document.querySelectorAll('.search-select-param');
    searchSelectParams.forEach(function(param) {
        const dropdownItems = param.querySelectorAll('.dropdown-item');
        const input = param.querySelector('input');

        dropdownItems.forEach(function(item) {
            item.addEventListener('click', function(e) {
                e.preventDefault();
                const value = this.getAttribute('data-value');
                input.value = value;
            });
        });
    });

    document.querySelectorAll('.glider').forEach(function(element) {
        new Glider(element, {
            slidesToShow: 1,
            dots: element.parentElement.querySelector('.dots'),
            draggable: true,
            arrows: {
                prev: element.parentElement.querySelector('.glider-prev'),
                next: element.parentElement.querySelector('.glider-next')
            }
        });
    });
});

