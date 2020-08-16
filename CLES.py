#!/usr/bin/env python3

# simple mail transfer protocol module
import smtplib

# Socket module imported for catching the exception socket.gaiaerror when no internet connection available
import socket

# Module used for attaching images to email from users operating system desktop
import os

# the EMAIL module is specifically for managing email and formating emails; does not send the email messages.
from email.message import EmailMessage

# MIME -- multipurpose internet mail extensions. Used for attaching images
from email.mime.image import MIMEImage

# takes a string but but will not display on screen. Used for users email password
import getpass


# displays software title on program startup and returns variable used as a line seperator for aesthetics
def software_title():
    __SEPERATOR__ = ("-" * 60)
    print('\n\n')
    print(__SEPERATOR__)
    print('T E R M I N A L  L I T E  E M A I L  S E N D E R')
    print('    - -  only what is needed [T.L.E.S]  -  - ')
    print(__SEPERATOR__)
    return __SEPERATOR__


# obtains users information with four mandatory fields. user email, email recipients, subject title, message body
# These 4 objects used [1] displaying to the user what they said [2] formatting the email in the EmailMessage() object
def user_information():

    # displays program information and takes users HOTMAIL or GMAIL response
    gmail_or_hotmail = input("Use the terminal to Send an email from your HOTMAIL account with ease. Please enter HOTMAIL now\n")

    # reminds the user to activate less secure apps if using GMAIL
    if gmail_or_hotmail == 'gmail' or gmail_or_hotmail == 'GMAIL':
        print(' > you chose gmail, be sure you have activated less secure apps')

    # senders email address
    input_sender = input('Y o u r  e m a i l: ')

    # taking users password but will not display on screen as as to getpass module functionality
    password = getpass.getpass('P a s s w o r d:')

    # recipients email address
    input_send_to = input("R e c i e v e r: ")

    # email subject title
    input_subject = input("S u b j e c t: ")

    # blank line for aesthetics
    print()
    input_message_body = input("m e s s a g e > >:  ")

    # creating two blank lines for aesthetics
    print()

    return input_sender, input_send_to, input_subject, input_message_body, password, gmail_or_hotmail


# displaying to the user what they have entered
def user_information_confirmation(input_sender, input_send_to, input_subject, input_message_body):


    print(__SEPERATOR__)
    print(f"s e n d e r: [{input_sender}] \n"
          f"r e c i e v e r: [{input_send_to}] \n"
          f"s u b j e c t: [{input_subject}] \n"
          f"m e s a g e: [{input_message_body} \n")


    # asking the user if the information above is correct
    while True:

        # retrieves user input
        is_information_correct = input('> > Is the information correct? type [Y] for yes or [N] for no: \n')

        # if user inputs y or Y, loop is broken and program execution continues
        if is_information_correct == 'y' or is_information_correct == 'Y':
            break

        # if user response is 'n' or 'N', program exited
        elif is_information_correct == 'n' or is_information_correct == 'N':
            exit('You chose to say your information is not correct. Program exited \n \n \n')

        # if user does not enter y,Y,n,No, while loop continues execution
        else:
            print('invalid response.\n')
    # seperator to close of user information confirmation
    print(__SEPERATOR__)


# Creating the Email format using the EmailMessage function from email.message module
def message_information(input_sender, input_send_to, input_subject, input_message_body):

    # creating the EmailMessage object that has all of the functionaility built into our_message
    our_message = EmailMessage()

    # the our_message  variable from the EmailMessage() object uses the same syntax as creating a dictionary[KEY] = VALUE
    our_message['Subject'] = input_subject
    our_message['From'] = input_sender
    our_message['To'] = input_send_to

    # creating the message body by using set_content function. input_message_body contains the information returned
    # when user_information function was executed.
    our_message.set_content(input_message_body)

    #returns the our_message object containing information from the EmailMessage() module
    return our_message


