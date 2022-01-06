// Отслеживаем на предмет наведения и отвода курсора на область карти
$(document).ready(function() {
    $('.part').on('mouseover', within_the_area);
    $('.part').on('mouseout', outside_the_area);
});

// Когда курсор в пределах области
function within_the_area() {
    $.ajax({
        data: {'value': $(this).attr('value')},
        url: '{% url 'return_queryset' %}',
        success: function (resp) {
            $('.cont').html(resp.queryset);
            $('.cont2').html(resp.value2);
        },
        error: function (resp) {
            console.log(resp.message);
        }
    });
    $('.username').html($(this).attr('information'));
    $('.model-content').fadeIn();
}
// Когда курсор вне области всей карты
function outside_the_area() {
    $('.model-content').hide();
}




function city() {
    $.ajax({
        data: {'value': $(this).attr('value')},
        url: "{% url 'return_of_city' %}",
        success: function (resp) {
            $('.cont').html(resp.information);
            $('.cont2').html(resp.information);
            $('.cont3').html(resp.information);
            $('.cont4').html(resp.information);
        },
        error: function (resp) {
            console.log(error message);
        }
    });
}
$document.ready(function(){
    city();
    setInterval('city()', 10000)
})
