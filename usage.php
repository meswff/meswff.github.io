<?php
    /* Вариант использования без composer*/
	require_once  'Intrum/Api.php';
	require_once  'Intrum/Cache.php';
	
	/*Intrum\Cache::getInstance()->setup(
		array(
			"folder" => __DIR__ . "/cache",
			"expire" => 600
		)
	);*/
	
	$api = Intrum\Api::getInstance()
	->setup(
		array(
			"host"   => "aires.astoria-tula.ru",//"yourdomain.intrumnet.com",
			"apikey" => "21d1c8300ca07c06bf8f3aac3c16c275",
			"cache"  => false,
			"port"   => 80
		)
	);
?>