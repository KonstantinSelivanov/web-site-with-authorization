(function () {
    var jquery_version = '3.3.1';
    var site_url = 'http://127.0.0.1:8000/';
    var static_url = site_url + 'static';
    // Высота и ширина изображения
    var min_width = 100;
    var min_height = 100;

    function photostock(msg) {
        // код 
    };
    // JQuery connection check
    // Проверка подключения jQuery
    if (typeof window.jQuery != 'undefined'){
        photostock();
    } else {
        // Check that the attribute "window. $ Is not occupied by another object
        // Проверка, что атрибут window.$ не занят другим объектом
        var conflict = typeof window.$ != 'undefined';
        // Create <script> tag with jQuery loading
        // Создание тега <script> с загрузкой jQuery
        var script = document.createElement('script');
        script.src = '//ajax.googleapis.com/ajax/libs/jquery' + jquery_version + '/jquery.min.js';
        // Adding a tag to the <head> block of a document
        // Добавление тега в блок <head> документа
        document.head.appendChild(script);
        // Adding the ability to use multiple tries to load jQuery
        // Добавление возможности использовать несколько попыток для загрузки jQuery
        var attempts = 15;
        (function () {
            // JQuery connection check
            // Проверка подключения jQuery
            if (typeof window.jQuery == 'undefined') {
                if (--attempt > 0) {
                    // If jQuery is not connected, try to load again
                    // Если не подключен jQuery, пытаемся снова загрузить
                    window.setTimeout(arguments.callee, 250)
                } else {
                    // JQuery load attempts exceeded, display message
                    // Превышено число попыток загрузки jQuery, выводим сообщение
                    alert('Ошибка при загрузке jQuery')
                }
            } else {
                photostock();
            }
        })();
    }
})()