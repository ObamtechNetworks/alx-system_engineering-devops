# Puppet manifest to ensure the occurrence of a 500 error is resolved and add specified requirements

exec {'replace':
 provider => shell,
 command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
