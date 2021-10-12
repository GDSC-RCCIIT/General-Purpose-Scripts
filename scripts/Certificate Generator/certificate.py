import smtplib, ssl
from PIL import Image, ImageDraw, ImageFont
import csv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def add_data(name: str, email: str):
    data_dict = [{"Name": name, "Email": email}]
    fields = ['Name', 'Email']

    with open("Data.csv", 'a') as file:

        #creating writer object
        writer = csv.DictWriter(file, fieldnames=fields)

        #writing data
        writer.writerows(data_dict)

        file.close()
        
def generate(name: str, certificate: str, font_path: str):

    text_pos_y = 630
    ink = (255,255,255)

    #open certificate template
    img = Image.open('certificate.png', mode='r')

    #gets width and height
    img_width = img.width

    #replicate template
    draw = ImageDraw.Draw(img)

    #specifying font
    font = ImageFont.truetype(
            font_path,
            150,
            )
    
    text_width, _ = draw.textsize(name, font = font)   
    
    draw.text(
        (
            (img_width - text_width) /2,
            text_pos_y
        ),
        name,
        fill=ink,
        font=font,
    )
    
    # saves the image in png format
    img.save("{}.pdf".format(name)) 

def send_mail(receiver_mail: str, name: str):
    port = 465  # For SSL
    password = "Googleisdumb"


    # Create a secure SSL context
    sender_email = 'programtester66@gmail.com'
    #creating the message
    msg_text = "Greetings " + name + ", \n PFA your certificate of appreciation owing to your invaluable contributions to our company."
    message = MIMEMultipart("alternative")
    message['Subject'] = "Certificate"
    message['To'] = email
    message['From'] = sender_email
    part1 = MIMEText(msg_text, 'plain')
    message.attach(part1)

    filename = name + '.pdf'

    with open(filename, 'rb') as certificate:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(certificate.read())
    
    encoders.encode_base64(part)

    part.add_header(
    "Content-Disposition",
    f"certificate; filename= {filename}",
)

    # Add attachment to message and convert message to string
    message.attach(part)

    # send message
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_mail, message.as_string())


if __name__ == "__main__":

    #Name to put on certificate
    name = input("Enter Name: ")

    #Email where to send
    email = input("Enter email address of recipient: ")

    #path of template
    template = "C:/Users/jayan/Vs Code/Hacktoberfest/Certificate Template.jpg" 

    #path for font
    font_path = "C:/WINDOWS/FONTS/GABRIOLA.TTF"

    #Calling functions
    add_data(name, email)
    generate(name, template, font_path)
    send_mail(email, name)
