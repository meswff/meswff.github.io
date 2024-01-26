<?php

	require_once 'usage.php'; //настройте данный конфигурационный файл

    header('Content-Type: application/json');
    $aResult = array();
    echo json_encode($aResult);


	$res = $api->updateSales(array( 
        'id' => $argv[1],
        'sales_status_id' => $argv[2]
    ));
?>
