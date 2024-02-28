# ssh_config.pp

# Ensure SSH client configuration
file { '/home/ubuntu/.ssh/config':
  ensure => present,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
  content => '
    Host ubuntu
      HostName 3.85.41.84
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ',
}
