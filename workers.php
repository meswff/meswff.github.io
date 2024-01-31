<?php

	require_once 'usage.php'; //настройте данный конфигурационный файл
	
	$res = $api->filterEmployee(array( 
        'id' => $argv[1],
    ));

	$data = $res['data'];
    $maximum = max($data);
    $key = $maximum['fields']['3643']['value'];

	$json_byid = json_encode($key);

	print_r($json_byid);

?>