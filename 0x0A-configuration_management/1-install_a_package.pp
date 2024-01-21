# a puppet manifest to install `flask` from `pip3`
# Requirements `flask` version must be `2.1.0`

# Define package and version 
$package_name = 'flask'
$version = '2.1.0'


# install werkzeug
$werkzeug_package = 'werkzeug'
$werkzeug_version = '2.1.1'

# install flask with the specified version
package { $package_name:
  ensure   => $version,
  provider => 'pip3',
}

# install the werkzeug
package { $werkzeug_package:
  ensure   => $werkzeug_version,
  provider => 'pip3',
}
