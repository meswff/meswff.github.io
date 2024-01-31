<?php

    require_once 'usage.php'; //настройте данный конфигурационный файл



$result = $api->filterSales(array( 
    'byid' => $argv[1],
));


$cust_id = $result['data']['list']['0']['employee_id'];

$insert = $api->insertEvent(array( 
    'event' => array(
        'dtstart' => $argv[3],
        'dtend' => $argv[3],
        'description' => $argv[4],
        'summary' => 'Автоматически созданное напоминание через телеграмм бота',
        'connections' => $argv[1],
        'author_id' => $cust_id,
        'alarms' => array(
            'trigger' => '-P10M',
            'notice' => 'Автоматически созданное напоминание через телеграмм бота'
        ),
        'type_id' => '2'
    ),
));

$insert_status = $api->updateSales(array( 
	array(    
        'id' => $argv[1],
        'sales_status_id' => $argv[2]
	),  
));

print_r($insert);
print_r($insert_status);

?>
