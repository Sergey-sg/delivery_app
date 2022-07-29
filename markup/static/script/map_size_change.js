function mapSizeChange() {
    let mapElement = document.querySelector('.map_canvas_wrapper')
    let map = document.getElementById('map_canvas')
    mapElement.style.marginLeft = "0";
    map.style.height = '300px';
}

window.addEventListener('load', mapSizeChange)