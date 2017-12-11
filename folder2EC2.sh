 scp -i ../beiSentence.pem -r $1 ubuntu@54.152.38.60:beiSentenceTransport/
 ssh -i ../beiSentence.pem ubuntu@54.152.38.60 sudo cp -avr /home/ubuntu/beiSentenceTransport/$1 /var/www/html
