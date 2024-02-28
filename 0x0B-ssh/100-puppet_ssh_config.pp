# using puppet to run ssh client configuration

$private_key = '~/.ssh/school'
$passkey_auth = 'no'

# execute command
file { '/home/ubuntu/.ssh/config':
  ensure => 'file',
  content => "Host mypupet_config\n\tHostName 54.237.76.176\n\tUser ubuntu\n\tIdentityFile ${private_key}\n\tPasswordAuthentication ${passkey_auth}\n"
}
