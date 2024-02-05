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
        'author_id' => $cust_id,
        'alarms' => array(
            'trigger' => '-P10M',
            'notice' => 'Автоматически созданное напоминание через телеграмм бота'
        ),
        'type_id' => '2',
        'connections' => array(
            'object_type' => 'crm_sale',
            'object_id' => $argv[1]
        )
    ),
));

$insert_status = $api->updateSales(array( 
	array(    
        'id' => $argv[1],
        'sales_status_id' => $argv[2]
	),  
));

#$evnt_id = (int)$argv[1] - 54471;

/*$insert_status = $api->getEventsFilter(array( 
    'event_id' => '33366',
	),  
);*/

print_r($insert);
print_r($insert_status);

?>
