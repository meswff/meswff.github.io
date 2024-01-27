<?php

	require_once 'usage.php'; //настройте данный конфигурационный файл


$arg = json_decode($argv[1]);

$insert_status = $api->updateSales(array( 
	array(    
	'id' => $arg['0']['0'],
	'sales_status_id' => $arg['0']['1']
	),  
));

$insert = $api->insertEvent(array( 
	'dtend' => $arg['0']['2'],
	'description' => $arg['0']['3'],
	'summary' => 'Автоматически созданное напоминание через телеграмм бота',
	'connections' => $argv['0']['0']
));

print_r($insert_status);
print_r($insert);

?>
