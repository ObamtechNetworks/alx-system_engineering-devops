# Puppet manifest to ensure the occurrence of a 500 error is resolved and add specified requirements

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => file('/var/www/html/wp-settings.php').content.replace('phpp', 'php')
}
