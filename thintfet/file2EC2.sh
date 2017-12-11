 scp -i ../beiSentence.pem $1 ubuntu@ec2-52-87-238-25.compute-1.amazonaws.com:beiSentenceTransport
 ssh -i ../beiSentence.pem ubuntu@ec2-52-87-238-25.compute-1.amazonaws.com sudo mv /home/ubuntu/beiSentenceTransport/$1 /var/www/html