# allows user to attach a DESKTOP image to the email.
def attach_image():

    ''' TO DO:
        +  need to find a way to label image
        + NONE is printed out on the screen if the user selects NO. Remove this
        + make it so the file naviagtes to the users desktop. Use OS module
    '''

    print(__SEPERATOR__)

    # a tuple with the possible yes answer to attach an image
    yes_response_list = ('yes', 'Y', 'YeS', 'YES', 'y')

    # asking if user wants to input an image
    user_attach_image = input("A T T A C H  I M A G E ? [ Y ] or [ N ]:   ")

    # if it is true the user respone is in the yes_response_list tuple
    if user_attach_image in yes_response_list:

        # displaying desktop contents header
        print(__SEPERATOR__)
        print("D E S K T O P  C O N T E N T S ")
        print(__SEPERATOR__)

        # image file extensions to to display to user
        file_extension = ['.jpg', '.jpeg', '.gif', '.png']

        # the empty variable to recieve the Desktop Path
        desktop_folder = None

        # the desktop path for MACS. Paths are not case sensitive.
        try:
            desktop_folder = os.path.join(os.environ.get('HOME'), 'DESKTOP')
        except FileNotFoundError:
            pass
        # the desktop path for LINUX/UBUNTU. Paths are case sensitive
        try:
            desktop_folder = os.path.join(os.environ.get('HOME'), 'Desktop')
        except FileNotFoundError:
            print('It appears that you are neither using a MAC or LINUX')


        # gets the list of files on users desktop
        desktop_files_enumeration = enumerate(os.listdir(desktop_folder))

        # empty list for users to go into
        desktop_files_only_file_name = []

        # looping through the desktop images that have been returned
        for file_on_desktop in desktop_files_enumeration:

            # looping through the file extensions (e.g., .jpg)
            for extension in file_extension:

                # checking to see if the file extension string is in the desktop file. Here I have index[1] because the
                # enumerate function returns a two element tuple (number, file)  (7, 'kitten.jpg')
                if extension in file_on_desktop[1]:

                    #appending the file name only into the empty list created above
                    desktop_files_only_file_name.append(file_on_desktop[1])

        # displaying the list of user images desktop files appended into the list (e.g., \_ kitten.jpg )
        for user_files in desktop_files_only_file_name:
            print(f"\_ {user_files}")


        print(__SEPERATOR__)
        # taking image response the user wants to attach
        desktop_image = input(str("A T T A C H  W H I C H  I M A G E \n"
                                  "put in full file name and extension [e.g., kitten.jpg]"))
        print(__SEPERATOR__)

        # displays to user the image they attached to the email
        print(f"attached: {desktop_image}")

        # retrieving the destination path for the desktop image
        desktop_image_location = (os.path.join((desktop_folder), desktop_image))

        # opening (but not displaying) the image in pycharm
        image = open(desktop_image_location, 'rb')

        # creating a MIMEimage object and reading the image opened above
        img = MIMEImage(image.read())

        # attaching the image using the ADD_ATTACHMENT function to OUR_MESSAGE object we created using the
        # EmailMessage function from the EMAIL module.
        return our_message.add_attachment(img)

    # if user enter anything other then yes to the user_attach_image variable, then no image is attached.
    else:
        print(">> no image attached\n")
        return None

# CONNECTING, LOGGING INTO, and SENDING the email. Sending the our_message object created using the EmailMessage function
# from the EMAIL module
def sending_email_and_logging_in():

    if gmail_or_hotmail == 'gmail' or gmail_or_hotmail == 'GMAIL':
        connecting_to_email = smtplib.SMTP('smtp.gmail.com', 587)

    elif gmail_or_hotmail == 'hotmail' or gmail_or_hotmail == 'HOTMAIL':
        connecting_to_email = smtplib.SMTP('smtp.live.com', 587)

    else:
        exit('user did not enter hotmail or gmail')




    # Initates the TRANSPORT LAYER SECURITY enabling email encryption. I know this is working because.
    # In the sender information in sent email, it states - Standard encryption (TLS) Learn more
    # noinspection PyUnboundLocalVariable
    connecting_to_email.starttls()


    # sending the sender email and password entered to gmail or hotmail smtp server
    connecting_to_email.login(input_sender, password)

    # attaching the message body
    connecting_to_email.send_message(our_message)

    # displaying content to user
    print()
    print(__SEPERATOR__)
    print(f"E M A I L  S E N T >> {input_send_to}")
    print(__SEPERATOR__)
    print("C O N C A T E N A T I N G")
    print(__SEPERATOR__)

    # returning variable consitisting of smtplib object
    return connecting_to_email


#----------------------------------------------------------
# EXECTUGING THE PROGRAM
if __name__ == '__main__':
    while True:
        try:
            __SEPERATOR__ = software_title()


            # user_information function returns multiple variables, so they need to be stored in seperate vars
            input_sender, input_send_to, input_subject, input_message_body, password, gmail_or_hotmail = user_information()

            user_information_confirmation(input_sender, input_send_to,input_subject, input_message_body)
            our_message = message_information(input_sender, input_send_to, input_subject, input_message_body)
            attach_image()
            connecting_to_email = sending_email_and_logging_in()
            connecting_to_email.quit()
            break

        # SPECIFIC EXCEPTION CATCHING

        except smtplib.SMTPSenderRefused as errdata:
            print(f'[F A I L E D] Your sender email address has not been accepted.'
                  f' Did you enter it correctly? Program exited  // [{errdata}]')
            print('\n')
            exit()

        except smtplib.SMTPRecipientsRefused  as errdata:
            print(f'[F A I L E D] reciepients address does not exist.'
                  f'Did you enter it correctly? Program exited  // [{errdata}]')
            print('\n')
            exit()

        except (smtplib.SMTPConnectError) as errdata:
            print(f'[F A I L E D] Connection to your email serer failed. Program exited  // [{errdata}]')
            print('\n')
            exit()


        except smtplib.SMTPAuthenticationError as errdata:
            print(f'[F A I L E D] Authentication did not work. Is your username and password'
                  f'combination correct? Program exited // [{errdata}]')
            print('\n')
            exit()

        except FileNotFoundError as err:
            print(f'the file was not found on the DESKTOP. Place the file onto the desktop to send'
                  f'to the user or press N not to attach a file when prompted. Program exited [{err}]')
            exit()

        except socket.gaierror as err:
            print(f'[ F A I L E D ] Email not sent due to {err}. Are you connected to the internet?')
            exit()

        except TypeError as err:
            print(f'[ F A I L E D ] did you fill out all of the fields correctly? Program exited  {err}')
            exit()
