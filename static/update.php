<?php

	require_once 'usage.php'; //настройте данный конфигурационный файл
	
	$res = $api->updateSales(array( 
        'id' => $argv[1],
        'sales_status_id' => $argv[2]
    ));
?>