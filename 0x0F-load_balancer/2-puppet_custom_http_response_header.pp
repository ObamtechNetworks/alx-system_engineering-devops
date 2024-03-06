# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx server block with custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  root /var/www/html;
  index index.html index.htm;

  server_name obam.tech www.obam.tech;
  
  # Custom HTTP header X-Served-By with the hostname
  add_header X-Served-By ${::hostname};

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
}
",
  require => Package['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
