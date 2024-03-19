<?php

    require_once 'usage.php'; //настройте данный конфигурационный файл


$insert_status = $api->updateSales(array( 
	array(    
        'id' => $argv[1],
        'sales_status_id' => $argv[2]
	),  
));

print_r($insert_status);
?>
