let tomWaypointCounter = 0;

const addNewWaypoint = (event) => {
    const $elem = $('#new_waypoint');
    const $container = $('#waypoint-container');
    tomWaypointCounter += 1;
    $container.append(`
    <div class="field" id="waypoint[${tomWaypointCounter}]">
    <nav class="level">
    <input class="input" type="text" name="waypoint[${tomWaypointCounter}]" value="${$elem.val()}" readonly>
        <span class="button" onclick="removeWaypoint('waypoint[${tomWaypointCounter}]')" style="color: #3b3b3b">
            <i class="fas fa-light fa-trash-can"></i>     
        </span>
    </nav>
    </div>
    `);
    $elem.val('');
};

function removeWaypoint(id_name) {
    document.getElementById(id_name).remove()
}

