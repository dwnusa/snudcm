# original path: /etc/nginx/sites-available/snudcm
# symolic link path: /etc/nginx/sites-enabled/snudcm
# ln -s /etc/nginx/sites-available/snudcm /tec/nginx/sites-enabled

server {
	listen 80;
	server_name 18.219.244.83;
	# server_name 127.0.0.1;

	location = /favicon.ico {access_log off; log_not_found off;}

	location /static/ {
		root /home/ubuntu/snudcm;
	}

	location / {
		include proxy_params;
		proxy_pass http://unix:/home/ubuntu/run/gunicorn.sock;
		# proxy_pass http://127.0.0.1:8000;
	}
}
