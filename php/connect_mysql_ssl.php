<?php echo '<h1>Page loaded with PHP!</h1>';
  
$mysqli = mysqli_init();
$mysqli->options(MYSQLI_OPT_SSL_VERIFY_SERVER_CERT, true);
$mysqli->ssl_set(NULL, NULL, "/usr/share/ca-certificates/mozilla/Baltimore_CyberTrust_Root.crt", NULL, NULL);

$link = mysqli_real_connect($mysqli, 'dbhost', 'dbuser', 'dbpasswd', 'db', 3306, NULL, MYSQLI_CLIENT_SSL);

if (!$link)
{
    die ('Connect error (' . mysqli_connect_errno() . '): ' . mysqli_connect_error() . "\n");
} else {
    $res = $mysqli->query('SHOW TABLES;');
    print_r ($res);
    $mysqli->close();
}

?>

