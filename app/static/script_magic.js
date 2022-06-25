let tomWaypointCounter = 0;
let starting_destination_selected = false

const addNewWaypoint = (event) => {
    const $elem_address = $('#new_waypoint_address');
    const $elem_city = $('#new_waypoint_city');
    const $container = $('#waypoint-container');
    tomWaypointCounter += 1;
    $container.append(`
    <div class="field" name="waypoint" id="waypoint[${tomWaypointCounter}]">
        <nav class="level">
            <input class="input" type="text" name="waypoint_address[${tomWaypointCounter}]" value="${$elem_address.val()}" readonly>
            <input class="input" type="text" name="waypoint_city[${tomWaypointCounter}]" value="${$elem_city.val()}" readonly>
            
            <input class="button" type="radio" name="is_starting_destination" id="is_destination[${tomWaypointCounter}]" value="${$elem_address.val()}" onchange="handleChange('is_destination[${tomWaypointCounter}]')" style="color: #3b3b3b">
                <i class="fa-solid fa-arrow-right-from-bracket" id="buttonIcon"></i>
            </input>
            
            <input class="button" type="button" onclick="removeWaypoint('waypoint[${tomWaypointCounter}]', 'is_destination[${tomWaypointCounter}]')" style="color: #3b3b3b">
                <i class="fas fa-light fa-trash-can" id="buttonIcon"> </i>
            </input>
        </nav>
    </div>
    `);
    $elem_address.val('');
    $elem_city.val('');
};

function removeWaypoint(id_name, is_destination_id) {
    if (document.getElementById(is_destination_id).checked){
        starting_destination_selected = false
    }
    document.getElementById(id_name).remove()
}

function handleChange(is_destination_button) {
    let is_destination_NodeList = document.getElementsByName("is_starting_destination")
    starting_destination_selected = true
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
    if (document.getElementsByName("waypoint").length <= 1) {
        alert("Veuillez saisir au moins deux adresses")
        return false
    } 

    if (starting_destination_selected == false) {
        alert("Veuillez sélectionner la destination de départ")
        return false
    }

    for (let i = 0; i < document.querySelectorAll('input[name^="waypoint"]').length; i++) {
        let item = document.querySelectorAll('input[name^="waypoint"]')[i];
        if (item.value == ""){
            alert("Veuillez vérifier vos adresses pour voir si l'une d'entre elles est vide")
            return false
        }
    }

    return true
}
