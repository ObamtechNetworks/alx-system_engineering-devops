# puppet code to configure nginx response header
# install nginx

package {'nginx':
  ensure => installed,
}

# customize content of the index.html
file { '/var/www/html/index.html':
  ensure => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure Nginx server block
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  root /var/www/html;
  index index.html index.htm;

  server_name obam.tech www.obam.tech;
  add_header X-Served-By $HOSTNAME;

  location / {
    try_files $uri $uri/ =404;
  }

  location = /redirect_me/ {
    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
  }

  location = /redirect_me {
    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
  }

  error_page 404 /404.html;
}',
  require => Package['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}
