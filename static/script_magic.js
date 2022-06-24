let tomWaypointCounter = 0;

const addNewWaypoint = (event) => {
    const $elem = $('#new_waypoint');
    const $container = $('#waypoint-container');
    tomWaypointCounter += 1;
    $container.append(`
    <div class="field" id="waypoint[${tomWaypointCounter}]" name="test">
        <nav class="level">
            <input class="input" type="text" name="waypoint[${tomWaypointCounter}]" value="${$elem.val()}" readonly>
            
            <input class="button" type="radio" name="is_starting_destination" id="is_destination[${tomWaypointCounter}]" value="${$elem.val()}" onchange="handleChange('is_destination[${tomWaypointCounter}]')" style="color: #3b3b3b">
                <i class="fa-solid fa-arrow-right-from-bracket" id="buttonIcon"></i>
            </input>
            
            <input class="button" type="button" onclick="removeWaypoint('waypoint[${tomWaypointCounter}]')" style="color: #3b3b3b">
                <i class="fas fa-light fa-trash-can" id="buttonIcon"> </i>
            </input>
        </nav>
    </div>
    `);
    $elem.val('');
};

function removeWaypoint(id_name) {
    document.getElementById(id_name).remove()
}

function handleChange(is_destination_button) {
    let is_destination_NodeList = document.getElementsByName("is_starting_destination")
    is_destination_button = document.getElementById(is_destination_button)

    for (let i = 0; i < is_destination_NodeList.length; i++) {
        let item = is_destination_NodeList[i];
        item.className = "button is-white"
    }

    if (is_destination_button.checked) {
        is_destination_button.className = "button is-dark"
    }
}

function required() {
    // Here goes form validation
    return false
}
