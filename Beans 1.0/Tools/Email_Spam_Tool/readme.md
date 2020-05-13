Author: Pr0t_N0fg4n at 2020/04

##Run using the python3.

All the files need to be in the same path.

in case of errors please send it to me :)

If you want to put emails in ```email_list.txt``` you'll need toseparate the email and password using a space. One email and pass for each line.

The ```emails_to_list.txt``` are your victim email. One email for each line.

Your spam message need to be on ```text_message.txt``` file. (only plain text)

If you don't want to attach documents or images on your message comment all the lines starting on ```16 to 34``` on the ```msg_create.py``` file

Your email "Title" need to be in ```msg['Subject']``` on the ```msg_create.py``` file ```(line 13)```
the ```rand``` variable are a counter, if you want to remove it just exclude the ```%s``` and the ```%(rand)``` on subject


For now i have add only the gmail, rambler (russian email service) and yahoo servers but if you want you can add anyone. send me a pm if you do :D


1.3 News -
	Gmail error: ```run connect() first``` fixed. (But when you send a lot of messages the gmail server send this again, and i can't resolve that)
	Error: always show the login succefful fixed.
	
	
1.4 Plans -
	Outlook/Hotmail servers
	Fix Error: If using proxys a time out error make the program jump and never come back to a from email 

Thx, have fun
