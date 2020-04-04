# Configure Nginx so that its HTTP response contains a custom header
exec { 'conf_server':
    command  => sudo apt-get update&&sudo apt-get -y install nginx&&echo "Holberton School" | sudo tee /var/www/html/index.html&&sudo sed -i "/server_name _;/a rewrite ^/redirect_me https://twitter.com/Yulyzulu5 permanent;" /etc/nginx/sites-available/default&&sudo sed -i "11 a \ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf&&sudo service nginx restart,
    provider => shell,
}
