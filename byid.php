<?php

	require_once 'usage.php'; //настройте данный конфигурационный файл
	
	$res = $api->getSalesChangeStage(array( 
		'date_start' => "2024-01-01",
     	'date_end' => "2030-01-01"
	));

	$data = $res['data']['list'];
	$maximum = max($data)['sale_id'];

	$result = $api->filterSales(array( 
		'byid' => $maximum
	));

	$data = $result['data']['list'];
	$id_customer = $data['0']['customers_id'];

	$res_customer = $api->filterCustomers(array( 
		'byid' => $id_customer
	));
	
	if (!is_array($res_customer)) {
		$json_byid = json_encode($data['0']);
	} else {
		$json_byid = json_encode(array_merge($data['0'], $res_customer['data']['list']['0']));
	}

	print_r($json_byid);

?>
