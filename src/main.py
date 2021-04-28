from lib.types import IStdin, IStdout

def main(stdin: IStdin, stdout: IStdout):
    stdout.write('*** You are a student at PWN_University and you are all set to graduate at the end of the semester. Unfortunately the night before graduation you learned you were going to fail your last class and now you’re afraid the school wont let you graduate. Luckily you have a friend in IT and after hearing of your situation he casually sends you a message with the IP address for one of the schools secure servers. Your goal is to hack into the server and figure out a way to change your grade! ***\n')
    stdout.write('\n')
    stdout.write('You are requesting access to an offical PWN_University server. Only authorised individuals are allowed further.\n')
    stdout.write('\n')
    stdout.write('*** You remember one of your IT friends who works for the university keeps their username encoded on their desk incase they forget the spelling. So you go to their desk and find out its MTMzN3VzZXI= ***\n')
    stdout.write('\n')
    stdout.write('Enter your username: ')
    stdout.flush()
    username = stdin.readline().strip('\n')
    if username == '1337user':
        stdout.write('\n')
        stdout.write('*** You then remember there was a data breach of all university passwords. Luckily PWN_University does not store their passwords in plain text, but rather in MD5 hashes. You navigate to the one associated with your friends username and it is 90f2c9c53f66540e67349e0ab83d8cd0 ***\n')
        stdout.write('\n')
        stdout.write('Now please enter your password: ')
        stdout.flush()
        password = stdin.readline().strip('\n')
        if password == 'p@ssword':
            stdout.write('Login Successful!\n')
            stdout.write('\n')
            stdout.write('*** Now that you have logged into the server you remember your IT friend implying that the database of grades is a mysql databse. Maybe you should try changing directories to where that is commonly stored (please use the full path) ***\n')
            stdout.write('\n')
            stdout.write('~$ ')
            stdout.flush()
            path = stdin.readline().strip('\n')
            if path == 'cd /var/lib/mysql':
                stdout.write('\n')
                stdout.write('*** Wow it looks like your getting close you are now in the mysql directory. You run some SQL queries on the grades database and are able to select the string that says \'PWNER1337 has a F\'. All you have to do is replace F with an A (type in the SQL command to do this bellow) ***\n')
                stdout.write('\n')
                stdout.write('mysql> ')
                stdout.flush()
                sql = stdin.readline().strip('\n')
                #if sql == 'REPLACE(\'PWNER1337 has a F\', \'F\', \'A\');':
                if 'REPLACE' in sql and 'PWNER1337' in sql and 'F' in sql and 'A' in sql:
                    stdout.write('\n')
                    stdout.write('*** Congratulations you changed your grade from an F to an A. Unfortunatly the university caught you in the act, but because you were able to hack PWN_University they decided to let you graduate after all! ***\n')
                    stdout.write('\n')
                    stdout.write('*** Present this flag to the challenge oragnizer to claim your prize! flag{CI_NETSEC_1ST_COMP}\n')
                else :
                    stdout.write('\n')
                    stdout.write('*** Oh no looks like you entered the wrong SQL command maybe you should try reconnecting to the server and try another answer... ***\n')
            else :
                stdout.write('\n')
                stdout.write('*** Oh no looks like you entered the wrong path maybe you should try reconnecting to the server and try another answer... ***\n')
            
        else :
            stdout.write('\n')
            stdout.write('Thats not the correct password access denied!\n')
            stdout.write('*** Oh no looks like your access was denied maybe you should try reconnecting to the server and try another answer... ***\n')
    else :
        stdout.write('\n')
        stdout.write('Thats not a valid username access denied!\n')
        stdout.write('*** Oh no looks like your access was denied maybe you should try reconnecting to the server and try another answer... ***\n')
