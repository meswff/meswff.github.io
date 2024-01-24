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
	$maximum_customer = max($data);
	$id_customer = $maximum_customer['customers_id'];

	$res_customer = $api->filterCustomers(array( 
		'byid' => $id_customer
	));
	
	if (!is_array($res_customer)) {
		$global_array = $data['0'];
	} else {
		$global_array = array_merge($data, $res_customer['data']['list']['0']);
	}

	$json = json_encode($global_array);

	print_r($json);

?>
