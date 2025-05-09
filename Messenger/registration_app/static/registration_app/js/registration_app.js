let webSocket = new WebSocket(`ws://${window.location.host}/registration`)

webSocket.onmessage = function (event){

    let data = JSON.parse(event.data)

    if (data.type === 'connection_established'){

    }
} 