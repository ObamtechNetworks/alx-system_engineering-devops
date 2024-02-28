# using puppet to run ssh client configuration

# Get the home directory of the current user
$user_home = $facts['os']['family'] ? {
  'windows' => $facts['env']['USERPROFILE'],
  default   => $facts['env']['HOME'],
}

# Define variables for the private key path and passphrase authentication
$private_key = "${user_home}/.ssh/school"
$passkey_auth = 'no'

# Execute command to create or modify the SSH client configuration file
file { "${user_home}/.ssh/config":
  ensure  => 'file',  # Ensure that the file exists
  content => "Host mypuppet_config\n\tHostName 54.237.76.176\n\tUser ubuntu\n\tIdentityFile ${private_key}\n\tPasswordAuthentication ${passkey_auth}\n"
}
