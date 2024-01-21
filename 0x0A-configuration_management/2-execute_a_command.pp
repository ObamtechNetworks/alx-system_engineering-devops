# a puppet manifest to kill a process named killmenow
# Requirements: must use `exec` puppet resource
# must use `pkill`

# Define command_name
$run_cmd = 'pkill -f killmenow'

# execute command
exec { 'kill process named `killmenow':
  command => $run_cmd,
  path    => ['usr/bin', '/bin', 'usr/sbin', 'sbin'],
}
