all:

	chmod 777 *.py
	
	./game_2048.py

clean:
	rm -fr *~ *.pyc score_file.txt

	clear

