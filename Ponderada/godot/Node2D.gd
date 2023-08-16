extends Node2D

func _process(delta):
	$HTTPRequest.request("https://nbo2vi-5000.csb.app/get", [], false, HTTPClient.METHOD_GET)	

func _on_request_error(error):
	print("Erro na solicitação: ", error)

func _on_HTTPRequest_request_completed(result, response_code, _headers, body):
	if result == HTTPRequest.RESULT_SUCCESS:
		var json = JSON.parse(body.get_string_from_utf8())
		var id = String(json.result["id"])
		var x = int(json.result["x"])
		var y = int(json.result["y"])
		var z = int(json.result["z"])
		var r = int(json.result["r"])
		$CanvasLayer/Label_id.text = "ID = " + str(id)
		$CanvasLayer/Label_x.text = "X = " + str(x)
		$CanvasLayer/Label_y.text = "Y = " + str(y)
		$CanvasLayer/Label_z.text = "Z = " + str(z)
		$CanvasLayer/Label_r.text = "R = " + str(r)
		escala(z)
		$Sprite.position.x = x
		$Sprite.position.y = y
		$Sprite.rotation_degrees = r
	else:
		print("Erro na solicitação: ", response_code)

func escala(z):
	if z < 0:
		z = -z
	if z > 200:
		z = 200
	if z < 10:
		z = 0.25
	$Sprite.scale.x = z/75
	$Sprite.scale.y = z/75
