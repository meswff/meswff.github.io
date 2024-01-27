<?php

	require_once 'usage.php'; //настройте данный конфигурационный файл


	/*$res = $api->updateSales(array( 
        'id' => $argv[1],
        'sales_status_id' => $argv[2]
    ));*/
$arg = json_decode($argv[1])

$insert_status = $api->updateSales(array( 
	array(    
	'id' => $argv[1],
	'sales_status_id' => $argv[2]
	),  
));

$insert = $api->insertEvent(array( 
	'dtend' => $argv[3],
	'description' => $argv[4],
	'summary' => 'Автоматически созданное напоминание через телеграмм бота',
	'connections' => $argv[1]
));

print_r($insert_status);

?>
