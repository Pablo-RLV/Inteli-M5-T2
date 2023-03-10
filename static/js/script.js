function change_values(x, y, z, r){
    $("#x_final").text(parseInt($("#x_final").text()) + x);
    $("#y_final").text(parseInt($("#y_final").text()) + y);
    $("#z_final").text(parseInt($("#z_final").text()) + z);
    $("#r_final").text(parseInt($("#r_final").text()) + r);
}

function get_positions(){
    $("#x_final").text($("#x").text());
    $("#y_final").text($("#y").text());
    $("#z_final").text($("#z").text());
    $("#r_final").text($("#r").text());
}

$(document).ready(function() {
    $('#update').click(function() {
        var x = $('#x_final').text();
        var y = $('#y_final').text();
        var z = $('#z_final').text();
        var r = $('#r_final').text();
        $.ajax({
            url: '/rota',
            type: 'POST',
            data: { x: x,
                    y: y,
                    z: z,
                    r: r,
            },
            success: function(response) {
                alert('Texto enviado com sucesso!');
                location.reload();
            },
            error: function(xhr, status, error) {
                alert('Erro ao enviar texto: ' + error);
                location.reload();
            }
        });
    });
});