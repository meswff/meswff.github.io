<?php

    require_once 'usage.php'; //настройте данный конфигурационный файл

$insert_event = $api->getDocumentsFilter(array( 
	'event' => array(    
        'id' => $argv[1],
        'dtstart' => $argv[2],
        'dtend' => $argv[2],
        'dtoffset' => 180,
        )
	),  
);


$insert_event = $api->update_org(array( 
	'event' => array(    
        'id' => $argv[1],
        'dtstart' => $argv[2],
        'dtend' => $argv[2],
        'dtoffset' => 180,
        )
	),  
);

print_r($insert_event);

?>
